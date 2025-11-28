
from django.db import models
from django.contrib.auth.models import User


class Interest(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    ROLE_CHOICES = (
        ("developer", "Developer"),
        ("investor", "Investor"),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )

    # Basic fields
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)

    # Additional
    interests = models.ManyToManyField(Interest, blank=True, related_name="profiles")

    # Optional useful fields (general)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role})"








class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    uploader = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    video_file = models.FileField(upload_to="posts/videos/")
    description = models.TextField(blank=True, null=True)

    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.uploader.name}"