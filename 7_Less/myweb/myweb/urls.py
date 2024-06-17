
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
        return HttpResponse("<h1>Super Home Page</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

]
