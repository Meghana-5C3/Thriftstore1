from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    role = models.CharField(max_length=10, choices=[('buyer', 'Buyer'), ('seller', 'Seller')], default='buyer')
    bio = models.TextField(blank=True)   
    def __str__(self):
        return f"{self.user.username} Profile"

# Automatically create or update user profile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
