from django.shortcuts import redirect, render

from lawfirmapp.forms import LawFirmForm,EnquiryForm,AppointmentForm
from lawfirmapp.models import lawfirm,Enquiry,AllCases,Appointment
from lawfirmapp.utils import send_email_view

# Create your views here.
def home(request):
    casedata = AllCases.objects.all()
    return render(request,'lawfirm/home.html',{'casedata':casedata})

def about(request):
    data = lawfirm.objects.last()
    return render(request,'lawfirm/about.html',{'firm':data})

def profile(request):
    form = LawFirmForm()
    if request.method == 'POST':
        form = LawFirmForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Submitted")
            return redirect('about')
    return render(request,'lawfirm/profile.html',{'form':form})

def Case_Type(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = Enquiry(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Submitted")
    return render('lawfirm/enquiry.html',{'form':form})
    # return render(request,'lawfirm/allcases.html',{'form':form})

def allCases(request):
    casedata = AllCases.objects.all()
    return render(request,'lawfirm/allCases.html',{'casedata':casedata})

def enquery(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Submitted")
            return redirect('enquery')
    enqueries = Enquiry.objects.all()
    return render(request,'lawfirm/enquery.html',{'form':form,'enqueries':enqueries})

def appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST,request.FILES)
        if form.is_valid():

            print("Success")
            email = form.cleaned_data['email']
            print(email)

            response = send_email_view(email)
            return response
            # print("sent email")

            # form.save()
            print("Appointment Fixed")
            return redirect('appointment')
    appointments = Appointment.objects.all()
    return render(request,'lawfirm/appointment.html',{'form':form,'appointments':appointments})


