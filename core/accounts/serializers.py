
# account/serializers.py
# from rest_framework import serializers
# from .models import MyUser
# from django_countries.fields import CountryField
# from django_countries.serializer_fields import CountryField as CountrySerializerField

# class UserSerializer(serializers.ModelSerializer):
#     country = CountrySerializerField(name_only=True)

#     class Meta:
#         model = MyUser
#         fields = ['id', 'email', 'name', 'age', 'phone', 'country', 'state', 'city', 'pincode', 'local_address', 'gender', 'date_of_birth']
#         read_only_fields = ['id']

# # class RegisterSerializer(serializers.ModelSerializer):
# #     password = serializers.CharField(write_only=True)
# #     password2 = serializers.CharField(write_only=True,label='Confirm Password')

# #     country = CountrySerializerField(required=False, allow_null=True)

# #     class Meta:
# #         model = MyUser
# #         fields = ['email', 'name', 'age', 'phone', 'country', 'state', 'city', 'pincode', 'local_address', 'gender', 'date_of_birth', 'password', 'password2']

# #       #   extra_krawgs={ 'password2': {'label': 'Confirm Password'},}
# #         extra_kwargs ={
# #               'country':{'required': False},
# #              'date_of_birth':{'required':False,'allow_null':True}          }

# #     def validate(self, attrs):
# #         if attrs['password'] != attrs['password2']:
# #             raise serializers.ValidationError({"password": "Passwords must match."})
# #         return attrs

# #     def create(self, validated_data):
# #         validated_data.pop('password2')
# #         user = MyUser.objects.create_user(**validated_data)
# #         return user
    
# class RegisterSerializer(serializers.ModelSerializer):
#     user_name = serializers.CharField(source='username')  # maps to User.username
#     full_name = serializers.CharField(required=True)
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(write_only=True)
#     city = serializers.CharField(required=False, allow_blank=True)
#     state = serializers.CharField(required=False, allow_blank=True)
#     address = serializers.CharField(required=False, allow_blank=True)
#     phone = serializers.CharField(required=False, allow_blank=True)

#     class Meta:
#         model = MyUser
#         fields = ['user_name', 'full_name', 'email', 'password', 'city', 'state', 'address', 'phone']

#     def create(self, validated_data):
#         # Extract username & full_name
#         username = validated_data.pop('username')
#         full_name = validated_data.pop('full_name')

#         user = MyUser.objects.create_user(
#             username=username,
#             email=validated_data['email'],
#             password=validated_data['password']
#         )

#         # Store other info (e.g., in User model fields or in a profile model)
#         user.first_name = full_name
#         user.save()

#         return user
# account/serializers.py
from rest_framework import serializers
from .models import MyUser

class RegisterSerializer(serializers.ModelSerializer):
    # Accept either "user_name" or "username" from frontend
    user_name = serializers.CharField(required=False, allow_blank=True)
    username = serializers.CharField(required=False, allow_blank=True)
    full_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    city = serializers.CharField(required=False, allow_blank=True)
    state = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = MyUser
        fields = [
            'user_name',
            'username',
            'full_name',
            'email',
            'password',
            'city',
            'state',
            'address',
            'phone'
        ]

    def create(self, validated_data):
        # Try to get username from either key
        username = validated_data.pop('user_name', '') or validated_data.pop('username', '')
        if not username:
            raise serializers.ValidationError({'user_name': 'Username is required.'})

        full_name = validated_data.pop('full_name')
        email = validated_data.get('email')
        password = validated_data.get('password')
        city = validated_data.get('city', '')
        state = validated_data.get('state', '')
        address = validated_data.get('address', '')
        phone = validated_data.get('phone', '')

        user = MyUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            name=full_name,
            age=0,
            phone=phone,
            country='IN',
            state=state,
            city=city,
            pincode='000000',
            local_address=address,
            gender='O',
            date_of_birth='2000-01-01'
        )
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['email', 'password']
