from django.http import HttpResponse, HttpResponseRedirect
from .forms import usersForm
from service.models import Service, Contact, News
from .utils import send_contact_email

# Display a simple welcome message for the About Us page
def aboutUs(request):
    # Return a basic HTTP response with a welcome message
    return HttpResponse("Welcome to View page ")

# Display a simple HTML response for the Home page
def Home(request):
    # Return a basic HTTP response with an HTML header
    return HttpResponse("<h1>Home page values are here </h1>")

# Handle dynamic URL routing with integer course ID parameter
def DynamicRoute(request, courseId):
    # Return the course ID as an HTTP response
    return HttpResponse(courseId)

# Handle dynamic URL routing with any type of data parameter
def DynamicRouteAnyData(request, courseId):
    # Return the course ID as an HTTP response
    return HttpResponse(courseId)

# 
from django.shortcuts import render


# Render the main home page with navigation to all Django learning pages
def HomePage(request):
    """
    This function renders the main home page with navigation to all Django learning pages.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered HTML response.
    """
    NewsData = News.objects.all()
    context = {
        'NewsData': NewsData
    }
    # Use the render function to render the O1_index.html template
    return render(request,'O1_index.html',context)

# Demonstrate passing data from view to template with context dictionary
def PassData(request):
    """
    This function demonstrates passing data from the view to the template using a context dictionary.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered HTML response with passed data.
    """
    # Create a dictionary with sample data to pass to template
    data={
        'title':"Pass Data view to Html",
        'description':'It will pass data here to html page help to see data from server to browser',
        'Process':'Process of Data passing',
        'Step':['O1- create a Html Page inside templates','O2- create function in views.py','O3- Create url routing and pass function in urls.py file']
    }
    return render(request,'O2_PassingData.html',data)

# Demonstrate using Django template loops with lists and dictionaries
def PassDataLoop(request):
    """
    This function demonstrates using Django template loops with lists and dictionaries.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered HTML response with looped data.
    """
    # Create sample data including lists and dictionaries to demonstrate loop functionality
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

# Display CSS styling demonstration page
def Webpage(request):
    """
    This function displays a CSS styling demonstration page.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered HTML response with CSS styling.
    """
    # Render the CSS styling demonstration template
    return render(request,'O4_Css_Style.html')

# Display base template or website layout demonstration
def Website(request):
    """
    This function displays a base template or website layout demonstration.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered HTML response with base template.
    """
    # Render the base template or website layout demonstration
    return render(request,'O5_base.html')

# Handle contact form submission and display contact page
def Contact(request):
    """
    This function handles contact form submission and displays the contact page.
    It processes form data and performs basic calculations.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered contact page with form or success redirect.
    """
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
    return render(request, 'pages/contact.html', context)

# Display thank you page after successful form submission
def ThankYou(request):
    """
    This function displays a thank you page after successful form submission.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered thank you page.
    """
    return render(request, 'pages/thank_you.html')

# Display service information page
def Service(request):
    """
    This function displays the service information page.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered service page.
    """
    return render(request,'pages/service.html')

# Display about us page with company information
def About(request):
    """
    This function displays the about us page with company information.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered about page.
    """
    return render(request,'pages/about.html')

# Perform mathematical calculations with basic operations
def Calculator(request):
    """
    This function performs mathematical calculations with basic operations.
    Supports add, subtract, multiply, divide, power, and modulo operations.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered calculator page with results.
    """
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

# Handle comprehensive login form with multiple input fields
def Form(request):
    """
    This function handles a comprehensive login form with multiple input fields.
    It processes various user data and redirects to thank you page.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered login form page or success redirect.
    """
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
    return render(request,'pages/loginForm.html')

# Validate user input with basic form validation rules
def FormValidation(request):
    """
    This function validates user input with basic form validation rules.
    Checks for required fields and password confirmation.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered validation form or success redirect.
    """
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
    
    # Render the validation form with the context
    return render(request, 'O8_Form_validation.html', context)

