from django.conf import settings
from django.conf.urls.static import static
from django.core.checks import Debug
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.drive, name='drive'),
    path('upload/', views.upload, name='upload'),
    path('<uuid:uuid>/', views.details_view, name='details'),
    path('<uuid:uuid>/share', views.share_file, name='share'),
    path('<uuid:uuid>/<int:id>', views.delete_comment, name='deletecomment'),
    path('<uuid:uuid>/<int:id>/edit', views.edit_comment, name='editcomment'),
]