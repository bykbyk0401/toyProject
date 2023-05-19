from django.urls import path
from posts.views import *

urlpatterns = [
    path('new/', create_post, name = 'create_post'),
    path('all/', get_post_all, name = 'get_post_all'),
    path('delete/<int:id>/', delete_post, name = 'delete_post'),
    path('<int:id>/', get_post, name = 'get_post'),
]