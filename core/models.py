from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
from autoslug import AutoSlugField

# Create your models here.


class Posts(models.Model):

    title = models.CharField(
        verbose_name='Title of post',
        max_length=255
    )

    slug = AutoSlugField(
        populate_from='title',
        unique=True,
        null=True
    )

    image = models.ImageField(
        verbose_name='Picture',
        upload_to='comment',
        null=True,
        blank=True
    )

    description = models.TextField(
        verbose_name='Description',
        blank=True
    )

    public_date = models.DateTimeField(
        verbose_name='date of publication',
        default=timezone.now
        #auto_now=True
    )

    show = models.BooleanField(
        verbose_name='show?',
        default=True
    )

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    @property
    def short_description(self):
        return self.description[:20] + '...' if len(self.description) > 20 else self.description

    def get_absolute_url(self):
        return reverse('core:posts', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = None
        super().save(*args, **kwargs)


class Comments(models.Model):

    title = models.ForeignKey(
        Posts,
        verbose_name='Post',
        on_delete=models.CASCADE
    )

    author = models.CharField(
        verbose_name='Author of post',
        max_length=255,
        blank=False

    )

    comment = models.TextField(
        verbose_name='Text of comment',
        blank=False
    )

    public_date = models.DateTimeField(
        verbose_name='date of publication',
        default=timezone.now
        #auto_now=True
    )

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('core:comments', kwargs={'slug': self.posts.slug, 'pk': self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

