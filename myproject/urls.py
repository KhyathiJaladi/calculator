from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('mlprojects.urls')),
    #path('',include('datas.urls')),
    path('',include('calculator.urls')),
    #path('',include('myapp.urls')),
    #path('',include('braintumordp.urls')),
]
