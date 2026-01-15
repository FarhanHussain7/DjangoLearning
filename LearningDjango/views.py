from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to View page ")

def Home(request):
    return HttpResponse("<h1>Home page values are here </h1>")

def DynamicRoute(request, courseId):
    return HttpResponse(courseId)

def DynamicRouteAnyData(request, courseId):
    return HttpResponse(courseId)
