"""
URL configuration for wifimemory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    wifimemory. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    wifimemory. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    wifimemory. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import home
from .views import ip_address
from .views import wifi_scanner
from .views import wifi_signal

urlpatterns = [
    path('home/', home, name='home'),
    path('myip/', ip_address, name='ip'),
    path('wifi_scan/', wifi_scanner, name='wifi-scan'),
    path('wifi_signal/', wifi_signal, name='wifi-signal'),
]
