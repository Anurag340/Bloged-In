from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course
from .forms import CourseForm

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course-list')
