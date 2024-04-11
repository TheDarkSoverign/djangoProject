from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, FormView

from .models import Post
from .forms import RegisterUserForm, LoginUserForm


class BlogList(ListView):
    paginate_by = 3
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reg_form'] = RegisterUserForm()
        context['login_form'] = LoginUserForm()
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class RegisterUserView(FormView):
    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']

            # Создаем пользователя
            user = User.objects.create_user(username=username, email=email, password=password)

            # Авторизуем пользователя
            user = authenticate(username=username, password=password)
            login(request, user)

            # Перенаправляем пользователя на нужную страницу
            return redirect('home')
        return render(request, 'register.html', {'form': form})


class LoginUser(View):
    def get(self, request):
        form1 = LoginUserForm()
        return render(request, 'login.html', {'form': form1})

    def post(self, request):
        form1 = LoginUserForm(data=request.POST)
        if form1.is_valid():
            user = form1.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'form': form1})

def logout_user(request):
    logout(request)
    return redirect('home')
