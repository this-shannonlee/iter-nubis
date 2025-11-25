from django.urls import path

from . import views

app_name = "certifications"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:certification_id>/", views.certification_detail, name="certification_detail"),
]