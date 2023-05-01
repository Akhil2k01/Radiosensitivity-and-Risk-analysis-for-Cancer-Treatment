from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Patient, Clinic
from mapp.forms import UserImage 
import subprocess

# Create your views here.

def home(request):
    return render(request, 'home.html' )

def about(request):
    return render(request, 'about.html' )

def cregister(request):
    if request.method=='POST':
        cid = request.POST['cid']
        cname = request.POST['cname']
        cemail = request.POST['cemail']

        clinic = Clinic()
        clinic.cid = cid
        clinic.cname = cname
        clinic.cemail = cemail

        clinic.save()
        
        msg = 'Your request of clinic registration is successful.'
        messages.info(request, msg)
        return redirect(cregister)
    else:
        return render(request, 'cregister.html' )

def pform(request):
    if request.method=='POST':

        img=request.FILES['img']
        gender=request.POST['gender']
        type=request.POST['type']
        kind=request.POST['kind']
        stage=request.POST['stage']
        clid = request.POST['clid']
        patient_id = request.POST['id']
        first_name = request.POST['first_name']
        last_name =request.POST['last_name']
        age =request.POST['age']
        email=request.POST['email']
        phone=request.POST['phone']
        address_a = request.POST['address_a']
        address_b = request.POST['address_b']

        if not Clinic.objects.raw("SELECT cid from mapp_Clinic AS c WHERE c.cid=="+clid):
            msg = 'Please register clinic before entering the patient form.'
            messages.info(request, msg)
            return redirect(pform)

        #Checking correct drop down values
        lsblood = ['Hodgkin lymphoma', 'Non-Hodgkin lymphoma', 'Multiple lymphoma']
        lsbreast = ['Non-recurrent', 'Locally-advanced', 'Recurrent']
        lslung = ['Non-Small cell', 'Small cell']
        lsskin = ['Basal cell carcinoma', 'Squamous cell carcinoma', 'Merkel  cell carcinoma']
        lsprostate = ['Non-recurrent', 'Locally-advanced', 'Recurrent']

        if type == 'Blood'and kind not in lsblood:
            msg = 'Select appropriate blood cancer kinds : Hodgkin lymphoma, Non-Hodgkin lymphoma, Multiple lymphoma'
            messages.info(request, msg)
            return redirect(pform)
        elif type == 'Breast'and kind not in lsbreast:
            msg = 'Select appropriate breast cancer kinds : Non-recurrent, Locally-advanced, Recurrent'
            messages.info(request, msg)
            return redirect(pform)
        elif type == 'Lung'and kind not in lslung:
            msg = 'Select appropriate lung cancer kinds : Non-Small cell, Small cell'
            messages.info(request, msg)
            return redirect(pform)
        elif type == 'Skin'and kind not in lsskin:
            msg = 'Select appropriate skin cancer kinds : Basal cell carcinoma, Squamous cell carcinoma, Merkel  cell carcinoma'
            messages.info(request, msg)
            return redirect(pform)
        elif type == 'Prostate' and kind not in lsprostate:
            msg = 'Select appropriate prostate cancer kinds : Non-recurrent, Locally-advanced, Recurrent'
            messages.info(request, msg)
            return redirect(pform)

        #save image
        form = UserImage(request.POST, request.FILES) 
        if form.is_valid:
            form.save()

        #save form entry in table
        patient = Patient()
        patient.img = img
        patient.gender = gender
        patient.type = type
        patient.kind = kind
        patient.stage = stage
        patient.clid = clid #clinic.objects.get(pk=clid)
        patient.patient_id = patient_id
        patient.first_name = first_name
        patient.last_name = last_name
        patient.age = age
        patient.email = email
        patient.phone = phone
        patient.address_a = address_a
        patient.address_b = address_b
        patient.analysis = "NODONE"

        patient.save()
        
        msg = 'Please wait your request is being processed....'
        messages.info(request, msg)

        msg = 'Your Request has been successfully submitted. We will send the result to your email.'
        messages.info(request, msg)
        path = "C:/Users/Dell/Desktop/final_proj/codes/mail.py"
        subprocess.run(["Python", path])
        return redirect(pform)
    else:
        return render(request, 'pform.html')

def help(request):
    return render(request, 'help.html' )