from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monitoring_app.urls'))
]