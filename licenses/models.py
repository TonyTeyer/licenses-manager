from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User

# Create your models here.

class Licenses(models.Model):
    companyname = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=50, blank=False)
    jobtitle = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, validators=[EmailValidator])
    softwareusername = models.CharField(max_length=50, blank=False)
    expirationdate = models.DateField(blank=False)
    version = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    # relation with users & cascade deletion
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #Show the company name and the name of the user who registered the license in the administrator dashboard
    def __str__(self):
        return self.companyname + ' - License of: ' + self.user.username