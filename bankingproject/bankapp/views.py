from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login as auth_login,logout
from .models import Register_User, Fill_Form
from .forms import Fill_FormForm
from django.views import View

class Form(View):
    def get(self,request):
        form = Fill_FormForm()
        return render(request,'fill_forms.html',{'form':form})
    def post(self,request):
        form = Fill_FormForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully')
            return redirect('fill_forms')
        else:
            return render(request,'fill_forms.html',{'form':form})


# Create your views here.
# for index page
def index(request):
    return render(request,'index.html')

#  for about page
def about(request):
    return render(request,'about.html')

# for registration page
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Taken ')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            return render(request,'login.html')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

# for login page
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')



#
def newpage(request):
    if request.method == 'POST':
        form=userCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'newpage.html')
            print("form submitted")
        else:
            print("form not submitted")
            return render(request,'newpage.html')
    else:
        form=UserCreationForm()
        return render(request,'newpage.html',{'form':form})

    return render(request,'newpage.html')



# for form filling
# def form(request):
#     if request.method == 'POST':
#         user=request.POST['name']
#         dob=request.POST['dob']
#         age=request.POST['age']
#         gender=request.POST['gender']
#         phone=request.POST['phone']
#         mail=request.POST['mail']
#         address=request.POST['address']
#         district=request.POST['district']
#         branch=request.POST['branch']
#         account_type=request.POST['account_type']
#         materials_provided=request.POST['materials_provided']
#         form=Register_User(user=user,dob=dob,age=age,gender=gender,phone_number=phone,mail_id=mail,address=address,district=district,branch=branch,account_type=account_type,materials_provided=materials_provided)
#         form.save()
#         messages.info(request,'form submitted')
#         return render(request,'form.html')
#     else:
#         return render(request,'form.html')


  # Replace with the actual name of your form
