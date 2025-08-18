from django.db import models

# Create your models here.

case_types=[
    ('criminal case','CRIMINAL CASE'),
    ('civil case','CIVIL CASE'),
    ('labour case','LABOUR CASE'),
    ('tax case','TAX CASE'),
    ('other','OTHER')

]

court_names=[
    ('high-court','HIGH-COURT'),
    ('supreme-court','SUPREME-COURT'),
    ('district-court','DISTRICT-COURT'),

]

class lawfirm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    years_of_exp = models.IntegerField()
    specialization = models.CharField(max_length=100)
    total_cases = models.IntegerField()
    description = models.TextField()
    advimg = models.ImageField(upload_to='advimg/',null=True,blank=True)

    def __str__(self):
      return self.name

class AllCases(models.Model):
    case_title=models.CharField(max_length=100)
    case_description=models.TextField()
    case_image=models.ImageField(upload_to='caseimg/',blank=True,null=True)


class Enquiry(models.Model):
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    case_type=models.CharField(max_length=100,choices=case_types) 
    description = models.TextField()
    any_doc = models.ImageField(upload_to='advimg/',null=True,blank=True)

    def __str__(self):
      return self.name

class Appointment(models.Model):
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    case_type=models.CharField(max_length=100,choices=case_types) 
    description = models.TextField()
    case_doc = models.ImageField(upload_to='advimg/',null=True,blank=True)
    total_no_hearings = models.BigIntegerField()
    court_name=models.CharField(max_length=100,choices=court_names) 
    fee = models.IntegerField()

    def __str__(self):
      return self.name
    

