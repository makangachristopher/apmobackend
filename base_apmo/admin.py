from django.contrib import admin
from .models import Category, Preacher, Playlist, Sermon
# Register your models here.

admin.site.register(Category)
admin.site.register(Preacher)
admin.site.register(Playlist)
admin.site.register(Sermon)