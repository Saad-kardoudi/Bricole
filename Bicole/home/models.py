from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    Available_choices = (
        ('Not Available', 'Not Available'),
        ('Available', 'Available'),
        ('Available form now', 'Available form now'))
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    adress = models.CharField(max_length=500)
    job = models.CharField(max_length=100, null=True)
    bio = models.CharField(max_length=500, null=True)
    Available = models.CharField(max_length=70, null=True,choices=Available_choices)
    Acc_pic = models.ImageField(default="image.jfif", null=True, blank=True)

    def _str_(self):
        return self.user.name


class Rating (models.Model):
    rate_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5))
    Worker = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='worker')
    employer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='employer')
    Comment = models.CharField(max_length=500)
    rate = models.IntegerField(choices=rate_choices)
    created_at = models.DateTimeField(auto_now_add=True)


class Hire_me (models.Model):
    Worker = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='worker_1')
    employer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='employer_1')
    Disciption = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Annoce (models.Model):
    employer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='employer_2')
    Disciption = models.CharField(max_length=500)
    job_titel = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
