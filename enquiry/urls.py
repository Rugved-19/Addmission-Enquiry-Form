from django.urls import path
from . import views

urlpatterns = [
    path('', views.enquiry_form, name='enquiry_form'),
    path('list/', views.enquiry_list, name='enquiry_list'),
    path('delete/<int:id>/', views.delete_enquiry, name='delete_enquiry'),
]