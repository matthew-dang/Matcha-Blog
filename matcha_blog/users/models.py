from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # create a user that has a one to one relationship, meaning one user can have one profile and one profile is associated with one user
    # CASCADE means that if user is deleted, also delete profile, but if profile is deleted, user is not deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)