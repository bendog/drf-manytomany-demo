from rest_framework import serializers

from .models import Profile, Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name", "slug"]
        read_only_fields = ["slug"]


class ProfileSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        slug_field="slug", queryset=Skill.objects.all(), many=True
    )

    class Meta:
        model = Profile
        fields = "__all__"
