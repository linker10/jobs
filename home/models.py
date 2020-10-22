from django.db import models
from django.utils import timezone

from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/files')


# Create your models here.

class Personnel(models.Model):
    position_type = models.CharField(max_length=100)
    job_category = models.CharField(max_length=100)
    position_title = models.CharField(max_length=100)
    workplace = models.CharField(max_length=100)
    preferred_contact_method = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message_for_us = models.CharField(max_length=120)
    created = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.created = timezone.now()
        return super(Personnel, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, email: {self.email}'

    class Meta:
        verbose_name_plural = 'personnel'


class Cv(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    confirmpassword = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    confirmemail = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    cv = models.FileField(blank=True, null=True)
    canadanational = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.username)



