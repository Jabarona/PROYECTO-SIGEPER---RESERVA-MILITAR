from django.views.generic import ListView, View
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.apps import apps
from django.db.models import Q


#--------------------ingreso de resoluciones-----------------------------------------#
class IngresoResolucionView(LoginRequiredMixin, View):
    def get(self, request):
        # Inicializa todos los formularios
        ascenso_form = ResolucionAscensoForm()
        condecoracion_form = ResolucionMedallaForm()
        cambio_escalafon_form = ResolucionCambioEscalafonForm()
        cambio_institucion_form = ResolucionCambioInstitucionForm()
        
        reservistas = ReservistaModel.objects.all()
        medallas = ConedecoracionModel.objects.all()
        grados = GradoModel.objects.all()        
        armas = ArmaServicioModel.objects.all()
        
        PROCEDENCIA_CHOICES = [
        ('Ejercito', 'Ejercito'),
        ('Armada', 'Armada'),
        ('Fuerza Aerea', 'Fuerza Aerea')
        ]
        TIPO_RESOLUCION_CHOICES = [
        ('Ascenso', 'Ascenso'),
        ('Nombramiento', 'Nombramiento')
        ]

        context = {
            'ascenso_form' : ascenso_form,
            'condecoracion_form' : condecoracion_form,
            'cambio_escalafon_form' : cambio_escalafon_form,
            'cambio_institucion_form' : cambio_institucion_form,
            
            'reservistas':reservistas,
            'medallas': medallas,
            'grados': grados,
            'armas': armas,
            'PROCEDENCIA_CHOICES' :PROCEDENCIA_CHOICES,
            'TIPO_RESOLUCION_CHOICES':TIPO_RESOLUCION_CHOICES,
        }


        return render(request, 'actos_administrativos/ingreso_resol.html', context)

    
    
    def post(self, request, *args, **kwargs):
        # Obtiene el tipo de formulario que se envió
        form_type = request.POST.get('form_type')
        print (form_type)
        print("Datos enviados desde el formulario:", request.POST)

        # Inicializa el formulario correspondiente
        if form_type == 'res_ascenso':
            ascenso_form = ResolucionAscensoForm(request.POST, request.FILES)
            if ascenso_form.is_valid():                
                ascenso_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("ingreso_resolucion")}?tab=res_ascenso')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("ingreso_resolucion")}?tab=res_ascenso')
            
            
        elif form_type == 'res_condecoracion':
            condecoracion_form = ResolucionMedallaForm(request.POST)
            if condecoracion_form.is_valid():
                print("Datos validados:", condecoracion_form.cleaned_data)
                condecoracion_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("ingreso_resolucion")}?tab=res_condecoracion ')
            else:                
                print("Errores de validación:", condecoracion_form.errors)
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("ingreso_resolucion")}?tab=res_condecoracion')
            
        elif form_type == 'res_escalafon':
            cambio_escalafon_form = ResolucionCambioEscalafonForm(request.POST, request.FILES)
            if cambio_escalafon_form.is_valid():
                cambio_escalafon_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("ingreso_resolucion")}?tab=res_escalafon')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("ingreso_resolucion")}?tab=res_escalafon')
            
        elif form_type == 'res_institucion':
            cambio_institucion_form = ResolucionCambioInstitucionForm(request.POST, request.FILES)
            if cambio_institucion_form.is_valid():
                cambio_institucion_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("ingreso_resolucion")}?tab=res_institucion')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("ingreso_resolucion")}?tab=res_institucion')

        
            
        # Si ningún formulario es válido o se envió un formulario desconocido, inicializa todos los formularios de nuevo
        ascenso_form = ResolucionAscensoForm()
        condecoracion_form = ResolucionMedallaForm()
        cambio_escalafon_form = ResolucionCambioEscalafonForm()
        cambio_institucion_form = ResolucionCambioInstitucionForm()

        reservistas = ReservistaModel.objects.all()
        medallas = ConedecoracionModel.objects.all()
        grados = GradoModel.objects.all()
        armas = ArmaServicioModel.objects.all()
        
        PROCEDENCIA_CHOICES = [
        ('Ejercito', 'Ejercito'),
        ('Armada', 'Armada'),
        ('Fuerza Aerea', 'Fuerza Aerea')
        ]
        TIPO_RESOLUCION_CHOICES = [
        ('Ascenso', 'Ascenso'),
        ('Nombramiento', 'Nombramiento')]
        
        context = {
            'ascenso_form' : ascenso_form,
            'condecoracion_form' : condecoracion_form   ,
            'cambio_escalafon_form' : cambio_escalafon_form,
            'cambio_institucion_form' : cambio_institucion_form,
            
            'reservistas':reservistas,
            'medallas': medallas,
            'grados':grados,
            'armas': armas,
            'PROCEDENCIA_CHOICES' :PROCEDENCIA_CHOICES,
            'TIPO_RESOLUCION_CHOICES':TIPO_RESOLUCION_CHOICES,
        }

        return render(request, 'actos_administrativos/ingreso_resol.html', context)
  

