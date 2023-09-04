from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rules.choices import TYPE
# Create your models here.


class Profile(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=12, choices=TYPE, default=TYPE[1][1])
    experience = models.FloatField(null=True, blank=True, default=0)
    salary = models.IntegerField(null=True)
    date_joined = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return f"user_id {self.user.id} profile_id {self.id}, username {self.user.username}"

