from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("signup/", Signup.as_view(), name="signup"),
    path("signin/", Signin.as_view(), name="signin"),
    path("logout/", views.signout, name="signout"),
    path("profile/", Perfil.as_view(), name="profile"),
    path("profile/create_project/", CreateProject.as_view(), name="create_project"),
    path("profile/<int:project_id>/", ProjectDetail.as_view(), name="projects_detail"),
    
]
