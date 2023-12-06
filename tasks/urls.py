from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, HomeView, SignUpView, LoginView, HelpView, AboutView, ContactUsView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('home/', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('help/', HelpView.as_view(), name='help'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]

