from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors/', null=True, blank=True)
    competencies = models.TextField()
    schedule_pattern = models.CharField(max_length=50)  # например "2/2" или "5/2"
    
    def __str__(self):
        return f"{self.user.get_full_name()}"

class Modality(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    max_studies_per_shift = models.IntegerField()

    def __str__(self):
        return self.name

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    shift_type = models.CharField(max_length=20)  # утро/день/ночь
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['doctor', 'date']

class Study(models.Model):
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE)
    date = models.DateField()
    count = models.IntegerField()
    complexity = models.CharField(max_length=20)