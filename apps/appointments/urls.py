from .views import AppointmentListView, AppointmentDetailView
from django.urls import path

urlpatterns = [
    path('appointments/', AppointmentListView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'), 
]