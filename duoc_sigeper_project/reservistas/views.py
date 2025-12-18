from django.shortcuts import HttpResponse, get_object_or_404
from .models import ReservistaModel
from mantenedor.models import *
from actos_administrativos.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from openpyxl import Workbook
from django.db.models import Q, Value, CharField
from django.db.models.functions import Concat, Cast


# Vista para mostrar la lista de reservistas
class ReservistaListView(LoginRequiredMixin, ListView):
    model = ReservistaModel
    template_name = "reservistas/list_reservista.html"
    context_object_name = 'reservista'
    paginate_by = 10


#vista para eliminar al reservista
class ProfileReservistaDelete(LoginRequiredMixin, DeleteView):
    template_name = 'reservistas/profile-reservista_confirm_delete.html'
    model = ReservistaModel
    
    def get_success_url(self):        
        return reverse('list_reservista')


#vista para actualizar el reservista
class ProfileReservistaUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'reservistas/profile-reservista_update.html'
    model = ReservistaModel
    fields = '__all__'
    
    
    def form_valid(self, form):
        # Manejo explícito de archivos subidos
        if 'foto' in self.request.FILES:
            form.instance.imagen = self.request.FILES['foto']
        messages.success(self.request, "Reservista actualizado exitosamente!", extra_tags="success")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario tiene errores
        messages.error(self.request, "Hubo un error al guardar. Por favor, verifica los campos.", extra_tags="danger")
        return super().form_invalid(form)
    
    def get_success_url(self):   
        return reverse_lazy('profile_reservista', args=[self.object.id])
        
           
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Asegúrate de pasar los datos necesarios a la plantilla
        context['ciudades'] = CiudadModel.objects.all()
        context['isapres'] = ISAPREModel.objects.all()
        context['afps'] = AFPModel.objects.all()
        context['armas'] = ArmaServicioModel.objects.all()
        context['estados_civiles'] = EstadoCivilModel.objects.all()
        context['grupos_sanguineos'] = GrupoSanguineoModel.objects.all()        
        context['grados'] = GradoModel.objects.all()
        context['ubms'] = UBMModel.objects.all()
        context['religiones'] = ReligionModel.objects.all()
        context['profesiones'] = ProfesionModel.objects.all()
        context['uacs'] = UACModel.objects.all()
        context['categorias'] = categoriaModel.objects.all()        
        return context


#vista para crear un reservista
class ProfileReservistaCreate(LoginRequiredMixin, CreateView):
    template_name = 'reservistas/profile-reservista_create.html'
    model = ReservistaModel
    fields = '__all__'
    success_url = reverse_lazy('profile_reservista-create') 

    def form_valid(self, form):
        # Si el formulario es válido
        messages.success(self.request, "Reservista guardada exitosamente!", extra_tags="success")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario tiene errores
        messages.error(self.request, "Hubo un error al guardar. Por favor, verifica los campos.", extra_tags="danger")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Asegúrate de pasar los datos necesarios a la plantilla
        context['ciudades'] = CiudadModel.objects.all()
        context['isapres'] = ISAPREModel.objects.all()
        context['afps'] = AFPModel.objects.all()
        context['armas'] = ArmaServicioModel.objects.all()
        context['estados_civiles'] = EstadoCivilModel.objects.all()
        context['grupos_sanguineos'] = GrupoSanguineoModel.objects.all()        
        context['grados'] = GradoModel.objects.all()
        context['ubms'] = UBMModel.objects.all()
        context['religiones'] = ReligionModel.objects.all()
        context['profesiones'] = ProfesionModel.objects.all()
        context['uacs'] = UACModel.objects.all()
        context['categorias'] = categoriaModel.objects.all()        
        return context


# Vista para mostrar el perfil de un reservista
class ProfileReservistaView(LoginRequiredMixin, TemplateView):
    template_name = "reservistas/profile-reservista.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        reservista = get_object_or_404(ReservistaModel, pk=pk)
        medallas = ResolucionMedalla.objects.filter(id_reservista=reservista)
        ascensos = ResolucionAscenso.objects.filter(id_reservista=reservista)
        escalafones = ResolucionCambioEscalafon.objects.filter(id_reservista=reservista)
        instituciones = ResolucionCambioInstitucion.objects.filter(id_reservista=reservista)
        
        context = super().get_context_data(**kwargs)
        context.update({
            'reservista': reservista,
            'medallas': medallas,
            'ascensos': ascensos,
            'escalafones': escalafones,
            'instituciones': instituciones,
        })
        return context



#vista para descargar archivos en excel
class ExportReservistasExcelView(View):
    def get(self, request, *args, **kwargs):
        # Crear un nuevo libro de trabajo de Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "Base_Datos_Reservistas"

        # Escribir encabezados
        headers = [
            "ID", "Nombre", "Apellido Paterno", "Apellido Materno",
            "RUN", "DV", "Fecha de Nacimiento", "Género",
            "Grado", "Ciudad", "ISAPRE", "AFP", "Estado Civil",
            "Grupo Sanguíneo", "Religión", "Arma", "Profesión",
            "UBM", "UAC", "Categoría", "Estado"
        ]
        ws.append(headers)

        # Escribir los datos de los reservistas
        for reservista in ReservistaModel.objects.all():
            ws.append([
                reservista.id, reservista.nombre, reservista.apellido_paterno,
                reservista.apellido_materno, reservista.run, reservista.dv,
                reservista.fecha_nacimiento, reservista.genero,
                reservista.grado.grado if reservista.grado else "",
                reservista.ciudad.nombre if reservista.ciudad else "",
                reservista.isapre.nombre if reservista.isapre else "",
                reservista.afp.nombre if reservista.afp else "",
                reservista.estado_civil.nombre if reservista.estado_civil else "",
                reservista.grupo_sanguineo.nombre if reservista.grupo_sanguineo else "",
                reservista.religion.nombre if reservista.religion else "",
                reservista.arma.nombre if reservista.arma else "",
                reservista.profesion.nombre if reservista.profesion else "",
                reservista.ubm.nombre if reservista.ubm else "",
                reservista.uac.nombre if reservista.uac else "",
                reservista.categoria.nombre if reservista.categoria else "",
                reservista.estado
            ])

        # Configurar la respuesta HTTP para descargar el archivo
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="Reservistas.xlsx"'
        wb.save(response)
        return response


# vista para mostrar resultados de búsqueda de reservistas
class SearchReservistaView(LoginRequiredMixin, ListView):
    model = ReservistaModel
    template_name = "reservistas/search_results.html"
    context_object_name = 'reservistas'
    paginate_by = 10

    def get_queryset(self):
        query= self.request.GET.get('query')
        
        reservistas = ReservistaModel.objects.annotate(
            run_completo = Concat(Cast('run', CharField()), Value('-'), 'dv'),
            nombre_completo = Concat('nombre', Value(' '), 'apellido_paterno', Value(' '), 'apellido_materno'),
            apellido_completo = Concat('apellido_paterno', Value(' '), 'apellido_materno', Value(' '), 'nombre')
        )
        
        if query:
            reservistas = reservistas.filter(
                Q(run_completo__icontains=query) |
                Q(nombre__icontains=query) |
                Q(apellido_paterno__icontains=query) |
                Q(apellido_materno__icontains=query) |
                Q(nombre_completo__icontains=query) |
                Q(apellido_completo__icontains=query) | 
                Q(run__icontains=query)
            ).distinct()
        
        return reservistas
    