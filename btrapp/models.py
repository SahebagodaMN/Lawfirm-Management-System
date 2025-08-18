from django.db import models
from django.contrib.auth.models import User
from lawfirmapp.models import Appointment,lawfirm,Enquiry

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional fiels
    phone = models.BigIntegerField()
    address = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    profile_pic = models.ImageField(upload_to='userImg/',blank=True,null=True)

    def __str__(self):
        return self.city


class CaseManagement(models.Model):
    case_id = models.BigIntegerField()
    case_type = models.ForeignKey(Appointment,related_name="appointemts",on_delete=models.CASCADE)
    # case_desc = models.ForeignKey(Appointment,related_name="appointemts",on_delete=models.CASCADE)
    lawyer = models.ForeignKey(lawfirm,related_name="lawfirm",on_delete=models.CASCADE)
    court = models.ForeignKey(Enquiry,related_name="enqueries",on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.case_type)


    
