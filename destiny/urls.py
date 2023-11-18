from django.urls import path
from . import views

app_name ='destiny'

urlpatterns =[
     path('', views.index, name='home'),
path('main/', views.main, name='main'),
#path('book/', views.book, name='book'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('destination_details/',views.destinationDetails,name='destination_details'),
    path('contact/',views.contact,name='contact'),
    path('elements/',views.elements,name='elements'),
    path('index/',views.index,name='index'),
    path('single-blog/',views.single_blog,name='singleBlog'),
    path('travel-destinations/',views.travelDestinations,name='travelDestinations'),
    path('flight/',views.flight,name='flight'),
    path('nissan/',views.nissan,name='nissan'),
    path('bus/',views.bus,name='bus'),
    path('plan/',views.plan,name='plan'),
    path('private/',views.private,name='private'),
    path('form/',views.form,name='form'),
    path('fligthlist/',views.flight_list,name='flight_list'),
    path('popular/',views.popularContent,name='popularContent'),
    path('booking/',views.Booking,name='Booking')

]