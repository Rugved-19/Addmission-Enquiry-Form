from django import forms
from .models import Administrator

HANDLED_BY_CHOICES = [
    ('Ashwini man', 'Ashwini Mam'),
    ('Sachin sir', 'Sachin Sir'),
    ('Vinayashree mam', 'Vinayashree Mam '),
    ('Counsellor', 'Counsellor'),
]

Course_Name=[
    ('Module 1', 'Module 1'),
    ('Module 2', 'Module 2'),
    ('Module 3', 'Module 3'),
    ('Module 4', 'Module 4'),
    ('Module 5', 'Module 5'),

]

class AdmissionEnquiryForm(forms.ModelForm):
    enquiry_handled_by = forms.ChoiceField(
    choices=HANDLED_BY_CHOICES,
    widget=forms.Select(attrs={'class': 'form-control'})
    )

    course_name= forms.ChoiceField(
    choices=Course_Name,
    widget=forms.Select(attrs={'class': 'form-control'})    
    )

    excel_file_path = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Excel path only if changing location"
        })
    )


    class Meta:
        model = Administrator
        fields = '__all__'
        widgets = {
            'enquiry_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                },
                format='%Y-%m-%d'
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')