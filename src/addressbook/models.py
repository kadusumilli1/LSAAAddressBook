from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your models here.

"""user = User.objects.create_user('kim', 'kim@indiana.com', 'kimpassword')
user.save()


user = authenticate(username='kim', password='kimpassword')
if user is not None:
    # the password verified for the user
    if user.is_active:
        print("User is valid, active and authenticated")
    else:
        print("The password is valid, but the account has been disabled!")
else:
    # the authentication system was unable to verify the username and password
    print("The username and password were incorrect.")"""

#contact model 
class Contact(models.Model):
	firstname = models.CharField(max_length = 20, null = False , blank = False)
	lastname = models.CharField(max_length = 20, null = False , blank = False)
	phone = models.CharField(max_length = 10, null = False , blank = False)
	email = models.EmailField(max_length = 20, null = False , blank = False)
	address = models.TextField(max_length = 10, null = False , blank = False)

#form to collect user input
class createNewContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['firstname','lastname','phone','email','address']




