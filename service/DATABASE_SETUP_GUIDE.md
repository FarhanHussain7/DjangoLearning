# Django Database Setup & Model Creation Guide
# ===========================================

## 📋 Prerequisites
- Django project already created
- MySQL database installed and running
- Virtual environment activated (recommended)

## 🗄️ Step 1: Database Setup

### Option A: MySQL Database Setup
1. **Install MySQL connector:**
   ```bash
   pip install mysqlclient
   ```

2. **Create database in MySQL:**
   ```sql
   CREATE DATABASE service CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'farhan'@'localhost' IDENTIFIED BY 'Farhan123';
   GRANT ALL PRIVILEGES ON service.* TO 'farhan'@'localhost';
   FLUSH PRIVILEGES;
   ```

3. **Update settings.py:**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'service',
           'USER': 'farhan',
           'PASSWORD': 'Farhan123',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

### Option B: SQLite (Default - Good for Development)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## 🏗️ Step 2: Model Creation

### Current Models in service/models.py:
```python
from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
```

### Enhanced Models with More Fields:
```python
from django.db import models
from django.urls import reverse

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile App'),
        ('design', 'UI/UX Design'),
        ('consulting', 'Consulting'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    is_active = models.BooleanField(default=True)
    duration_days = models.PositiveIntegerField(help_text="Duration in days")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['-created_at']

class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('support', 'Technical Support'),
        ('billing', 'Billing Question'),
        ('feedback', 'Feedback'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='general')
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['-created_at']
```

## 🔄 Step 3: Create Migrations

1. **Make migrations:**
   ```bash
   python manage.py makemigrations service
   ```

2. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Check migration status:**
   ```bash
   python manage.py showmigrations
   ```

## 🎛️ Step 4: Admin Configuration

### Update service/admin.py:
```python
from django.contrib import admin
from .models import Service, Contact

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'category')
        }),
        ('Pricing & Duration', {
            'fields': ('price', 'duration_days')
        }),
        ('Media & Status', {
            'fields': ('image', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_resolved', 'created_at']
    list_filter = ['subject', 'is_resolved', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_resolved']
    readonly_fields = ['created_at', 'updated_at']
    
    actions = ['mark_as_resolved', 'mark_as_unresolved']
    
    def mark_as_resolved(self, request, queryset):
        queryset.update(is_resolved=True)
    mark_as_resolved.short_description = "Mark selected as resolved"
    
    def mark_as_unresolved(self, request, queryset):
        queryset.update(is_resolved=False)
    mark_as_unresolved.short_description = "Mark selected as unresolved"
```

## 🌐 Step 5: Create Views

### Update service/views.py:
```python
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Service, Contact
from .forms import ServiceForm, ContactForm

# Service Views
class ServiceListView(ListView):
    model = Service
    template_name = 'service/service_list.html'
    context_object_name = 'services'
    paginate_by = 6

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service/service_detail.html'
    context_object_name = 'service'

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service/service_form.html'
    success_url = reverse_lazy('service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service/service_form.html'
    success_url = reverse_lazy('service_list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service/service_confirm_delete.html'
    success_url = reverse_lazy('service_list')

# Contact Views
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'service/contact_form.html', {'form': form})

def contact_success(request):
    return render(request, 'service/contact_success.html')
```

## 📝 Step 6: Create Forms

### Create service/forms.py:
```python
from django import forms
from .models import Service, Contact

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'category', 'duration_days', 'image', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'duration_days': forms.NumberInput(attrs={'min': 1}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0")
        return price

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
            'phone': forms.TextInput(attrs={'placeholder': '+1 (555) 123-4567'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Add custom email validation if needed
        return email
```

## 🔗 Step 7: URL Configuration

### Update service/urls.py:
```python
from django.urls import path
from . import views

urlpatterns = [
    # Service URLs
    path('', views.ServiceListView.as_view(), name='service_list'),
    path('create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service_update'),
    path('<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),
    
    # Contact URLs
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
```

### Update main urls.py to include service URLs:
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from LearningDjango import O1_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('service.urls')),  # Include service app URLs
    # ... other URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 🖼️ Step 8: Media Files Setup

### Add to settings.py:
```python
import os

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

## 🚀 Step 9: Run Commands

1. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

2. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

3. **Run development server:**
   ```bash
   python manage.py runserver
   ```

## 🌐 Step 10: Access Your Application

- **Admin Panel:** http://127.0.0.1:8000/admin/
- **Service List:** http://127.0.0.1:8000/services/
- **Create Service:** http://127.0.0.1:8000/services/create/
- **Contact Form:** http://127.0.0.1:8000/services/contact/

## 🔍 Step 11: Database Commands Reference

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migrations status
python manage.py showmigrations

# Reset database (WARNING: Deletes all data)
python manage.py flush

# Create superuser
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Database shell
python manage.py dbshell
```

## 📝 Step 12: Django Shell Examples

```python
# Start shell
python manage.py shell

# Create service
from service.models import Service
service = Service.objects.create(
    name="Web Development",
    description="Full-stack web development service",
    price=999.99,
    category="web",
    duration_days=30
)

# Query services
services = Service.objects.all()
active_services = Service.objects.filter(is_active=True)
web_services = Service.objects.filter(category="web")

# Update service
service = Service.objects.get(pk=1)
service.price = 1299.99
service.save()

# Delete service
service = Service.objects.get(pk=1)
service.delete()
```

## ⚠️ Troubleshooting

### Common Issues:
1. **Migration errors:** Delete migration files and run `makemigrations` again
2. **Database connection errors:** Check database credentials and server status
3. **Static files not loading:** Run `collectstatic` and check URLs configuration
4. **Media files not uploading:** Check MEDIA_ROOT and MEDIA_URL settings

### Debug Commands:
```bash
# Check Django version
python -m django --version

# Check settings
python manage.py check --deploy

# List all commands
python manage.py help
```

## 📚 Next Steps

1. **Add authentication system**
2. **Implement user permissions**
3. **Add API endpoints (Django REST Framework)**
4. **Add testing suite**
5. **Deploy to production**

---
*This guide covers the complete workflow from database setup to a fully functional Django app with models, views, and admin interface.*
