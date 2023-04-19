from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, SearchPosts, subscriptions, AuthorDetail


urlpatterns = [
   path('news/', PostList.as_view(), name="posts"),
   path('subscriptions/', subscriptions, name='subscriptions'),
   path('author/<int:pk>', AuthorDetail.as_view(), name="author"),
   path('news/<int:pk>', PostDetail.as_view(), name="post"),
   path('news/create', PostCreate.as_view(), name="post_edit"),
   path('news/<int:pk>/update', PostUpdate.as_view(), name="post_update"),
   path('news/<int:pk>/delete', PostDelete.as_view(), name="post_delete"),
   path('news/search', SearchPosts.as_view(), name="search"),
]
