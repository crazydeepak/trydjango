from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=120)

    # def get_absolute_url(self):
    #     return reverse("courses:course-update", kwargs={"id": self.id})
