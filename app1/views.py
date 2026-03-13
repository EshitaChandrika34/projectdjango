from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import Student
from .models import Studentdata
from .forms import SignupForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import LoginUser



def home(request):
    return render(request, 'app1/home.html')

def colleges(request):
    colleges_list =  [
        {'name': 'SVECW', 'slug': 'svecw'},
        {'name': 'VIT', 'slug': 'vit'},
        {'name': 'BVRIT', 'slug': 'bvrit'},
    ]
    return render(request, 'app1/colleges.html', {'colleges': colleges_list})

def college_detail(request, slug):
    college_data = {
        'svecw': {'name': 'SVECW', 'logo': 'svecw.png'},
        'vit': {'name': 'VIT', 'logo': 'vit.jpg'},
        'bvrit': {'name': 'BVRIT', 'logo': 'bvrit.png'},
    }

    college = college_data.get(slug)

    return render(request, 'app1/college_detail.html', {'college': college})

def students(request):
    students = Student.objects.all()
    return render(request, 'app1/students.html', {'students': students})


def address(request):
    return render(request, 'app1/address.html')
def login_page(request):
    return render(request,"app1/login.html")
#def loginverification(request):
    #uname=request.POST['username']
    #if uname== " ":
     #    print("sorry")
      #   return HttpResponse("sorry")
   # else:
    #    return HttpResponse(uname)




#def signup_form(request):
    #if request.method == "POST":
        #form = SignupForm(request.POST)

        #if form.is_valid():
          #  username = form.cleaned_data['username']

           
           # Studentdata.objects.create(name=username)
          # u1=Studentdata.objects.filter(name=username).exists()
          #print(u1)
          #if u1:
            #return HttpResponse("success")
          #else:
            #return HttpResponse("credentials does not match")
        

           # return HttpResponse("Data saved successfully")

        
        #return render(request, "app1/signupform.html", {"form": form})

    #form = SignupForm()
    #return render(request, "app1/signupform.html", {"form": form})

#def signup_form(request):
    #if request.method == "POST":
        #form = SignupForm(request.POST)

       # if form.is_valid():
             #   form.save()
            #username = form.cleaned_data['username']

           # exists = Studentdata.objects.filter(name=username).exists()
            #print(exists)

            #if exists:
               # return HttpResponse("success")
            #else:
                #return HttpResponse("credentials does not match")

        #return render(request, "app1/signupform.html", {"form": form})

    #form = SignupForm()
    #return render(request, "app1/signupform.html", {"form": form})

def loginverification(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        if not uname or not pwd:
            return HttpResponse("Username or Password missing")

        user = LoginUser.objects.filter(
            username=uname,
            password=pwd
        ).first()

        if user:
            request.session['userid'] = user.id
            request.session['uname'] = user.username
            request.session.set_expiry(60)
            return redirect("welcome")
        else:
            return HttpResponse("Invalid Username or Password")

    return render(request, "app1/login.html")




def signup_form(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, "app1/signupform.html", {"form": form})

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        LoginUser.objects.create(
            username=username,
            password=password
        )

        return render(request, "login.html")

    return render(request, "signupform.html")
def welcome(request):
    uname = request.session.get('uname')

    if not uname:
       return redirect("login")

    return HttpResponse(f"Welcome to the welcome page")