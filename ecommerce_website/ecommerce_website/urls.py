# pro/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import fontpage, about

urlpatterns = [
    path('', include('store.urls')),  # Include store URLs
    path('', fontpage, name='fontpage'),  # Main page
    path('about/', about, name='about'),   # About page
    path('admin/', admin.site.urls),        # Admin panel
]