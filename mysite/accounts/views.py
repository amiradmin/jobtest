from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from django.core import serializers
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
# Create your views here.



class UserProfile(viewsets.ModelViewSet):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def list(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        university = request.data['university']
        city = request.data['city']
        country = request.data['country']
        phone = request.data['phone']
        cell_phone = request.data['cell_phone']
        birth_date = request.data['birth_date']
        avatar = request.data['avatar']

        user = User()

        user.username = username
        user.set_password (password)
        user.email = email
        user.save()
        user.refresh_from_db()
        user.profile.university = university
        user.profile.city = city
        user.profile.country = country
        user.profile.phone = phone
        user.profile.cell_phone = cell_phone
        user.profile.birth_date = birth_date
        user.profile.avatar = avatar
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.profile.save()
        print(username)
        print(email)

        return Response('Account created')

    def update(self, request, pk):
        print('OK')
        user = User.objects.get(pk=pk)
        # user.username = request.data['username']
        user.set_password(request.data['password'])
        user.email = request.data['email']
        user.profile.university = request.data['university']
        user.profile.city = request.data['city']
        user.profile.country = request.data['country']
        user.profile.phone = request.data['phone']
        user.profile.cell_phone = request.data['cell_phone']
        user.profile.birth_date = request.data['birth_date']
        user.profile.avatar = request.data['avatar']
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        print(user.username)

        return Response('Account updated')
