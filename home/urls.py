"""homework URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from home import views
from homework import settings

app_name = 'home'

urlpatterns = [
    path('', views.index, name='main'),
    path('lecture', views.lecture, name='lecture'),
    path('lectureSearch',views.lectureSearch, name="lectureSearch"),
    path('lecturePost', views.lecturePost, name='lecturePost'),
    path('lectureDetail/<int:l_id>', views.lectureDetail, name='lectureDetail'),
    path('lectureComment', views.lectureComment, name='lectureComment'),

    path('market', views.market, name='market'),
    path('marketPost', views.marketPost, name='marketPost'),
    path('marketDetail/<int:l_id>', views.marketDetail, name='marketDetail'),
    path('marketComment', views.lectureComment, name='marketComment'),

    path('free', views.free, name='free'),
    path('freePost', views.freePost, name='freePost'),
    path('freeDetail/<int:l_id>', views.freeDetail, name='freeDetail'),
    path('freeComment', views.lectureComment, name='freeComment'),

    path('register', views.register, name='register'),
    path('login', views.signin, name='signin'),
    path('logout', views.signout, name='signout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)