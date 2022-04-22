from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path("register",register_admin,name="RegisterAdmin"),
    path("login",mylogin,name="Login"),
    path("logout",mylogout,name="Logout"),
]