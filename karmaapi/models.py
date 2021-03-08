from django.db import models


class Profile(models.Model):
    user = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=150,editable=False)
    mobile_no=models.IntegerField(unique=True)
    alternate_mobileno=models.IntegerField(unique=True)
    address=models.CharField(max_length=150,editable=True)

