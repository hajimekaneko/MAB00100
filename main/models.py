import uuid
from django.db import models
from django.db.models.fields.related import ForeignKey


class Auth(models.Model):

    class Meta:
        db_table = 'auth'

    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email', max_length=20)
    password = models.CharField(verbose_name='password', max_length=20, null=True, blank=True)
    token = models.CharField(verbose_name='token', max_length=20, null=True, blank=True)

    def __str__(self):
        return self.email
