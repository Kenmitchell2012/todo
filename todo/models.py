from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=250, blank=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task