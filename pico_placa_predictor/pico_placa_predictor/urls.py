"""pico_placa_predictor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from pico_placa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^predictor/(?P<licenseplate>[A-Z]{3}[0-9]{4})/$', PicoPlacaPredictorView.as_view(), name="predictor"),
    #re_path(r'^date/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})$', views.day_archive)
    #(?P<year>[0-9]{4})
    #[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}Z
    #/(?P<datetime>.*)

]
