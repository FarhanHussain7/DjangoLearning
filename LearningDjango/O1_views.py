from django.http import HttpResponse, HttpResponseRedirect
from .forms import usersForm
from service.models import Service


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
    context = {}
    fn = usersForm()
    context={
        'form':fn
        }
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            number1 = request.POST.get("number1")
            number2 = request.POST.get("number2")
        # Print values in terminal
            print("Name:", name)
            print("Email:", email)
            print("Subject:", subject)
            print("Message:", message)
            print("Number 1:", number1)
            print("Number 2:", number2)
            
            # Add the numbers
            try:
                num1 = int(number1)
                num2 = int(number2)
                sum_result = num1 + num2
                print("Sum:", sum_result)
                
                # Pass the result back to the template
                context = {
                    'form': fn,
                    'sum_result': sum_result,
                    'num1': num1,
                    'num2': num2
                }
                
            except ValueError:
                context['error'] = "Please enter valid numbers"
                
        # You can also add logic here to save data or send email
            url = "/thank-you/?sum_result=" + str(sum_result)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request, 'contact.html', context)

def ThankYou(request):
    return render(request, 'thank_you.html')

def Service(request):
    return render(request,'service.html')

def About(request):
    return render(request,'about.html')

def Calculator(request):
    result = None
    context = {}
    
    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1", 0))
            num2 = float(request.POST.get("num2", 0))
            operation = request.POST.get("operation", "add")
            
            print(f"Number 1: {num1}")
            print(f"Number 2: {num2}")
            print(f"Operation: {operation}")
            
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    context['error'] = "Cannot divide by zero!"
            elif operation == "power":
                result = num1 ** num2
            elif operation == "modulo":
                if num2 != 0:
                    result = num1 % num2
                else:
                    context['error'] = "Cannot modulo by zero!"
            
            if result is not None:
                context['result'] = round(result, 4)
                context['num1'] = num1
                context['num2'] = num2
                context['operation'] = operation
                print(f"Result: {result}")
                
        except ValueError:
            context['error'] = "Please enter valid numbers!"
    
    return render(request, 'O6_calculater.html', context)

def Form(request):
    try:
        if request.method == "POST":
            # Get all form input values
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            phone = request.POST.get("phone")
            dob = request.POST.get("dob")
            address = request.POST.get("address")
            age = request.POST.get("age")
            gender = request.POST.get("gender")
            interests = request.POST.getlist("interests")
            country = request.POST.get("country")
            favorite_color = request.POST.get("favorite_color")
            experience = request.POST.get("experience")
            website = request.POST.get("website")
            search = request.POST.get("search")
            resume = request.FILES.get("resume")
            time_preferred = request.POST.get("time")
            birth_month = request.POST.get("month")
            week = request.POST.get("week")
            form_id = request.POST.get("form_id")
            
            # Print all values in terminal
            print("Username:", username)
            print("Email:", email)
            print("Password:", password)
            print("Confirm Password:", confirm_password)
            print("Phone:", phone)
            print("Date of Birth:", dob)
            print("Address:", address)
            print("Age:", age)
            print("Gender:", gender)
            print("Interests:", interests)
            print("Country:", country)
            print("Favorite Color:", favorite_color)
            print("Experience:", experience)
            print("Website:", website)
            print("Search:", search)
            print("Resume:", resume)
            print("Preferred Time:", time_preferred)
            print("Birth Month:", birth_month)
            print("Week:", week)
            print("Form ID:", form_id)
            
            # You can add logic here to save data to database or send email
            url = "/thank-you/?name=" + username
            return HttpResponseRedirect(url)
    except Exception as e:
        print("Error:", str(e))
    return render(request,'loginForm.html')


    def FormValidation(request):
        context = {}
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            
            # Basic validation
            if not username or not email or not password or not confirm_password:
                context['error'] = "All fields are required!"
            elif password != confirm_password:
                context['error'] = "Passwords do not match!"
            else:
                # If validation passes, you can save data or redirect
                url = "/thank-you/?name=" + username
                return HttpResponseRedirect(url)
        
        return render(request, 'O8_Form_validation.html', context)