from django import forms
from .models import Student

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

DEPARTMENT_CHOICES = [
    ('IT', 'IT'),
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('MECH', 'MECH'),
    ('AI', 'AI'),
]

YEAR_CHOICES = [
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
]

STATE_CHOICES = [
    ('AP', 'Andhra Pradesh'),
    ('TS', 'Telangana'),
    ('KA', 'Karnataka'),
    ('TN', 'Tamil Nadu'),
]

SKILLS_CHOICES = [
    ('python', 'Python'),
    ('java', 'Java'),
    ('c', 'C'),
    ('django', 'Django'),
    ('sql', 'SQL'),
]


MODE_CHOICES = [
    ('Online', 'Online'),
    ('Offline', 'Offline'),
    ('Hybrid', 'Hybrid'),
]


class StudentForm(forms.ModelForm):

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select
    )

    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        widget=forms.Select
    )

    year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select
    )

    state = forms.ChoiceField(
        choices=STATE_CHOICES,
        widget=forms.Select
    )

    skills = forms.MultipleChoiceField(
        choices=SKILLS_CHOICES,
        widget=forms.CheckboxSelectMultiple,  
        
        label='Skills'
    )

    learning_mode = forms.ChoiceField(
        choices=MODE_CHOICES,
        widget=forms.Select
    )

    agree = forms.BooleanField()

    dob = forms.DateField(
    widget=forms.DateInput(attrs={'type': 'date'})
)

    class Meta:
        model = Student
        fields = '__all__'
