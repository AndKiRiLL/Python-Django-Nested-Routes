"""
URL configuration for Homework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from App import views
from django.urls import path, include, re_path

posts_patterns = [
    path("popular", views.popular),
    path("new", views.new),
    path("allposts", views.all_posts),
    ]

urlpatterns = [

    path("", views.index),
    path("posts/", include(posts_patterns)),
    path("about/", views.about),
    path("contacts/", views.contacts),
    path("error", views.error),
    path('access/', views.access),
    path('access/<str:login>/', views.access),
    path('access/<str:login>/<str:password>/', views.access),
    path("posts/likesandcom/<int:post>", views.get_likes_com),
    path('json/', views.js_file),
    path('json/<str:name>/', views.js_file),
    path('json/<str:name>/<int:age>/', views.js_file),
    path('set', views.set),
    path('get', views.get),
]
