from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView, FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.

class Home(View):
    template = 'index.html'
    def get(self, request):
        projects = Project.objects.order_by('-created')
        return render(request, self.template, {'projects' : projects})

class Signup(View):
    template = 'signup.html'
    form = SignUpForm

    def get(self, request):
        return render(request, self.template, {"form": self.form})
    
    def post(self, request):
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"], email=request.POST["email"])
                user.save()
                login(request, user)
                return redirect('profile')
            except IntegrityError:
                return render(request, self.template, {"form": self.form, "error": "El usuario ya existe."})
        else:
            return render(request, self.template, {"form": self.form, "error": "Contraseñas no coinciden"})

class Signin(View):
    template = 'signin.html'
    form = SignInForm

    def get(self, request):
        return render(request, self.template, {"form": self.form})
    
    def post(self, request):
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": self.form, "error": "Usuario o contraseña incorrectos!!!"})

        login(request, user)
        return redirect('profile')

class Perfil(View):
    template = 'profile.html'
    def get(self, request):
        projects = Project.objects.filter(user = request.user).order_by('-created')
        return render(request, self.template,  {'projects' : projects})


def signout(request):
    logout(request)
    return redirect('home')

class CreateProject(View):
    model = Project
    template = 'create_project.html'
    form = ProjectForm

    def get(self, request):
        return render(request, self.template, {"form": self.form})
    
    def post(self, request):
        try:
            form = self.form(request.POST)
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('profile')
        except ValueError:
            return render(request, self.template, {"form": self.form, "error": "Error al crear proyecto."})

class ProjectDetail(View):
    model = Project
    template = 'create_project.html'
    form = ProjectForm

    def get(self, request, project_id):
        project = get_object_or_404(self.model, pk=project_id, user=request.user)
        form = self.form(instance=project)
        return render(request, self.template, {'project': project, 'form': form})
    
    def post(self, request, project_id):
        try: 
            project = get_object_or_404(self.model, pk=project_id, user=request.user)
            form = self.form(request.POST, instance=project)
            form.save()
            return redirect('perfil')
        except ValueError:
            return render(request, self.template, {'project': project, 'form': form, 'error': 'Error updating task.'})



