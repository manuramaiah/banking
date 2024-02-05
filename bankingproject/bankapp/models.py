# import necessary libraries
from django.db import models
# from django import forms
# from .models import UserProfile, District, Branch, AccountType, Material
# Create your models here.
# for new user
class Register_User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username
# district choice
DISTRICT_CHOICE = (
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Kollam', 'Kollam'),
    ('Pathanamthitta', 'Pathanamthitta'),
    ('Alappuzha', 'Alappuzha'),
    ('Kottayam', 'Kottayam'),
    ('Idukki', 'Idukki'),
    ('Ernakulam', 'Ernakulam'),
    ('Thrissur', 'Thrissur'),
    ('Palakkad', 'Palakkad'),
    ('Malappuram', 'Malappuram'),
    ('Kozhikode', 'Kozhikode'),
    ('Wayanad', 'Wayanad'),
    ('Kannur', 'Kannur'),
    ('Kasaragod', 'Kasaragod'),
)

# branch choice
BRANCH_CHOICE = (
    ('Attingal', 'Attingal'),
    ('Neyyaattinkara', 'Neyyaattinkara'),
    ('Kilimanoor', 'Kilimanoor'),
    ('Varkala', 'Varkala'),
    ('Kattakkada', 'Kattakkada'),
    ('Karunagappally', 'Karunagappally'),
    ('Kadakkal', 'Kadakkal'),
    ('Kottiyim', 'Kottiyim'),
    ('Kundara', 'Kundara'),
    ('Kollam Town', 'Kollam Town'),
    ('Pathanamthitta Town', 'Pathanamthitta Town'),
    ('Ranni', 'Ranni'),
    ('Thiruvalla', 'Thiruvalla'),
    ('Adoor', 'Adoor'),
    ('Omalloor', 'Omalloor'),
    ('Aroor', 'Aroor'),
    ('Cherthala', 'Cherthala'),
    ('Haripad', 'Haripad'),
    ('Kayamkulam', 'Kayamkulam'),
    ('Mannar', 'Mannar'),
    ('Pala', 'Pala'),
    ('Kanjirapally', 'Kanjirapally'),
)
# account type
ACCOUNT_TYPE_CHOICE = (
    ('Savings', 'Savings'),
    ('Current', 'Current'),
    ('Fixed Deposit', 'Fixed Deposit'),
    ('Recurring Deposit', 'Recurring Deposit'),
    ('Overdraft', 'Overdraft'),
    ('Credit', 'Credit'),
    ('Debit', 'Debit'),
    ('Loan', 'Loan'),
    ('Mortgage', 'Mortgage'),
    ('Joint', 'Joint'),
    ('Personal', 'Personal'),
    ('Corporate', 'Corporate'),
    ('Government', 'Government'),
    ('Business', 'Business'),
    ('Hybrid', 'Hybrid'),
    ('NRI', 'NRI'),
    ('Foreign', 'Foreign'),
    ('Domestic', 'Domestic'),
    ('Others', 'Others'),
)

# creating model for fill the form



class Fill_Form(models.Model):
    user_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(auto_now=False, auto_now_add=False)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    phone_number=models.PositiveIntegerField()
    mail_id=models.EmailField()
    address=models.TextField(max_length=200)
    district=models.CharField(choices=DISTRICT_CHOICE,max_length=100)
    branch=models.CharField(choices=BRANCH_CHOICE,max_length=100)
    type_of_account=models.CharField(choices=ACCOUNT_TYPE_CHOICE,max_length=100)
    materials_provided=models.CharField(max_length=100)