from django.urls import path
from . import views
# from .views import tweet_list


urlpatterns = [
    path('list/', views.tweet_list,name = 'tweet_list'),
    # path('list/', tweet_list, name='tweet_list'),
    path('create/', views.tweet_create,name = 'tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit,name = 'tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete,name = 'tweet_delete'),
]