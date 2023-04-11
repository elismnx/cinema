from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from kinoapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('categories/', categories, name='categories'),
    path('anime-details/', anime_details, name='anime_details'),
    path('anime-watching/', anime_watching, name='anime_watching'),
    path('blog_details/', blog_details, name='blog_details'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)