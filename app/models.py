from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify as django_slugify

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    skills = models.ManyToManyField(Skill, related_name="profiles")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@receiver(pre_save, sender=Skill)
def validate_slug(sender, instance, **kwargs):
    instance.slug = django_slugify(instance.name)
