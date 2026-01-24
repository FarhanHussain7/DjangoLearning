from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to View page ")

def Home(request):
    return HttpResponse("<h1>Home page values are here </h1>")

def DynamicRoute(request, courseId):
    return HttpResponse(courseId)

def DynamicRouteAnyData(request, courseId):
    return HttpResponse(courseId)

# 
from django.shortcuts import render
def HomePage(request):
    return render(request,'O1_index.html')

def PassData(request):
    data={
        'title':"Pass Data view to Html",
        'description':'It will pass data here to html page help to see data from server to browser',
        'Process':'Process of Data passing',
        'Step':['O1- create a Html Page inside templates','O2- create function in views.py','O3- Create url routing and pass function in urls.py file']
    }
    return render(request,'O2_PassingData.html',data)

def PassDataLoop(request):
    data={
        'title':"Python Loop in Html",
        'description':'In Html using for loop for list , and dict data ',
        'Process':'use {{% Declare here your for Loop %}}',
        'Lang':['Python','Java ','Javascript'],
        'Student':[
            {'name':"Farhan hussain", 'phone': 9688438382,'address':"delhi"},
            {'name':"Imran ", 'phone': 9688438382,'address':"delhi"},
            {'name':"Suraj ", 'phone': 9688438382,'address':"delhi"},
            {'name':"Kabir ", 'phone': 9688438382,'address':"delhi"},
            {'name':"Faeem ", 'phone': 9688438382,'address':"delhi"},
        ],
        'Number':[10,23,40,30,50]
    }
    return render(request,'O3_Loop.html',data)

def Webpage(request):
    return render(request,'O4_Css_Style.html')

def Website(request):
    return render(request,'O5_base.html')

def Contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Print values in terminal
        print("Name:", name)
        print("Email:", email)
        print("Subject:", subject)
        print("Message:", message)

        # You can also add logic here to save data or send email

    return render(request, 'contact.html')

def Service(request):
    return render(request,'service.html')

def About(request):
    return render(request,'about.html')

def Form(request):
    try:
        name=request.GET['username']
        email=request.GET['email']
        phone=request.GET['phone']
        address=request.GET['address']
        print(name,email,phone,address)
    except:
        pass
    return render(request,'loginForm.html')