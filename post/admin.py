from django.contrib import admin
from post.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        'title',
        'slug',
        'pub_date',
        'image_tag'
    )


# Register your models here.
admin.site.register(Post, PostAdmin)
