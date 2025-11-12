from django.db import models


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True)
    TAG_TYPE_CHOICES = [
        ("concept", "Concept"),
        ("tech", "Technology"),
        ("service", "Service"),
        ("product", "Product"),
        ("tool", "Tool"),
        ("platform", "Platform"),
        ("language", "Language"),
        ("library", "Library"),
        ("framework", "Framework"),
        ("database", "Database"),
        ("skill", "Skill"),
        ("certification", "Certification"),
        ("provider", "Provider"),
        ("other", "Other"),
    ]
    tag_type = models.CharField(
        max_length=20, choices=TAG_TYPE_CHOICES, default="other"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
