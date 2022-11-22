from django.db import models

# Create your models here.
from django.db import models

class Todo(models.Model):
    STATUS_CHECK = (
        ('PENDING', 'PENDING'),
        ('COMPLETED', 'COMPLETED'),
        ('INPROGRESS', 'INPROGRESS'),
    )
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=10, choices= STATUS_CHECK)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
