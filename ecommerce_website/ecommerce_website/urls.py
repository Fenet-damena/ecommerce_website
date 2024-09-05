from django.contrib import admin
from django.urls import path
from core.views  import fontpage,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about,name='about'),
    path('',fontpage, name='fontpage')
]
