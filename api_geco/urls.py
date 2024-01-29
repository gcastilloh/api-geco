from django.urls import path
from django.urls import include

urlpatterns = [
    path('api/v0.1/', include('api.urls')),
]
