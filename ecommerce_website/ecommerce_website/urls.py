from django.contrib import admin
from django.urls import path,include
from core.views  import fontpage,about

urlpatterns = [
    path('', fontpage, name='fontpage'),  
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('', include('store.urls')), 
]