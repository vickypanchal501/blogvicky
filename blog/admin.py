from django.contrib import admin
from blog.models import Tag,Post

# Register your models here.
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ["title","created_at","modified_at"]


admin.site.register(Post, PostAdmin)