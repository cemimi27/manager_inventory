from django.urls import path
from django.views.generic import RedirectView

from manager_inventory import controllers, views

app_name = 'manager_inventory'

urlpatterns = [
    path('', RedirectView.as_view(url='/index/')),
    path('index/', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('estoque/', views.estoque, name="estoque"),
    path('categoria/', views.categoria, name="categoria"),
    # CONTROLLERS
    path('validar_login/', controllers.validarLogin, name='validar_login'),
]
