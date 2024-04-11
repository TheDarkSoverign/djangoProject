from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
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
        context['form'] = RegisterUserForm()
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class RegisterUserView(FormView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)  # Возвращаем JSON-ответ о успешной регистрации

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    success_url = ''

    def get(self, request):
        form = LoginUserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def logout_user(request):
    logout(request)
    return redirect('home')
