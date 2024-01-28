from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    status_names = [
        ('in_progress','In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ]
    name = models.CharField(max_length=40, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    status = models.CharField(choices=status_names, default='todo')
    members = models.ManyToManyField(User, related_name='projects')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
            user = kwargs.pop('user', None)
            if user:
                self.created_by = user
        super().save(*args, **kwargs)

class Task(models.Model):
    status_names = [
        ('to_do', 'Todo'),
        ('in_progress','In Progress'),
        ('done', 'Done')
    ]
    name = models.CharField(max_length=40, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    deadline_time = models.DateTimeField(blank=False, null=False)
    status = models.CharField(choices=status_names, default='todo')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='assignee')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,  blank=False, null=True, related_name='created_by')
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            if not self.id:
                self.created_on = timezone.now()
        super().save(*args, **kwargs)