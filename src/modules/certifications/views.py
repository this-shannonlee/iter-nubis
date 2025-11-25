from django.shortcuts import render

from modules.certifications.models import Certification, Exam


# Create your views here.
def index(request):
    certifications = Certification.objects.all()
    context = {"certification_list": certifications}
    return render(request, "certifications/index.html", context)


def certification_detail(request, certification_id):
    certification = Certification.objects.get(id=certification_id)
    exam_set = certification.exam_set.all()
    print(exam_set)
    exam_list = Exam.objects.filter(certification_id=certification_id)
    print(exam_list)
    context = {"certification": certification, "exam_list": exam_list}
    return render(request, "certifications/detail.html", context)


5
5
