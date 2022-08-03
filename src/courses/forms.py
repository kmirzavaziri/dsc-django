from django import forms

from main.dictionary import exp
from main.forms import BootstrapForm

from .models import Course


class CourseForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Course
        fields = ['department', 'name', 'course_number', 'group_number', 'teacher', 'start_time', 'end_time',
                  'first_day', 'second_day']

        widgets = {
            'course_number': forms.NumberInput(attrs={'class': 'force-ltr'}),
            'group_number': forms.NumberInput(attrs={'class': 'force-ltr'}),
            'start_time': forms.TimeInput(attrs={'class': 'force-ltr', 'placeholder': 'hh:mm'}, format='%H:%M'),
            'end_time': forms.TimeInput(attrs={'class': 'force-ltr', 'placeholder': 'hh:mm'}, format='%H:%M'),
        }
