from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Curso, Comentarios
from django.http import HttpResponseNotFound

class HomePageView(TemplateView):
    template_name = 'home.html'

class CursosPageView(ListView):
    template_name = 'cursos.html'
    model = Curso
    context_object_name = 'Todos_Los_Cursos'

class CursosPageDetail(DetailView):
    template_name = 'cursos_detalle.html'
    model = Curso
    context_object_name = 'Curso_Completo'

class CursosPageCreate(CreateView):
    template_name = 'cursos_nuevo.html'
    model = Curso
    fields = "__all__"

class CursosPageUpdate(UpdateView):
    template_name = 'cursos_editar.html'
    model = Curso
    fields = "__all__"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Creador != self.request.user:
            return HttpResponseNotFound('<h1>Pagina no encontrada</h1>')
        else:
            return super().dispatch(request, *args, **kwargs)

class CursosPageDelete(DeleteView):
    model = Curso
    success_url = '/'
    template_name = 'cursos_delete.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.Creador != self.request.user:
            return HttpResponseNotFound('<h1>Pagina no encontrada</h1>')
        else:
            return super().dispatch(request, *args, **kwargs)

class ComentariosPageCreate(CreateView):
    template_name = 'comentarios_nuevo.html'
    model = Comentarios
    fields = "__all__"

class ComentariosPageDelete(DeleteView):
    model = Curso
    success_url = '/'
    template_name = 'comentarios_delete.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseNotFound('<h1>Pagina no encontrada</h1>')
# Create your views here.
