from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import SermonListView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path("signup/", views.signup, name="signup"),
    path("categories/", views.categories, name="categories"),
    path('sermons/create-category', views.createCategory, name='create_category'),
    path('sermons/create-preacher', views.createPreacher, name='create_preacher'),
    path('sermons/create-playlist', views.createPlaylist, name='create_playlist'),
    path('sermons/create-sermons', views.createSermon, name='create_sermon'),
    path('sermons/edit-category/<str:pk>/', views.editCategory, name='edit_category'),
    path('sermons/delete-category/<str:pk>/', views.deleteCategory, name='delete_category'),
    path('sermons/edit-preacher/<str:pk>/', views.editPreacher, name='edit_preacher'),
    path('sermons/delete-preacher/<str:pk>/', views.deletePreacher, name='delete_preacher'),
    path('sermons/edit-playlist/<str:pk>/', views.editPlaylist, name='edit_playlist'),
    path('sermons/delete-playlist/<str:pk>/', views.deletePlaylist, name='delete_playlist'),
    path('sermons/edit-sermon/<str:pk>/', views.editSermon, name='edit_sermon'),
    path('sermons/delete-sermon/<str:pk>/', views.deleteSermon, name='delete_sermon'),


    # Api Urls
    path('api/sermons/', SermonListView.as_view(), name='sermon-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)