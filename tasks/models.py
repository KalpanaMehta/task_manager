from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('started', 'Started'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=120)
    description = models.TextField(max_length = 200,blank=True)
    due_date = models.DateField(null= True,blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return self.title