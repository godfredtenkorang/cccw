from django import forms
from .models import Payment, Contact


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ("amount", "name", "phone", "email")
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "phone", "message")
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }