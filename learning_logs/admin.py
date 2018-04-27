from django.contrib import admin

# Register your models here.
from learning_logs.models import Groups, Post
admin.site.register(Groups)
admin.site.register(Post)
