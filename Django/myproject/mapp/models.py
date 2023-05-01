from django.db import models

"""
TYPE_CHOICES=(
    ("", ""),
    ("BLOOD", "BLOOD"),
    ("BREAST", "BREAST"),
    ("LUNG", "LUNG"),
    ("PROSTATE", "PROSTATE"),
    ("SKIN", "SKIN"),
)
GENDER_CHOICES=(
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
)
STAGE_CHOICES=(
    ("", ""),
    ("EARLY", "EARLY"),
    ("ADVANCED", "ADVANCED"),
)
KIND_CHOICES=(
    ("", ""),
    ("HODGKIN LYMPHOMA", "HODGKIN LYMPHOMA"),
    ("NON-HODGKIN LYMPHOMA", "NON-HODGKIN LYMPHOMA"),
    ("MULTIPLE LYMPHOMA", "MULTIPLE LYMPHOMA"),
    ("NON-RECURRENT", "NON-RECURRENT"),
    ("LOCALLY-ADVANCED", "LOCALLY-ADVANCED"),
    ("RECURRENT", "RECURRENT"),
    ("NON-SMALL CELL", "NON-SMALL CELL"),
    ("SMALL CELL", "SMALL CELL"),
    ("BASAL CELL CARCINOMA", "BASAL CELL CARCINOMA"),
    ("SQUAMOUS CELL CARCINOMA", "SQUAMOUS CELL CARCINOMA"),
    ("MERKEL CELL CARCINOMA", "MERKEL CELL CARCINOMA"),
)
"""

# Create your models here.

class Patient(models.Model):
    patient_id = models.CharField(max_length=8,primary_key=True,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender=models.CharField(max_length=6)#, choices=(GENDER_CHOICES),default='')
    age = models.CharField(max_length=2)
    img=models.ImageField(upload_to="media/")
    type=models.CharField(max_length=15)#,choices=(TYPE_CHOICES),default='')
    stage=models.CharField(max_length=15)#,choices=(STAGE_CHOICES),default='')
    kind=models.CharField(max_length=35)#,choices=(KIND_CHOICES), default='')
    clid = models.CharField(max_length=6)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=40)
    address_a = models.TextField(max_length=60)
    address_b = models.TextField(max_length=60)
    analysis = models.CharField(max_length=6, default="NA")
    def __str__(self):
        return self.email
    
class Clinic(models.Model):
    cid = models.CharField(max_length=6, primary_key=True, unique=True)
    cname = models.CharField(max_length=30)
    cemail=models.EmailField(max_length=40)
    def __str__(self):
        return self.cemail