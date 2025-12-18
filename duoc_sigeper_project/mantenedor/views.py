from django.views.generic import ListView, View
from django.views.generic.edit import UpdateView, DeleteView
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from usuarios.mixins import AdminOrDivperRequiredMixin



#-------------------------Mantenedor---------------------------#
class MantenedorView(AdminOrDivperRequiredMixin, View):
    def get(self, request):
        # Inicializa todos los formularios
        afp_form = AFPForm()
        isapre_form = ISAPREForm()
        ciudad_form = CiudadForm()
        arma_form = ArmaServicioForm()        
        estado_civil_form = EstadoCivilForm()
        grado_form = GradoForm()
        grupo_sanguineo_form = GrupoSanguineoForm()
        profesion_form = ProfesionForm()
        religion_form = ReligionForm()
        uac_form = UACForm()
        ubm_form = UBMForm()
        medalla_form = CondecoracionForm()
        categoria_form = CategoriaForm()
        unidad_form = UnidadForm()
        
        uacs = UACModel.objects.all()        

        context = {
            'afp_form' : afp_form,
            'isapre_form' : isapre_form,
            'ciudad_form' : ciudad_form,
            'arma_form': arma_form,
            'estado_civil_form': estado_civil_form,
            'grado_form': grado_form,
            'grupo_sanguineo_form': grupo_sanguineo_form,
            'profesion_form': profesion_form,
            'religion_form' : religion_form,
            'uac_form' : uac_form,
            'ubm_form': ubm_form,
            'medalla_form' : medalla_form,  
            'categoria_form': categoria_form,
            'uacs': uacs,
            'unidad_form': unidad_form,
            
        }


        return render(request, 'mantenedor/mantenedor.html', context)

      
    
    def post(self, request, *args, **kwargs):
        # Obtiene el tipo de formulario que se envió
        form_type = request.POST.get('form_type')

        # Inicializa el formulario correspondiente
        if form_type == 'afp':
            arma_form = AFPForm(request.POST)
            if arma_form.is_valid():
                arma_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=afp')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=afp')
            
            
        elif form_type == 'isapre':
            arma_form = ISAPREForm(request.POST)
            if arma_form.is_valid():
                arma_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=isapre')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=isapre')
            
        elif form_type == 'ciudad':
            arma_form = CiudadForm(request.POST)
            if arma_form.is_valid():
                arma_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=ciudad')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=ciudad')
            
        elif form_type == 'arma':
            arma_form = ArmaServicioForm(request.POST, request.FILES)
            if arma_form.is_valid():
                arma_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=arma')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=arma')

        elif form_type == 'estado_civil':
            estado_civil_form = EstadoCivilForm(request.POST)
            if estado_civil_form.is_valid():
                estado_civil_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=estado_civil')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=estado_civil')
            
        elif form_type == 'grado':
            grado_form = GradoForm(request.POST, request.FILES)
            if grado_form.is_valid():
                grado_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=grado')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=grado')
            
        elif form_type == 'grupo_sanguineo':
            grupo_sanguineo_form = GrupoSanguineoForm(request.POST)
            if grupo_sanguineo_form.is_valid():
                print(grupo_sanguineo_form.is_valid)
                grupo_sanguineo_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=grupo_sanguineo')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=grupo_sanguineo')
            
        elif form_type == 'profesion':
            unidad_form = ProfesionForm(request.POST)
            if unidad_form.is_valid():
                unidad_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=profesion')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=profesion')
            
        elif form_type == 'religion':
            unidad_form = ReligionForm(request.POST)
            if unidad_form.is_valid():
                unidad_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=religion')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=religion')
            
            
        elif form_type == 'uac':
            ubm_form = UACForm(request.POST, request.FILES)
            if ubm_form.is_valid():
                ubm_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=uac')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=uac')
            
        elif form_type == 'ubm':
            ubm_form = UBMForm(request.POST, request.FILES)
            if ubm_form.is_valid():
                ubm_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=ubm')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=ubm')
            
        elif form_type == 'medalla':
            ubm_form = CondecoracionForm(request.POST, request.FILES)
            if ubm_form.is_valid():
                ubm_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=medalla')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=medalla')

        elif form_type == 'categoria':
            categoria_form = CategoriaForm(request.POST, request.FILES)
            if categoria_form.is_valid():
                print("Formulario válido:", categoria_form.cleaned_data)
                categoria_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=categoria')
            else:
                print("Errores del formulario:", categoria_form.errors)
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=categoria')
        
        elif form_type == 'unidad':
            unidad_form = UnidadForm(request.POST, request.FILES)
            if unidad_form.is_valid():
                unidad_form.save()
                messages.success(request, 'Información agregada correctamente.')
                return redirect(f'{reverse("mantenedor")}?tab=unidad')
            else:
                messages.warning(request, 'Información no agregada')
                return redirect(f'{reverse("mantenedor")}?tab=unidad')

            
        # Si ningún formulario es válido o se envió un formulario desconocido, inicializa todos los formularios de nuevo
        afp_form = AFPForm(request.POST or None)
        isapre_form = ISAPREForm(request.POST or None) 
        ciudad_form = CiudadForm(request.POST or None)
        arma_form = ArmaServicioForm(request.POST or None)
        estado_civil_form = EstadoCivilForm(request.POST or None)
        grado_form = GradoForm(request.POST or None)
        grupo_sanguineo_form = GrupoSanguineoForm(request.POST or None)
        profesion_form = ProfesionForm(request.POST or None) 
        religion_form = ReligionForm(request.POST or None) 
        uac_form = UACForm(request.POST or None)
        ubm_form = UBMForm(request.POST or None)
        medalla_form = CondecoracionForm(request.POST or None)
        categoria_form = CategoriaForm(request.POST or None)
        unidad_form = UnidadForm(request.POST or None)
        
        uacs = UACModel.objects.all()

        # Renderizar la plantilla con los formularios
        context = {
            'afp_form' : afp_form,
            'isapre_form' : isapre_form,
            'ciudad_form' : ciudad_form,
            'arma_form': arma_form,
            'estado_civil_form': estado_civil_form,
            'grado_form': grado_form,
            'grupo_sanguineo_form': grupo_sanguineo_form,
            'profesion_form': profesion_form,
            'religion_form' : religion_form,
            'uac_form' : uac_form,
            'ubm_form': ubm_form,
            'medalla_form' : medalla_form,
            'categoria_form': categoria_form,
            'uacs': uacs,
            'unidad_form': unidad_form,
        }
        return render(request, 'mantenedor/mantenedor.html', context)





