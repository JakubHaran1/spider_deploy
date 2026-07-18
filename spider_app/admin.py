from django.contrib import admin
from .models import User, Tag, Spider_img, Spider


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

# dodać related name


class SpiderImgAdmin(admin.ModelAdmin):
    list_display = ["spider__author__username", "spider__name"]


class SpiderAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "author__username"]


admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Spider_img, SpiderImgAdmin)
admin.site.register(Spider, SpiderAdmin)
