from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin
from django_countries.fields import CountryField

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

# Custom User Manager
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, age, phone, country, state='default', city='default',
                    pincode='000000', local_address='default', gender='O',
                    date_of_birth='2000-01-01', password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            age=age,
            phone=phone,
            country=country,
            state=state,
            city=city,
            pincode=pincode,
            local_address=local_address,
            gender=gender,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            age=0,
            phone='0000000000',
            country='IN',  # default ISO country code
            state='default',
            city='default',
            pincode='000000',
            local_address='default',
            gender='O',
            date_of_birth='2000-01-01',
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom User Model
class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=15, default='0000000000')
    country = CountryField(blank_label='(select country)', default='IN')
    state = models.CharField(max_length=100, default='default')
    city = models.CharField(max_length=100, default='default')
    pincode = models.CharField(max_length=10, default='000000')
    local_address = models.TextField(default='default')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    date_of_birth = models.DateField(blank=True, null=True, default='2000-01-01')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']  # For createsuperuser command

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
