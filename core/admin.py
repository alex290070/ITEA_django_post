from django.contrib import admin
from core.models import Posts, Comments

# Register your models here.


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'comment', 'public_date')
#    list_display_links = ('title', 'comment')

admin.site.register(Posts)
