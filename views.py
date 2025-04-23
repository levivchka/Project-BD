from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Doctor, Schedule, Study
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def home(request):
    return render(request, 'scheduler/home.html')

@login_required
def schedule_view(request):
    context = {
        'doctors': Doctor.objects.all(),
        'schedule': Schedule.objects.all().order_by('date')
    }
    return render(request, 'scheduler/schedule.html', context)

class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'scheduler/doctor_list.html'
    context_object_name = 'doctors'

@login_required
def analytics_view(request):
    # Здесь будет логика для аналитики и прогнозирования
    return render(request, 'scheduler/analytics.html')

    # medical_scheduler/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scheduler.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# scheduler/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('doctors/', views.DoctorListView.as_view(), name='doctor_list'),
    path('analytics/', views.analytics_view, name='analytics'),
]