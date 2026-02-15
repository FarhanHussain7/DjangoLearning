from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Service, News, Contact
from .forms import ServiceForm
from django.core.paginator import Paginator


def service_list(request):
    services = Service.objects.all()
    query = request.GET.get('servicename')
    if query:
        services = Service.objects.filter(name__icontains=query)
    return render(request, 'service/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service/service_detail.html', {'service': service})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service/service_form.html', {'form': form})

def service_contact(request):
    contactData = Contact.objects.all()
    paginate=Paginator(contactData, 3)
    page_number=request.GET.get('page')
    contactData=paginate.get_page(page_number)
    context = {
        'contactData': contactData,
        # 'paginate': paginate
    }   
    return render(request, 'service/service_contact.html', context)