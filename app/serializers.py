from rest_framework import serializers

from .models import Profile, Skill


class SkillSerializer(serializers.ModelSerializer):
    """
    Slug here is listed as a read only field,
    because i want the automated signal to do the job for me
    this is mostly just fo my fun, and not something you're required to do
    """

    class Meta:
        model = Skill
        fields = ["name", "slug"]
        read_only_fields = ["slug"]


class ProfileSerializer(serializers.ModelSerializer):
    """
    the user profile specifies an override for the skills reference
    this is to replace a primary key related fiield (the defaul from the model serializer
    with a slug related field, so we can specify skill by the slug
    """

    skills = serializers.SlugRelatedField(
        slug_field="slug", queryset=Skill.objects.all(), many=True
    )

    class Meta:
        model = Profile
        fields = "__all__"
