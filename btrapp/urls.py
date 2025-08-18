from django.urls import path
from btrapp import views

urlpatterns = [
    path('',views.register,name='registration'),
    path('login',views.user_login,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.user_logout,name='logout'),
    path('userProfile',views.profile,name='userProfile'),
    path('update',views.update,name='update')

]