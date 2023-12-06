from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task



class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'tasks/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task-list')
        return render(request, 'tasks/signup.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'tasks/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task-list')
        return render(request, 'tasks/login.html', {'form': form})
    
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'

class HomeView(View):
    def get(self, request):
        return render(request, 'tasks/home.html')  

class SignUpView(View):
    def get(self, request):
        return render(request, 'tasks/signup.html')  

class LoginView(View):
    def get(self, request):
        return render(request, 'tasks/login.html')  

class HelpView(View):
    def get(self, request):
        return render(request, 'tasks/help.html')  

class AboutView(View):
    def get(self, request):
        return render(request, 'tasks/about.html')  

class ContactUsView(View):
    def get(self, request):
        return render(request, 'tasks/contact_us.html') 
    
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'due_date', 'priority', 'completed']

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'due_date', 'priority', 'completed']

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
