"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from webapp.views import index_goods_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_goods_view, name='index'),
    # path('good/add/', good_create_view, name='good_add'),
    # path('good/<int:pk>', single_good_view, name='good_view'),
    # path('good/<int:pk>/edit/', good_update_view, name='good_update'),
    # path('good/<int:pk>/delete/', good_delete_view, name='good_delete')
    # path('good/<category>', good_category_view, name='category_view'),
]
