from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Service
from .forms import ServiceForm

def service_list(request):
    services = Service.objects.all()
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
