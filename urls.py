from django.urls import path
from . import views

urlpatterns = [
     path('', views.homepage, name='homepage'),
     path('patient_data_form/', views.patient_data_form, name='patient_data_form'),
     path('customer_details/', views.customer_details_form, name='customer_details'),
     ]