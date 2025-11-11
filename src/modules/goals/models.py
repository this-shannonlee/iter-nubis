from django.db import models


# Create your models here.
class Goal(models.Model):
    title = models.CharField(max_length=200)
    synopsis = models.TextField(null=True, blank=True)
    url = models.URLField()
    priority = models.IntegerField(max_value=5)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)


class Objective(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
