from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from mantenedor.models import *
from reservistas.models import ReservistaModel
from actos_administrativos.models import ResolucionMedalla, ResolucionAscenso





# Página index
class IndexTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'core/index.html'
    
    def get_context_data(self, **kwargs):
        total_reservistas = ReservistaModel.objects.count()
        total_resoluciones_medalla = ResolucionMedalla.objects.count()
        total_resoluciones_ascenso = ResolucionAscenso.objects.count()
        total_reservistas_masculino = ReservistaModel.objects.filter(genero='Masculino').count()
        total_reservistas_femenino = ReservistaModel.objects.filter(genero='Femenino').count() 
        
        
        
        #Gráfico de barra por grados
        orden_grados =['TCL (RVA)', 'MAY (RVA)', 'CAP (RVA)', 'TTE (RVA)', 'STE (RVA)', 'ALF (RVA)',
                       'SOM (RVA)', 'SOF (RVA)', 'SG1 (RVA)', 'SG2 (RVA)', 'CB1 (RVA)', 'CB2 (RVA)', 'CBO (RVA)',
                       'AOR', 'ASR', 'RVTA']        
        grados_filtrados = (ReservistaModel.objects
                            .filter(grado__grado_sigla__in=orden_grados)
                            .values('grado__grado_sigla')
                            .annotate(total=Count('id'))  
                            .order_by('grado__id')
                            )
        grados = [item['grado__grado_sigla'] for item in grados_filtrados]
        cantidades = [item['total'] for item in grados_filtrados]
        
        #Gráfico de barra por arma
        armas = ReservistaModel.objects.values('arma__sigla_arma').annotate(total=Count('id'))
        arma_labels = [arma['arma__sigla_arma'] for arma in armas] if armas else []
        arma_counts = [arma['total'] for arma in armas] if armas else []
        
        #Grafico de circular por categoria
        categorias = ReservistaModel.objects.values('categoria__nombre').annotate(total=Count('id'))
        categorias_labels = [categoria['categoria__nombre'] for categoria in categorias]
        categorias_counts = [categoria['total'] for categoria in categorias]
        
        #Grafico de barra por UAC
        uacs = ReservistaModel.objects.values('uac__uac_sigla').annotate(total=Count('id'))
        uacs_labels = [uac['uac__uac_sigla'] for uac in uacs]
        uacs_counts = [uac['total'] for uac in uacs]

        context = super().get_context_data(**kwargs)
        context.update({
            'total_reservistas': total_reservistas,
            'total_resoluciones_medalla': total_resoluciones_medalla,
            'total_resoluciones_ascenso': total_resoluciones_ascenso, 
            'total_reservistas_masculino': total_reservistas_masculino,
            'total_reservistas_femenino': total_reservistas_femenino, 
            'grados': grados,
            'cantidades': cantidades,
            'categorias_labels': categorias_labels,
            'categorias_counts': categorias_counts,
            'arma_labels': arma_labels,
            'arma_counts':arma_counts,
            'uacs_labels':uacs_labels,
            'uacs_counts':uacs_counts,
            
            
        })
        return context


class FaqTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'core/faq.html'
    
class ContactTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'core/pages-contact.html'

class Error404Views(TemplateView):
    template_name = 'core/error-404.html'