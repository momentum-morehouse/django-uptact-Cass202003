from django import forms
from .models import Contact
import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]

        widgets = {
            'birthday': forms.DateInput(format=
            ('%m/%d/%y'), attrs=
            {'class':'form-control',
            'placeholder':'Select a date',
            'type':'date'})
            
        }
    