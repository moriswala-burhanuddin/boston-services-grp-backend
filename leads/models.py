from django.db import models
from services.models import Service

class Lead(models.Model):
    STATUS_CHOICES = (
        ('NEW', 'New'),
        ('CONTACTED', 'Contacted'),
        ('CONVERTED', 'Converted'),
        ('REJECTED', 'Rejected'),
    )

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='leads')
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"

class LeadPhoto(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='leads/photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.lead.name}"
