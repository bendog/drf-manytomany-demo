from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify as django_slugify

# Create your models here.


class Skill(models.Model):
    """the skill is used to track skills a profile may have, the slug field is a text based reference"""

    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    """this is a user profile, i'm using this to avoid having to create a user app, you'd use your AbstractUser here"""

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    skills = models.ManyToManyField(Skill, related_name="profiles")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@receiver(pre_save, sender=Skill)
def validate_slug(sender, instance, **kwargs):
    """
    this validate slug process will automatically create a slug version of name of the skill
    this is entirely for my enjoyment and is not essential.
    """
    instance.slug = django_slugify(instance.name)
