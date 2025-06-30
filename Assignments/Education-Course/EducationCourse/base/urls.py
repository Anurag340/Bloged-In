from django.urls import path
from .views import (
    CourseListView, CourseDetailView,
    CourseCreateView, CourseUpdateView, CourseDeleteView
)

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('course/add/', CourseCreateView.as_view(), name='course-add'),
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course-edit'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
]