# Display comprehensive Django template filters examples with various data types
def FilterExample(request):
    """
    This function displays comprehensive Django template filters examples.
    Shows various filter types: string, number, date, list, dictionary, boolean, and safe filters.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered filter examples page with sample data.
    """
    from datetime import datetime, timedelta
    
    # String data for string filters
    my_string = "hello world this is a django filter example"
    
    # Number data for number filters
    my_number = 1048576  # 1 MB in bytes
    price = 29.99
    decimal_number = 3.14159
    
    # Date data for date filters
    current_date = datetime.now()
    past_date = datetime.now() - timedelta(days=5)
    
    # List data for list filters
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    # Dictionary data for dictionary filters
    my_dict = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York',
        'email': 'john@example.com'
    }
    
    # Boolean and default data
    is_active = True
    empty_value = None
    
    # HTML string for safe/escape filters
    html_string = "<strong>Bold Text</strong> and <em>italic text</em>"
    
    # Products data for table demonstration
    products = [
        {
            'name': 'laptop computer',
            'category': 'electronics',
            'price': 999.99,
            'stock': 15,
            'in_stock': True,
            'created': datetime.now() - timedelta(days=30)
        },
        {
            'name': 'wireless mouse',
            'category': 'electronics',
            'price': 25.50,
            'stock': 0,
            'in_stock': False,
            'created': datetime.now() - timedelta(days=20)
        },
        {
            'name': 'office chair',
            'category': 'furniture',
            'price': 199.99,
            'stock': 8,
            'in_stock': True,
            'created': datetime.now() - timedelta(days=15)
        },
        {
            'name': 'desk lamp',
            'category': 'furniture',
            'price': 45.75,
            'stock': 12,
            'in_stock': True,
            'created': datetime.now() - timedelta(days=10)
        },
        {
            'name': 'notebook set',
            'category': 'stationery',
            'price': 12.99,
            'stock': 0,
            'in_stock': False,
            'created': datetime.now() - timedelta(days=5)
        }
    ]
    
    # Context dictionary with all data
    context = {
        'my_string': my_string,
        'my_number': my_number,
        'price': price,
        'decimal_number': decimal_number,
        'current_date': current_date,
        'past_date': past_date,
        'my_list': my_list,
        'my_dict': my_dict,
        'is_active': is_active,
        'empty_value': empty_value,
        'html_string': html_string,
        'products': products
    }
    
    return render(request, 'O9_Filter.html', context)

# Display overview page for all service-related functionality
def ServicePages(request):
    """
    This function displays an overview page for all service-related functionality.
    Provides navigation to service list, create, and detail pages.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered service pages overview.
    """
    return render(request, 'service/service_pages.html')

def NewsList(request, slug):
    """
    This function displays an overview page for all news-related functionality.
    Provides navigation to news list, create, and detail pages.
    
    Parameters:
    request (HttpRequest): The current HTTP request.    
        Returns:
    HttpResponse: The rendered news pages overview.
    """
    NewsData = News.objects.get(slug=slug)
    context = {
        'NewsData': NewsData
    }
    return render(request, 'service/news_details.html', context)


def Email(request):
    """
    This function demonstrates sending an email using Django's email functionality.
    It sends a test email to a specified recipient.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: A response indicating whether the email was sent successfully or if there was an error.
    """
    from django.core.mail import send_mail
    from django.conf import settings
    
    subject = "Test Email from Django"
    message = "This is a test email sent from a Django view."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['fh4456200@gmail.com']   
    try:
        send_mail(
            subject, 
            message, 
            from_email, 
            recipient_list)
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending email: {str(e)}")   
    

def EmailTemplate(request):
    """
    This function demonstrates sending an email using a Django template for the email body.
    It renders an HTML template and sends it as the email content.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: A response indicating whether the email was sent successfully or if there was an error.
    """
    from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
    from django.template.loader import render_to_string
    from django.conf import settings
    
    subject = "Test Email with Template from Django"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['fh4456200@gmail.com']
    # Render the email body using a template
    email_body = render_to_string('email_template.html', {'username': 'John Doe'})  
    email = EmailMessage(subject, email_body, from_email, recipient_list)
    email.content_subtype = "html"  # Set content type to HTML  
    try:
        email.send()
        return HttpResponse("Email with template sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error sending email: {str(e)}")

# Send email using contact form data
def send_email(request):
    """
    This function sends an email using contact form data.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: Redirect to home page after sending email.
    """
    from django.shortcuts import redirect
    from LearningDjango.utils import send_contact_email
    
    if request.method == 'POST':
        try:
            # Use the simple utility function
            send_contact_email(request)
            
            # Return HTML with JavaScript popup alert
            return HttpResponse("""
                <script>
                    alert('Email sent successfully! 📧');
                    window.location.href = '/';
                </script>
            """)
        except Exception as e:
            return HttpResponse(f"""
                <script>
                    alert('Error sending email: {str(e)}');
                    window.location.href = '/';
                </script>
            """)
    
    return redirect('/')

# Simple email test form
def simple_email_test(request):
    """
    This function renders a simple email test form.
    
    Parameters:
    request (HttpRequest): The current HTTP request.
    
    Returns:
    HttpResponse: The rendered email test form.
    """
    return render(request, 'simple_email_test.html')