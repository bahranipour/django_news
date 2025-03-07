from django.urls import path 
from . import views

urlpatterns = [
    path('',views.news_list,name='news_list'),
    path('<int:category_id>/',views.news_list,name='news_by_category'),
    path('about',views.about,name='about'),
    path('news/<int:pk>/',views.news_detail,name='news_detail'),
    #path('category/<int:category_id>/',views.news_by_category,name='news_by_category'),
    path('tag/<int:tag_id>/',views.news_by_tag,name='news_by_tag'),
]