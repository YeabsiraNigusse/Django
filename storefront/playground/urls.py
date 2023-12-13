from django.urls import path
from . import views

# we add this file to respond for a request for http://127.0.0.1:8000/playground/hello

# this is called URL configration
urlpatterns = [
    path('hello/', views.hello)
]

# steps we go to rout into specific endpoint
# 1. define a function in views that respond for endpoint request using httprequest object
# 2. create a file that handle specific routnand call the function
# 3. include the file into general url file using include. include takes url and file path.