from django.contrib import admin
from django.urls import path
from myapps import views

app_name="myapps"
urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('fact/<n>',views.fact,name='fact'),
    path('child/',views.child,name='child'),
]