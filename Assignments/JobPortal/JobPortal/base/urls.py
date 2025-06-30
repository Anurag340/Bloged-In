from django.urls import path
from .views import (
    JobListView, JobDetailView,
    JobCreateView, JobUpdateView, JobDeleteView
)

urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('job/add/', JobCreateView.as_view(), name='job-add'),
    path('job/<int:pk>/edit/', JobUpdateView.as_view(), name='job-edit'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
]
