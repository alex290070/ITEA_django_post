from django.contrib import admin
from core.models import Post, Comment

# Register your models here.


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'comment', 'public_date')
    list_display_links = ('title', 'comment')

admin.site.register(Post)
