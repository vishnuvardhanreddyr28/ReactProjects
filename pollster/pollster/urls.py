
from django.contrib import admin
from django.urls import path,include
import polls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/',include('polls.urls'))
]
