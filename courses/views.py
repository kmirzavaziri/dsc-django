from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import CourseForm
from .models import Course


class CourseListView(generic.ListView):
    model = Course
    template_name = 'courses/list.html'


class CreateCourseView(generic.CreateView):
    template_name = 'courses/detail.html'
    form_class = CourseForm

    def get_success_url(self):
        return reverse('courses:detail', kwargs={'pk': self.object.id})


class UpdateCourseView(generic.UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/detail.html'
