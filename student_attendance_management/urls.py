"""student_attendance_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from attendance_app.api.views import GetFingerId

urlpatterns = [
    path('chat/', include('attendance_app.urls')),
    path('admin/', admin.site.urls),
    path('attendance-management/api/', include('users.api.urls')),
    path('attendance-management/api/', include('university_app.api.urls')),
    path('attendance-management/api/', include('attendance_app.api.urls')),
    path('attendance-management/api/', include('course_app.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('finger/', GetFingerId.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
