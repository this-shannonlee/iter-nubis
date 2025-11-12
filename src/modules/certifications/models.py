from django.db import models
from modules.home.models import Tag
from multiselectfield import MultiSelectField


class ExamDomainObjective(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class ExamDomain(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    min_weight_percentage = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        blank=True,
        null=True,
        help_text="Minimum weight percentage for this domain.",
    )
    max_weight_percentage = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        blank=True,
        null=True,
        help_text="Maximum weight percentage for this domain.",
    )

    def __str__(self):
        return self.title


class Exam(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    version = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    next_version_date = models.DateField(
        "New Version Release Date", null=True, blank=True
    )
    revision_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    guide = models.URLField("Exam Guide", blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration_minutes = models.IntegerField("Duration", null=True, blank=True)
    question_count = models.IntegerField(null=True, blank=True)
    QUESTION_FORMAT_CHOICES = [
        ("MC", "Multiple Choice"),
        ("TF", "True/False"),
        ("FILL", "Fill in the Blank"),
        ("ORDER", "Ordering"),
        ("MATCH", "Matching / Drag and Drop"),
        ("CASE", "Case Study"),
        ("SIM", "Simulation"),
        ("LAB", "Lab"),
        ("CODE", "Coding"),
        ("SHORTA", "Short Answer"),
        ("ESSAY", "Essay"),
        ("PBA", "Performance-Based Assessment"),
        ("PBQ", "Performance-Based Question"),
        ("ORAL", "Oral Exam"),
        ("OTHER", "Other"),
    ]
    question_format = MultiSelectField(choices=QUESTION_FORMAT_CHOICES, blank=True)
    passing_score = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    max_score = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    is_pass_fail = models.BooleanField("Pass/Fail", default=False)
    domains = models.ManyToManyField(ExamDomain, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title} [{self.code}]"


class Certification(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    prerequisites = models.ManyToManyField("self"), blank=True, symmetrical=False
    renewal_period_years = models.IntegerField(null=True, blank=True)
    exams = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
