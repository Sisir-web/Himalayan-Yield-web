from rest_framework import serializers
from core.models import CustomUser
from django.contrib.auth.password_validation import validate_password

class ButtonSerializer(serializers.Serializer):
   label = serializers.CharField()
   url = serializers.CharField()

class HomePageSerializer(serializers.Serializer):
   intro_title = serializers.CharField()
   intro_text = serializers.CharField()
   buttons = serializers.CharField()

class SignupSerializer(serializers.Serializer):
   password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
   class Meta:
      model = CustomUser
      fields = ['id','username','fullname','city','phone','address','password']

   def create(self, validated_data):
      user = CustomUser.objects.create_user(
         username=validated_data('username',''),
         fullname=validated_data('fullname',''),
         city=validated_data('city',''),
         phone=validated_data('phone',''),
         address=validated_data('address',''),
         password=validated_data['password']
      )
      return user