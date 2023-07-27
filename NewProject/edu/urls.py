from django.urls import path
from . import views
urlpatterns = [
    path('skills/',views.edu,name="skills")
]
