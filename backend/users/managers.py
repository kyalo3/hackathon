from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email,  group, password=None):
        if not username:
            raise ValueError('user must have a username')
        if not email:
            raise ValueError(_('The Email field must be set'))
        if not group:
            raise ValueError('Users must have a group choice')


        user = self.model(
            username = username, 
            email    = email,
            group    = group, 
                )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, password=None, group=None, **extra_fields):
        # Set default values for group
        group = None if group is None else group

        # Create a superuser with the provided parameters and default values
        user = self.create_user(
            username=username,
            email=email,
            group=group,
            password=password,
            **extra_fields
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
