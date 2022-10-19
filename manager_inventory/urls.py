from django.urls import path
from django.views.generic import RedirectView

from manager_inventory import controllers, views

urlpatterns = [
    path('', RedirectView.as_view(url='/index/')),
    path('index/', views.index),
    path('home/', views.home),
    # CONTROLLERS
    path('validar_login/', controllers.validarLogin, name='validar_login'),
]
