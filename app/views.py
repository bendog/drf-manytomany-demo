from django.shortcuts import render
from rest_framework import generics

from .models import Profile, Skill
from .serializers import ProfileSerializer, SkillSerializer

# Create your views here.


class ProfileListView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class SkillListView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
