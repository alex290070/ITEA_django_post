from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(verbose_name='Title of post', max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    image = models.ImageField(verbose_name='Picture', upload_to='img', null=True, blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    public_date = models.DateTimeField(verbose_name='date of publication', default=timezone.now)
    public = models.BooleanField(verbose_name='Published', default=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

    @property
    def short_description(self):
        return self.description[:20] + '...' if len(self.description) > 20 else self.description

    def get_absolute_url(self):
        return reverse('core:post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = None
        super().save(*args, **kwargs)


class Comment(models.Model):
    title = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)
    author = models.CharField(verbose_name='Author of post', max_length=255, blank=False)
    comment = models.TextField(verbose_name='Text of comment', blank=False)
    public_date = models.DateTimeField(verbose_name='date of publication', default=timezone.now)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('core:comments', kwargs={'slug': self.post.slug, 'pk': self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

