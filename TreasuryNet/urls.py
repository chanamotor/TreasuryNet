from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('department.urls')),
    path('finance/', include('finance.urls')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    
]