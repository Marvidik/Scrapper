"""WonderScraper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from user import views as uviews
from web import views as wviews 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",uviews.registration_login,name="reglog"),
    path("home/",wviews.home,name="home"),
    path("dashboard/",wviews.dashboard,name="dashboard"),
    path("error/",wviews.error,name="error"),
    path("records/",wviews.tables,name="records"),
    path("remotes/",wviews.remote_table,name="rem"),
    path("first/",wviews.first_table,name="ft"),
    path("second/",wviews.second_table,name="st"),
    path("third/",wviews.third_table,name="tt"),
    path("dashboard/scrape",wviews.fake,name="fake"),
    path("dashboard/remote",wviews.remote,name="remote"),
    path("dashboard/first",wviews.first,name="first"),
    path("dashboard/second",wviews.second,name="second"),
    path("dashboard/third",wviews.third,name="third"),
    path("dashboard/add_message/",wviews.message,name="message"),
    path("dashboard/add_note/",wviews.note,name="note"),
    path("add_user/",uviews.add_user,name="add_user"),
    path("user_login/",uviews.user_login,name="login"),
    path("user_logout/",uviews.user_logout,name="logout"),
    path("home/add_contact/",wviews.contact,name="add_contact"),
    path("home/news/",wviews.newslater,name="news"),
    path('delete/<str:id>/',wviews.delete,name='delete'),
    path('remotes/delete/<str:id>/',wviews.remote_delete,name='remote_delete'),
    path('notes/delete/<str:id>/',wviews.note_delete,name='dnote'),
    path('export/',wviews.csvexport,name="export"),
    path('fexport/',wviews.firstcsv,name="fexport"),
    path('sexport/',wviews.secondcsv,name="sexport"),
    path('texport/',wviews.thirdcsv,name="texport"),
    
]
