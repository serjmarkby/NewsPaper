from django.urls import path
from .views import PostList, PostDetail, PostCrate, PostUpdate, PostDelete, SearchPosts


urlpatterns = [
   path('', PostList.as_view(), name="posts"),
   path('<int:pk>', PostDetail.as_view(), name="post"),
   path('create', PostCrate.as_view(), name="post_edit"),
   path('<int:pk>/update', PostUpdate.as_view(), name="post_update"),
   path('<int:pk>/delete', PostDelete.as_view(), name="post_delete"),
   path('search', SearchPosts.as_view(), name='search'),
]
