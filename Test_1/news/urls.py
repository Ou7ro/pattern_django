from django.urls import path
from . import views
#лучше не указывать в путь news, будет ошибка, потому, что мы уже отслеживаем этот шаблон т.к. путь был бы news/news/
urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'), 
    #Отслеживаем динамический параметр, не ставим пробелы. <тип данных:название> 
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
]
