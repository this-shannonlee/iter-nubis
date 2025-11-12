from django.contrib import admin

# Register your models here.
from .models import Certification, Exam, ExamDomain

admin.site.register(Certification)
admin.site.register(Exam)
admin.site.register(ExamDomain)
