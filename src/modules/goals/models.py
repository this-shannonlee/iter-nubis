from datetime import timedelta
from django.utils import timezone
from django.db import models
from modules.home.models import Tag
from modules.certifications.models import Certification


def get_default_due_date():
    return timezone.now() + timedelta(days=28)


class GoalCommon(models.Model):
    title = models.CharField(unique=True, max_length=200)
    synopsis = models.TextField(blank=True)
    url = models.URLField()
    notes = models.TextField(blank=True)
    is_complete = models.BooleanField("Complete", default=False)
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    last_updated = models.DateTimeField("Last Updated", auto_now=True)

    class Meta:
        abstract = True


class Goal(GoalCommon):
    certification = models.OneToOneField(
        Certification, on_delete=models.CASCADE, null=True, blank=True
    )
    PRIORITY_CHOICES = [
        (1, "Critical"),
        (2, "High"),
        (3, "Medium"),
        (4, "Low"),
        (5, "Optional"),
    ]
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=3)
    due_date = models.DateTimeField(default=get_default_due_date)

    class Meta:
        ordering = ["priority", "-due_date"]
        indexes = [
            models.Index(
                fields=["priority", "-due_date"], name="priority_due_date_idx"
            ),
        ]

    def is_overdue(self):
        return not self.is_complete and timezone.now() > self.due_date

    def is_due_soon(self):
        return (
            not self.is_complete and timezone.now() + timedelta(days=7) >= self.due_date
        )

    def __str__(self):
        return f"{self.title} ({self.get_priority_display()}, Due: {self.due_date.strftime('%Y-%m-%d')})"


class Objective(GoalCommon):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} (Goal: {self.goal.title})"


class Plan(GoalCommon):
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} (Objective: {self.objective.title})"


class Assignment(GoalCommon):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    SOURCE_CHOICES = [
        (1, "Tutorial"),
        (2, "Article"),
        (3, "Video"),
        (4, "Book"),
        (5, "Course"),
        (6, "Lecture"),
        (7, "Lab"),
        (8, "Project"),
        (9, "Exam"),
        (10, "Other"),
    ]
    source_type = models.IntegerField(choices=SOURCE_CHOICES, default=10)
    PROGRESS_CHOICES = [
        (1, "Not Started"),
        (2, "In Progress"),
        (3, "Completed"),
        (4, "Reviewed"),
    ]
    progress = models.IntegerField(choices=PROGRESS_CHOICES, default=1)
    # tags = models.ManyToManyField('home.Topic', on_delete=models.SET_NULL, null=True, blank=True, db_table='assignment_tags')
    tags = models.ManyToManyField(Tag, blank=True)
    is_assimilated = models.BooleanField(
        "Clear understanding of content",
        default=False,
        help_text="Indicates whether the content is fully understood and assimilated.",
    )

    def __str__(self):
        return f"{self.title} (Plan: {self.plan.title}, Progress: {self.get_progress_display()})"
