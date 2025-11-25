from django.contrib import admin

# Register your models here.
from .models import Certification, Exam, ExamDomain, ExamDomainObjective

admin.site.register(Certification)
admin.site.register(Exam)
admin.site.register(ExamDomain)
admin.site.register(ExamDomainObjective)
