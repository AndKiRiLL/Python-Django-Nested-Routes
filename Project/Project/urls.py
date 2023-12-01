"""
URL configuration for Project project.

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
from django.urls import path, include

# product_patterns = [
    # path("", views.products),
    # path("new", views.new),
    # path("top", views.top),
    # path("comments", views.comments),
    # path("questions", views.questions),
# ]

urlpatterns = [
    # path("", views.index),
    # path("products/<int:id>/", include(product_patterns)),
    # path("user/", views.user)
    # path("about/", views.about),
    # path("contact/", views.contact),
    # path("details/", views.details),
    # path("index/<int:id>", views.index),
    # path("access/<int:age>", views.access),
    # path("", views.index)
    path("set", views.set),
    path("get", views.get),
]
