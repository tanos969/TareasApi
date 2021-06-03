from django.conf.urls import url
from Tareas import views

urlpatterns = [
    url(r'^api/tarea$', views.tarea_list),
    url(r'^api/tarea/(?P<pk>[0-9]+)/completar$', views.completar_tarea),
    url(r'^api/tarea/(?P<pk>[0-9]+)$', views.tarea_detail),
]
