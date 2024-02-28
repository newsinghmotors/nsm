from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# for image compression
from io import BytesIO
from PIL import Image
from django.core.files import File

#image compression method
def compress(image):
    im = Image.open(image)
    im = im.convert('RGB')
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image

class Keys(models.Model):
    name = models.CharField(max_length=255)
    saran = models.IntegerField(blank=False,default=0)
    minda = models.IntegerField(blank=False,default=0)
    madin = models.IntegerField(blank=False,default=0)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Update the date field to the current timestamp before saving
        self.date = timezone.now()
        super(Keys, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('key-detail', kwargs={'pk': self.pk})