#-------------------------afp crud----------------------------#
class AFPListView(AdminOrDivperRequiredMixin, ListView):
    model = AFPModel
    template_name = "mantenedor/mantenedor-afp.html"
    context_object_name = 'afp'
    paginate_by = 10  
    
    def get_queryset(self):
        return AFPModel.objects.order_by("id", "creado")  

  

class AfpUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-afp_update.html'
    model = AFPModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_afp', args=[self.object.id])


class AfpDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-afp_confirm_delete.html'
    model = AFPModel
    
    def get_success_url(self):        
        return reverse('list_afp')


#-------------------------arma y serivicio crud ---------------#
class ArmaListView(AdminOrDivperRequiredMixin, ListView):
    model = ArmaServicioModel
    template_name = "mantenedor/mantenedor-arma.html"
    context_object_name = 'arma'
    paginate_by = 10
    
    def get_queryset(self):
        return ArmaServicioModel.objects.order_by("id", "creado")


class ArmaUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-arma_update.html'
    model = ArmaServicioModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_arma', args=[self.object.id])
    


class ArmaDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-arma_confirm_delete.html'
    model = ArmaServicioModel
    
    def get_success_url(self):        
        return reverse('list_arma')


#-------------------------ciudad crud---------------------------#
class CiudadListView(AdminOrDivperRequiredMixin, ListView):
    model = CiudadModel
    template_name = "mantenedor/mantenedor-ciudad.html"
    context_object_name = 'ciudad'
    paginate_by = 10
    
    def get_queryset(self):
        return CiudadModel.objects.order_by("id", "creado")


class CiudadUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-ciudad_update.html'
    model = CiudadModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_ciudad', args=[self.object.id])
    


class CiudadDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-ciudad_confirm_delete.html'
    model = CiudadModel
    
    def get_success_url(self):        
        return reverse('list_ciudad')
    


#-------------------------estado civil crud---------------------#
class EstadoCivilListView(AdminOrDivperRequiredMixin, ListView):
    model = EstadoCivilModel
    template_name = "mantenedor/mantenedor-estado-civil.html"
    context_object_name = 'estadoCivil'
    paginate_by = 10
    
    def get_queryset(self):
        return EstadoCivilModel.objects.order_by("id", "creado")


class EstadoCivilUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-estado_civil_update.html'
    model = EstadoCivilModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_estado_civil', args=[self.object.id])


class EstadoCivilDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-estado_civil_confirm_delete.html'
    model = EstadoCivilModel
    
    def get_success_url(self):        
        return reverse('list_estado_civil')
    


#-------------------------grado crud----------------------------#
class GradoListView(AdminOrDivperRequiredMixin, ListView):
    model = GradoModel
    template_name = "mantenedor/mantenedor-grado.html"
    context_object_name = 'grado'
    paginate_by = 10    
    
    def get_queryset(self):
        return GradoModel.objects.order_by("id", "creado")


class GradoUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-grado_update.html'
    model = GradoModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_grado', args=[self.object.id])

class GradoDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-grado_confirm_delete.html'
    model = GradoModel
    
    def get_success_url(self):        
        return reverse('list_grado')

#-------------------------grupo sanguineo crud------------------#
class GrupoSanguineoListView(AdminOrDivperRequiredMixin, ListView):
    model = GrupoSanguineoModel
    template_name = "mantenedor/mantenedor-grupo_sanguineo.html"
    context_object_name = 'grupoSanguineo'
    paginate_by = 10

    def get_queryset(self):
        return GrupoSanguineoModel.objects.order_by("id", "creado")

class GrupoSanguineoUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-grupo_sanguineo_update.html'
    model = GrupoSanguineoModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_grupo_sanguineo', args=[self.object.id])


class GrupoSanguineoDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-grupo_sanguineo_confirm_delete.html'
    model = GrupoSanguineoModel
    
    def get_success_url(self):        
        return reverse('list_grupo_sanguineo')
    

#-------------------------isapre crud---------------------------#
class ISAPREListView(AdminOrDivperRequiredMixin, ListView):
    model = ISAPREModel
    template_name = "mantenedor/mantenedor-isapre.html"
    context_object_name = 'isapre'
    paginate_by = 10
    
    def get_queryset(self):
        return ISAPREModel.objects.order_by("id", "creado")


class ISAPREUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-isapre_update.html'
    model = ISAPREModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_isapre', args=[self.object.id])
    

class ISAPREDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-isapre_confirm_delete.html'
    model = ISAPREModel
    
    def get_success_url(self):        
        return reverse('list_isapre')
    

#-------------------------profesión crud------------------------#
class ProfesionListView(AdminOrDivperRequiredMixin, ListView):
    model = ProfesionModel
    template_name = "mantenedor/mantenedor-profesion.html"
    context_object_name = 'profesion'
    paginate_by = 10
    
    def get_queryset(self):
        return ProfesionModel.objects.order_by("id", "creado")


class ProfesionUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-profesion_update.html'
    model = ProfesionModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_profesion', args=[self.object.id])
    

class ProfesionDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-profesion_confirm_delete.html'
    model = ProfesionModel
    
    def get_success_url(self):        
        return reverse('list_profesion')
    


