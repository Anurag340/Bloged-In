from django.urls import path
from .views import (
    PatientListView, PatientDetailView,
    PatientCreateView, PatientUpdateView, PatientDeleteView
)

urlpatterns = [
    path('', PatientListView.as_view(), name='patient-list'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patient/add/', PatientCreateView.as_view(), name='patient-add'),
    path('patient/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient-edit'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),
]
