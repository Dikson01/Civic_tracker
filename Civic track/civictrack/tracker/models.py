from django.db import models

class CivicIssue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    photos = models.JSONField(default=list)  
    status = models.CharField(max_length=50, choices=[('Reported', 'Reported'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Reported')
    logs = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=True)

    def __str__(self):
        return self.title

