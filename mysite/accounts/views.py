from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from django.core import serializers
from rest_framework.response import Response
from .models import Profile,ClinicProfile
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from accounts.forms import InsertUser,InsertClinicUser
from django.views.generic import TemplateView
from booking.models import Queues
from clinics.models import Clinics

# Create your views here.



class Userprofiler(TemplateView):
    template_name = "accounts/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # .filter(user = self.request.user)
        booking_list =Queues.objects.select_related('clinic').filter(user =self.request.user )
        # booking_list = booking_list.objects.filter(user_id = 13)
        context['booking_list'] = booking_list

        return context


class ClinicProfiler(TemplateView):
    template_name = "accounts/clinic_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # .filter(user = self.request.user)
        booking_list =Queues.objects.select_related('clinic').filter(user =self.request.user )
        # booking_list = booking_list.objects.filter(user_id = 13)
        context['booking_list'] = booking_list

        return context


class NewUser(TemplateView):
    template_name = "accounts/user_signup.html"

    def get_context_data(self):
        context = super(NewUser, self).get_context_data()
        form = InsertUser()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        print('Post')
        form = InsertUser(self.request.POST,self.request.FILES)
        # clinic_list =Clinics.objects.all()
        # user_obj = Profile()
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        cell_phone = request.POST['cell_phone']
        birth_date = request.POST['birth_date']
        # avatar = request.FILES['avatar']

        user = User()
        user.username = username
        user.set_password (password)
        user.email = email
        user.save()
        user.refresh_from_db()
        user.profile.phone = phone
        user.profile.cell_phone = cell_phone
        user.profile.birth_date = birth_date
        # user.profile.avatar = avatar
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.profile.save()

        return render(request,'index.html',{})


class NewClinicUser(TemplateView):
    template_name = "accounts/clinic_signup.html"

    def get_context_data(self):

        context = super(NewClinicUser, self).get_context_data()
        form = InsertClinicUser()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        print('Post')
        form = InsertClinicUser(self.request.POST,self.request.FILES)
        # clinic_list =Clinics.objects.all()
        # user_obj = ClinicProfile()
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']
        name = request.POST['name']
        birth_date = request.POST['birth_date']
        # avatar = request.FILES['avatar']
        #
        user = User()
        user.username = username
        user.set_password (password)
        user.email = email
        user.save()
        user.refresh_from_db()
        user.clinicprofile.phone = phone
        user.clinicprofile.name = name
        user.clinicprofile.birth_date = birth_date
        # user.clinicprofile.avatar = avatar
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.clinicprofile.save()

        return render(request,'index.html',{})

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