# Vista para listar, actualizar y eliminar las resoluciones de condecoraciones
class ResolucionMedallaListView(LoginRequiredMixin, ListView):
    model = ResolucionMedalla
    template_name = "actos_administrativos/res-condecoracion.html"
    context_object_name = 'medalla'


class ResolucionMedallaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'actos_administrativos/res-condecoracion_update.html'
    model = ResolucionMedalla
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_res_condecoracion', args=[self.object.id])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservistas'] = ReservistaModel.objects.all() 
        context['medallas'] = ConedecoracionModel.objects.all()
        return context

class ResolucionMedallaDelete(LoginRequiredMixin, DeleteView):
    template_name = 'actos_administrativos/res-condecoracion_confirm_delete.html'
    model = ResolucionMedalla
    
    def get_success_url(self):        
        return reverse('list_res_condecoracion')
    


# Vista para listar, actualizar y eliminar las resoluciones de ascenso
class ResolucionAscensoListView(LoginRequiredMixin, ListView):
    model = ResolucionAscenso
    template_name = "actos_administrativos/res-ascenso.html"
    context_object_name = 'ascenso'
    paginate_by = 10  

class ResolucionAscensoUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'actos_administrativos/res-ascenso_update.html'
    model = ResolucionAscenso
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_res_ascenso', args=[self.object.id])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservistas'] = ReservistaModel.objects.all() 
        context['grados'] = GradoModel.objects.all()
        return context

class ResolucionAscensoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'actos_administrativos/res-ascenso_confirm_delete.html'
    model = ResolucionAscenso
    
    def get_success_url(self):        
        return reverse('list_res_ascenso')
    
# Vista para listar, actualizar y eliminar las resoluciones de cambio de escalafón
class ResolucionCambioEscalafonListView(LoginRequiredMixin, ListView):
    model = ResolucionCambioEscalafon
    template_name = "actos_administrativos/res-escalafon.html"
    context_object_name = 'escalafon'

class ResolucionCambioEscalafonUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'actos_administrativos/res-escalafon_update.html'
    model = ResolucionCambioEscalafon
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_res_escalafon', args=[self.object.id])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservistas'] = ReservistaModel.objects.all() 
        context['grados'] = GradoModel.objects.all()
        context['armas'] =ArmaServicioModel.objects.all()
        return context

class ResolucionCambioEscalafonDelete(LoginRequiredMixin, DeleteView):
    template_name = 'actos_administrativos/res-escalafon_confirm_delete.html'
    model = ResolucionCambioEscalafon
    
    def get_success_url(self):        
        return reverse('list_res_escalafon')

# Vista para listar, actualizar y eliminar las resoluciones de cambio de institución
class ResolucionCambioInstitucionListView(LoginRequiredMixin, ListView):
    model = ResolucionCambioInstitucion
    template_name = "actos_administrativos/res-institucion.html"
    context_object_name = 'institucion'


class ResolucionCambioInstitucionUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'actos_administrativos/res-institucion_update.html'
    model = ResolucionCambioInstitucion
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_res_institucion', args=[self.object.id])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservistas'] = ReservistaModel.objects.all() 
        return context

class ResolucionCambioInstitucionDelete(LoginRequiredMixin, DeleteView):
    template_name = 'actos_administrativos/res-institucion_confirm_delete.html'
    model = ResolucionCambioInstitucion
    
    def get_success_url(self):        
        return reverse('list_res_institucion')
    
# Vista para descargar documentos
class DescargarDocumentoGenericaView(LoginRequiredMixin, View):
    file_field = 'resolucion'

    def get(self, request, model, pk):
        # Obtener el modelo dinámicamente
        try:
            model_class = apps.get_model(app_label='actos_administrativos', model_name=model)
        except LookupError:
            return HttpResponseNotFound("El modelo especificado no existe.")

        # Obtener el objeto
        objeto = get_object_or_404(model_class, pk=pk)
        
        # Obtener el archivo del campo especificado
        archivo = getattr(objeto, self.file_field, None)
        if not archivo or not archivo.name:
            return HttpResponseNotFound("No se puede descargar el documento porque no se ha subido información.")

        # Devolver el archivo como respuesta
        with archivo.open('rb') as archivo_abierto:
            response = HttpResponse(archivo_abierto.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{archivo.name}"'
            return response


#-------------------------------------------------------------------------------------#
#--------------------Buscador de resoluciones de ascenso y nombramiento---------------#

# vista para mostrar resultados de búsqueda de reservistas
class SearchResAscensoView(LoginRequiredMixin, ListView):
    model = ResolucionAscenso
    template_name = "actos_administrativos/search_results_ascenso.html"
    context_object_name = 'resoluciones'
    paginate_by = 10

    def get_queryset(self):
        query= self.request.GET.get('query')       
       
        resoluciones = ResolucionAscenso.objects.all()
        if query:
            resoluciones = resoluciones.filter(
                Q(numero_resolucion__icontains=query) |
                Q(tipo_resolucion__icontains=query) 
            )
        return resoluciones
    