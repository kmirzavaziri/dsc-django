from django import forms


class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if 'class' not in visible.field.widget.attrs:
                visible.field.widget.attrs['class'] = ''
            visible.field.widget.attrs['class'] += ' form-control'
