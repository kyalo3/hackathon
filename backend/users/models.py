from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator


USERNAME_REGEX  = '^[a-zA-Z0-9.+-]*$'

class CustomUser(AbstractBaseUser):
    
    FIELD_CHOICE = (
        ('Cattle&Products', 'Cattle&Products'),
        ('Sheep&Products', 'Sheep&Products'),
        ('Pig&Products', 'Pig&Products'),
        ('Poultry&Products', 'Poultry&Products'),
        ('Others', 'Others'),
        ('Vegetables', 'Vegetable'),
        ('Fruits', 'Fruits'),
    )

    username = models.CharField(
        max_length=300,
        validators=[
            RegexValidator(regex=USERNAME_REGEX,
                           message='Username must be alphanumeric or contain numbers',
                           code='invalid_username'
                           )],
        unique=True
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    group = models.CharField(verbose_name='Select A Group', max_length=100, choices=FIELD_CHOICE)
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'group']

    def __str__(self):
        return self.username

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Does the user have permissions to view the app `app_label`?
        # Simplest possible answer: Yes, always
        return True


class Profile(models.Model):
    user            = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name      = models.CharField(verbose_name="name", max_length=20)
    last_name       = models.CharField(verbose_name="surname", max_length=20)
    user_info		= models.TextField(verbose_name='About Farmer', blank=True)
    image           = models.ImageField(default='default.jpg', upload_to='profile_pics')
    country         = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.user} Profile'

