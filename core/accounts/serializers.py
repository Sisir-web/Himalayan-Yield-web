
# account/serializers.py
from rest_framework import serializers
from .models import MyUser
from django_countries.fields import CountryField
from django_countries.serializer_fields import CountryField as CountrySerializerField

class UserSerializer(serializers.ModelSerializer):
    country = CountrySerializerField(name_only=True)

    class Meta:
        model = MyUser
        fields = ['id', 'email', 'name', 'age', 'phone', 'country', 'state', 'city', 'pincode', 'local_address', 'gender', 'date_of_birth']
        read_only_fields = ['id']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True,label='Confirm Password')

    country = CountrySerializerField()

    class Meta:
        model = MyUser
        fields = ['email', 'name', 'age', 'phone', 'country', 'state', 'city', 'pincode', 'local_address', 'gender', 'date_of_birth', 'password', 'password2']

      #   extra_krawgs={ 'password2': {'label': 'Confirm Password'},}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = MyUser.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    class Meta:
        model=MyUser
        fileds=['email','password']
