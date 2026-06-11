from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, View
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DocumentoPDF

# 📄 1. Repositorio Central de Documentos Activos
class DocumentoListView(LoginRequiredMixin, ListView):
    model = DocumentoPDF
    template_name = 'documentos/documento_list.html'
    context_object_name = 'documentos'

    def get_queryset(self):
        user = self.request.user
        
        # 👑 REGLA 1: El CEO tiene visión holística absoluta de los documentos activos
        if user.is_superuser:
            return DocumentoPDF.objects.filter(is_archivado=False).order_by('-fecha_creacion')
            
        # 👥 REGLA 2: Empleado común filtrado por su Área + Pasarela de Comunicación Oblicua
        if hasattr(user, 'area') and user.area:
            return DocumentoPDF.objects.filter(
                Q(formulario__area_propietaria=user.area) | 
                Q(formulario__areas_destinatarias=user.area),
                is_archivado=False
            ).distinct().order_by('-fecha_creacion')
            
        # Si el usuario no tiene área asignada ni es superuser, no ve nada por seguridad
        return DocumentoPDF.objects.none()

# 📦 2. Repositorio de Documentos Archivados (Pileta de Recuperación)
class DocumentoArchivadoListView(LoginRequiredMixin, ListView):
    model = DocumentoPDF
    template_name = 'documentos/documentos_archivados.html'
    context_object_name = 'documentos_archivados'

    def get_queryset(self):
        user = self.request.user
        # Mismos privilegios de visibilidad pero sobre los elementos ocultos
        if user.is_superuser:
            return DocumentoPDF.objects.filter(is_archivado=True).order_by('-fecha_creacion')
            
        if hasattr(user, 'area') and user.area:
            return DocumentoPDF.objects.filter(
                Q(formulario__area_propietaria=user.area) | 
                Q(formulario__areas_destinatarias=user.area),
                is_archivado=True
            ).distinct().order_by('-fecha_creacion')
            
        return DocumentoPDF.objects.none()

# 🔒 3. Acción de Archivado Lógico (Bypass de Delete)
class ArchivarDocumentoView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        documento = get_object_or_404(DocumentoPDF, pk=pk)
        documento.archivar()
        messages.warning(request, f"El documento '{documento.nombre}' fue retirado del repositorio general y enviado al archivo.")
        return redirect('documentos:lista')

# ♻️ 4. Acción de Recuperación de Archivos
class RecuperarDocumentoView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        documento = get_object_or_404(DocumentoPDF, pk=pk)
        documento.recuperar()
        messages.success(request, f"El documento '{documento.nombre}' fue restaurado con éxito en el repositorio activo.")
        return redirect('documentos:archivados')
