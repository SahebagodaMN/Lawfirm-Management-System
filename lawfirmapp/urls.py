from django.urls import path
from lawfirmapp import views

urlpatterns = [
    path('',views.home,name='index'),
    path('profile',views.profile,name='profile'),
    path('about',views.about,name='about'),
    path('allCases',views.allCases,name='allCases'),
    path('enquery',views.enquery,name='enquery'),
    path('appointment',views.appointment,name='appointment'),

]