from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.homePage, name="home"),
    path('project/<str:pk>',views.project, name="project"),
    path('profile',views.project, name="profile"),
    # path('projects',views.projects,name="projects"),
]