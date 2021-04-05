from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
admin.site.site_header = "meet first django website"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to my website"
