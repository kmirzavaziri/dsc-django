from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.decorators.http import require_http_methods

from users.decorators import superuser_required
from users.mixins import SuperUserRequiredMixin
from .forms import CourseForm
from .models import Course


class CourseListView(LoginRequiredMixin, generic.ListView):
    model = Course
    template_name = 'courses/list.html'


class CreateCourseView(SuperUserRequiredMixin, generic.CreateView):
    template_name = 'courses/detail.html'
    form_class = CourseForm

    def get_success_url(self):
        return reverse('courses:detail', kwargs={'pk': self.object.id})


class UpdateCourseView(SuperUserRequiredMixin, generic.UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/detail.html'
    success_url = reverse_lazy('courses:list')


@superuser_required
@require_http_methods(["POST"])
def delete_course_view(request, pk):
    Course.objects.filter(pk=pk).delete()
    return redirect(reverse('courses:list'))