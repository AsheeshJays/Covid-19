from django.contrib import admin
from django.urls import path
from Covid19 import views

urlpatterns = [
    path('', views.index),
    path('worldcorona/',views.worldco, name='worldcorona'),
    path('indiacorona/',views.indiaco, name='indiacorona'),
    path('indiadaywise/',views.daywise, name='indiadatwise'),
]