#-------------------------Religión crud-------------------------#
class ReligionListView(AdminOrDivperRequiredMixin, ListView):
    model = ReligionModel
    template_name = "mantenedor/mantenedor-religion.html"
    context_object_name = 'religion'
    paginate_by = 10
    
    def get_queryset(self):
        return ReligionModel.objects.order_by("id", "creado")


class ReligionUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-religion_update.html'
    model = ReligionModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_religion', args=[self.object.id])


class ReligionDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-religion_confirm_delete.html'
    model = ReligionModel
    
    def get_success_url(self):        
        return reverse('list_religion')
    


#-------------------------uac crud------------------------------#
class UACListView(AdminOrDivperRequiredMixin, ListView):
    model = UACModel
    template_name = "mantenedor/mantenedor-uac.html"
    context_object_name = 'uac'
    paginate_by = 10
    
    def get_queryset(self):
        return UACModel.objects.order_by("id", "creado")


class UACUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-uac_update.html'
    model = UACModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_uac', args=[self.object.id])
    


class UACDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-uac_confirm_delete.html'
    model = UACModel
    
    def get_success_url(self):        
        return reverse('list_uac')


#-------------------------ubm crud------------------------------#
class UBMListView(AdminOrDivperRequiredMixin, ListView):
    model = UBMModel
    template_name = "mantenedor/mantenedor-ubm.html"
    context_object_name = 'ubm'
    paginate_by = 10
    
    def get_queryset(self):
        return UBMModel.objects.order_by("id", "creado")


class UBMUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-ubm_update.html'
    model = UBMModel
    fields = '__all__'
    
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_ubm', args=[self.object.id])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #contexto uacs
        context['uacs'] = UACModel.objects.all()
        return context

class UBMDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-ubm_confirm_delete.html'
    model = UBMModel
    
    def get_success_url(self):        
        return reverse('list_ubm')   


#-------------------------medalla crud--------------------------#
class MedallaListView(AdminOrDivperRequiredMixin, ListView):
    model = ConedecoracionModel
    template_name = "mantenedor/mantenedor-medalla.html"
    context_object_name = 'medalla'
    paginate_by = 10
    
    def get_queryset(self):
        return ConedecoracionModel.objects.order_by("id", "creado")


class MedallaUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-medalla_update.html'
    model = ConedecoracionModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_medalla', args=[self.object.id])

class MedallaDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-medalla_confirm_delete.html'
    model = ConedecoracionModel
    
    def get_success_url(self):        
        return reverse('list_medalla')
    

#-------------------------categoria crud------------------------#
class CategoriaListView(AdminOrDivperRequiredMixin, ListView):
    model = categoriaModel
    template_name = "mantenedor/mantenedor-categoria.html"
    context_object_name = 'categoria'
    paginate_by = 10
    
    def get_queryset(self):
        return categoriaModel.objects.order_by("id", "creado")


class CategoriaUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-categoria_update.html'
    model = categoriaModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_categoria', args=[self.object.id])
    


class CategoriaDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-categoria_confirm_delete.html'
    model = categoriaModel
    
    def get_success_url(self):        
        return reverse('list_categoria')


#-------------------------unidad crud------------------------#
class UnidadListView(AdminOrDivperRequiredMixin, ListView):
    model = UnidadModel
    template_name = "mantenedor/mantenedor-unidad.html"
    context_object_name = 'unidad'
    paginate_by = 10
    
    def get_queryset(self):
        return UnidadModel.objects.order_by("id", "creado")


class UnidadUpdate(AdminOrDivperRequiredMixin, UpdateView):
    template_name = 'mantenedor/mantenedor-unidad_update.html'
    model = UnidadModel
    fields = '__all__'
    
    def form_valid(self, form):
        # Mensaje de éxito al actualizar correctamente
        messages.success(self.request, 'Actualización realizada correctamente.')
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('update_unidad', args=[self.object.id])
    


class UnidadDelete(AdminOrDivperRequiredMixin, DeleteView):
    template_name = 'mantenedor/mantenedor-unidad_confirm_delete.html'
    model = UnidadModel
    
    def get_success_url(self):        
        return reverse('list_unidad')
