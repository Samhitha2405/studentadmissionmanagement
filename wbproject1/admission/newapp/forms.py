# forms.py

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs['min'] = '1980-01-01'
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'aadhar_number', 'memo', 'photo',
                  'email', 'mother_name', 'father_name', 'student_phone_number', 'parent_phone_number', 'assign_id_number']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }