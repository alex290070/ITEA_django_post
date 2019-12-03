from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import MyUserManager
#from .tasks import send_mail_task


class MyUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=128, unique=True, blank=True)
    real_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=128, unique=True, db_index=True)
    phone = models.CharField(max_length=12, blank=True,)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = MyUserManager()

    #USERNAME_FIELD = 'login'
    #REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    class Meta:
        verbose_name = 'my user'
        verbose_name_plural = 'my users'

    @property
    def get_full_name(self):
        return '{} {}'.format(self.name.title(), self.surname.title())

    @property
    def get_short_name(self):
        return self.name

#    def send_user_mail(self, subject, message):
#        send_mail_task.delay(subject, message, self.email)
