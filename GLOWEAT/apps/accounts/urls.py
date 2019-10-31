from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.indexView, name="home2"),
    path('dashboard/', views.dashboardView, name="dashboard_url"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='dashboard_url'), name="logout_url"),
    
]