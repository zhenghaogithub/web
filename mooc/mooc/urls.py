"""mooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import xadmin
from django.urls import path
from django.conf.urls import include, url
from django.views.static import serve

from mooc.settings import  STATIC_ROOT#用于生产环境
from mooc.settings import  MEDIA_ROOT#用于生产环境
from mooc.settings import  MEDIA_URL


urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls), #这里使用xadmin来管理后台，替换原有的admin
    url(r'^captcha/', include('captcha.urls')), #生成验证码
    url(r'^ueditor/', include('DjangoUeditor.urls')),  # 富文本url

    url(r'^', include('users.urls'), name="users"), #用户登录注册相关urls
    url(r'^', include('organization.urls'), name="organization"),  # 授课机构urls
    url(r'^', include('courses.urls'), name="courses"),  # 公开课url


    url(r'^Media/(?P<path>.*)$', serve, { 'document_root':MEDIA_ROOT }), #配置在生产环境下的图片不能访问的问题
]
