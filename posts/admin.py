from django.contrib import admin

# Register your models here.
from posts.models import Posts

class PostsAdmin(admin.ModelAdmin):
	pass

admin.site.register(Posts, PostsAdmin)
