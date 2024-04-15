from django.db import models
from django_quill.fields import QuillField

# Create your models here.


class SingletonModel(models.Model):

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Information(SingletonModel):
    seo_content = models.CharField(max_length=255, default=None)
    slogan = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class About(SingletonModel):
    title = models.CharField(max_length=255)
    content = QuillField()

    def __str__(self):
        return self.title


class Footer(SingletonModel):
    title = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    address = models.CharField(max_length=255, default=None)
    address_caption = models.CharField(max_length=255, default=None)
    email = models.EmailField(default=None)
    email_caption = models.CharField(max_length=255, default=None)
    phone = models.CharField(max_length=20, default=None)
    phone_caption = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.title


class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    icon_image = models.ImageField(upload_to='store/images', null=True, blank=True)
    url = models.URLField()
    footer = models.ForeignKey(Footer, on_delete=models.PROTECT, null=True, blank=True, related_name='social_medias')
    call = models.ForeignKey('Call', on_delete=models.PROTECT, null=True, blank=True, related_name='social_medias')

    def __str__(self):
        return self.name


class Call(SingletonModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



