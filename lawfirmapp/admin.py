from django.contrib import admin
from lawfirmapp.models import lawfirm,AllCases,Enquiry,Appointment

# Register your models here.

admin.site.register(lawfirm)
admin.site.register(AllCases)
admin.site.register(Enquiry)
admin.site.register(Appointment)
