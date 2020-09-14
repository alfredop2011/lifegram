
from django.contrib import admin
from django.urls import path
from lifegram import view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', view.hello_World),
    path('sorted/', view.sorted_ints),
    path('hi/<str:name>/<int:age>/', view.say_hi),

]

