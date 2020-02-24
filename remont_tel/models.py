from django.db import models

# Create your models here.
class Category(models.Model):
        name = models.CharField('Название категории', max_length=120)
        slug = models.SlugField('URL', max_length=120)
        text = models.TextField('Текст категории')
        banner = models.ImageField('Баннер', upload_to='images/', blank=True, null=True)
        title = models.CharField('Title', max_length=120)
        description = models.CharField('Description', max_length=250)
        keywords = models.CharField('Keywords', max_length=250)
