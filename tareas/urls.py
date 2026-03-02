from django.urls import path
from .views import TareaListCreateView, TareaDetailView, TareaPendientesView, TareaCompletadasView, TareaMarcarCompletadaView, TareaMarcarPendienteView

urlpatterns = [
    path('', TareaListCreateView.as_view(), name='tarea-list-create'),
    path('<int:pk>/', TareaDetailView.as_view(), name='tarea-detail'),
    path('pendientes/', TareaPendientesView.as_view(), name='tarea-pendientes'),
    path('completadas/', TareaCompletadasView.as_view(), name='tarea-completadas'),
    path('<int:pk>/marcar_completada/', TareaMarcarCompletadaView.as_view(), name='tarea-marcar-completada'),
    path('<int:pk>/marcar_pendiente/', TareaMarcarPendienteView.as_view(), name='tarea-marcar-pendiente'),
]