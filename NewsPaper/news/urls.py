from django.urls import path
from .views import PostList, PostDetail, PostCrate, PostUpdate, PostDelete, SearchPosts, ArticleCrate


urlpatterns = [
   path('news/', PostList.as_view(), name="posts"),
   path('news/<int:pk>', PostDetail.as_view(), name="post"),
   path('news/create', PostCrate.as_view(), name="post_edit"),
   path('news/<int:pk>/update', PostUpdate.as_view(), name="post_update"),
   path('news/<int:pk>/delete', PostDelete.as_view(), name="post_delete"),
   path('article/create', ArticleCrate.as_view(), name="post_edit"),
   path('article/<int:pk>/update', PostUpdate.as_view(), name="post_update"),
   path('article/<int:pk>/delete', PostDelete.as_view(), name="post_delete"),
   path('news/search', SearchPosts.as_view(), name='search'),
]
