from django import forms

from main.dictionary import exp
from main.forms import BootstrapForm

from .models import Course


class CourseForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Course
        fields = ['department', 'name', 'course_number', 'group_number', 'teacher', 'start_time', 'end_time',
                  'first_day', 'second_day']
        labels = {
            'department': exp('courses.department'),
            'name': exp('courses.name'),
            'course_number': exp('courses.course_number'),
            'group_number': exp('courses.group_number'),
            'teacher': exp('courses.teacher'),
            'start_time': exp('courses.start_time'),
            'end_time': exp('courses.end_time'),
            'first_day': exp('courses.first_day'),
            'second_day': exp('courses.second_day'),
        }

        widgets = {
            'course_number': forms.NumberInput(attrs={'class': 'force-ltr'}),
            'group_number': forms.NumberInput(attrs={'class': 'force-ltr'}),
            'start_time': forms.TimeInput(attrs={'class': 'force-ltr', 'placeholder': 'hh:mm'}, format='%H:%M'),
            'end_time': forms.TimeInput(attrs={'class': 'force-ltr', 'placeholder': 'hh:mm'}, format='%H:%M'),
        }
