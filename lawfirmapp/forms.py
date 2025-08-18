from django import forms
from lawfirmapp.models import lawfirm,Enquiry,Appointment

class LawFirmForm(forms.ModelForm):
    class Meta:
        model = lawfirm
        fields = '__all__'

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    fee = forms.IntegerField(initial=500,disabled=True)
    class Meta:
        model = Appointment
        fields = '__all__'