# serializers.py
from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields = ('username','password','email','phone','cell_phone','birth_date','avatar')
