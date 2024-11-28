from django.urls import path 
from . import views
urlpatterns = [

    path('',views.ProjectListView.as_view(),name='index'),
    path('create',views.ProjectCreateView.as_view(),name='project_create'),


]