from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/<slug:platform_slug>/', views.PlatformDetail.as_view(), name='platform_detail'),
    path('projects/<slug:platform_slug>/<slug:author_slug>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('projects/<slug:platform_slug>/<slug:author_slug>/<slug:project_slug>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
    path('tag/<slug:name>', views.TagDetail.as_view(), name='tag_detail'),
    path('publications/', views.PublicationList.as_view(), name='publication_list'),
]
