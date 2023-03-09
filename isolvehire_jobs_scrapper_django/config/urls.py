"""isolvehire_jobs_scrapper_django URL Configuration

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
from jobs_board_scrapper_app.views import sync_db_view, JobsView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("sync-db/", sync_db_view, name='sync_db'),
    path("", JobsView.as_view(), name='home'),
]
