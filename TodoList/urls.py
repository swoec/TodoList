"""eugra URL Configuration

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
from .settings import MEDIA_ROOT
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.urls import path
from user.views import UserViewset,UserView
from todolist.views import TodoListViewSet

router = DefaultRouter()
router.register(r'user', UserViewset, base_name='user')
router.register(r'todolist', TodoListViewSet, base_name='todolist')
router.register(r'users', UserView, base_name='user')
# router.register(r'auth', CustomBackend, base_name='CustomBackend')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', obtain_jwt_token),
    url(r'^', include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'docs/', include_docs_urls(title="online shop")),
    # url('', include('social_django.urls', namespace='social')),

]
