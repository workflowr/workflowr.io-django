from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('author/<slug:name>', views.AuthorDetail.as_view(), name='author_detail'),
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('project/<slug:name>', views.ProjectDetail.as_view(), name='project_detail'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
    path('tag/<slug:name>', views.TagDetail.as_view(), name='tag_detail'),
    path('publications/', views.PublicationList.as_view(), name='publication_list'),
]
