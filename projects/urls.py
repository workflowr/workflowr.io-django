from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.index, name='index'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
    path('tag/<slug:name>', views.TagDetail.as_view(), name='tag_detail'),
]
