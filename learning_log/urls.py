"""learning_log URL Configuration

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

### LEARNING LOG URLS

from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
#from django.conf.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('learning_logs/', include('learning_logs.urls')),  # , namespace='learning_logs'
]

#the site you are redirected to if you type 127.0.0.1:8000/
urlpatterns += [
    path('', RedirectView.as_view(url='/learning_logs/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)