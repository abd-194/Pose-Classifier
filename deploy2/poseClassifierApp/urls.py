from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('yogaPose.urls')),
    # path('', include('yogaPose.routing')),
    path('', include('Demo.urls')),
    path("admin/", admin.site.urls),
]