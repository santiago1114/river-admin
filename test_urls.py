from django.urls import re_path, include
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include("river_admin.urls")),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]
