from django.urls import path 
from . import views 
from django.urls import path, re_path
from .views import ViewsToBeImported
urlpatterns = [
    path('',views.index, name='index'),
    #customer
    path('c/login', views.login_view, name='login'),
    path('c/register', views.register_view, name='register'),
    path('c/dashboard', views.dashboard_view, name='dashboard'),
    #seller
    path('s/login', views.slogan_view, name='seller_login'),
    path('s/register', views.sregister_view, name='seller_register'),
    path('s/dashboard', views.sdashboard_view, name='selller_dashboard'),
    #logout
    path('logout', views.logout_view, name='logout'),





    
]
    
    
