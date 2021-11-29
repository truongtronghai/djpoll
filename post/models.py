from django.db import models
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    # content = models.TextField()
    content = RichTextUploadingField()
    feature_image = models.ImageField(null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    # using for showing images in admin page
    def image_tag(self):
        return format_html("<img alt='%s' src='%s' width='150px'>" % (self.title, self.feature_image.url))
