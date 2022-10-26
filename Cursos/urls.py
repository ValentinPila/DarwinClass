from django.urls import path 

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('curso/', CursosPageView.as_view(), name='curso'),
    path('curso/<int:pk>/', CursosPageDetail.as_view(), name='curso_detalle'),
    path('curso/nuevo/', CursosPageCreate.as_view(), name='curso_nuevo'),
    path('curso/<int:pk>/Editar', CursosPageUpdate.as_view(), name='curso_editar'),
    path('curso/<int:pk>/delete', CursosPageDelete.as_view(), name='curso_delete'),
    path('curso/<int:pk>/comentarios/nuevo/', ComentariosPageCreate.as_view(), name='comentarios_nuevo'),
    path('curso/<int:pk>/comentarios/delete/', ComentariosPageDelete.as_view(), name='comentarios_delete'),
]
