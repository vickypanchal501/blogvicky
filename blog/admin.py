from re import search
from django.contrib import admin
from blog.models import Tag,Post

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    search_fields = ("value",)

admin.site.register(Tag,TagAdmin)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ["title","created_at","modified_at"]
    search_fields = ("title",)


admin.site.register(Post, PostAdmin)