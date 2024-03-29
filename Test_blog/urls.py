"""Test_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # 主页路径
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),  # 配置上传url
    path('myblog/', include('myblog.urls')),  # 博客app路径
    path('login/', views.login, name='login'),  # 登
]
# 设置ckeditor的上传
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
