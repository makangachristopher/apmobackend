from django.contrib import admin
from .models import Category, Preacher, Playlist, Sermon, Events, Download, Bookmark, Favourite, Devotion
# Register your models here.

admin.site.register(Category)
admin.site.register(Preacher)
admin.site.register(Playlist)
admin.site.register(Sermon)
admin.site.register(Events)
admin.site.register(Download)
admin.site.register(Favourite)
admin.site.register(Bookmark)
admin.site.register(Devotion)