from django.contrib import admin
from django.urls import path
from apps.knnanalyzer.views import home,predict

urlpatterns = [
    path('home/',home, name='home'),
    path('predict/',predict, name='predict'),

]
