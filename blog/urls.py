from django.contrib import admin
from django.urls import path
from .views import PostList,PostDetail,PostCreate,PostUpdate,PostDelete,UserList
from . import views


urlpatterns = [
    path('about/',views.about,name='about'),
    path('',PostList.as_view(),name='home'),
    path('drafts/',views.DraftListView.as_view(),name='post-draft-list'),
    path('post/new/',PostCreate.as_view(),name='post-create'),
    path('post/<int:pk>/publish',views.post_publish,name='post-publish'),
    path('post/<username>/<int:pk>/update/',PostUpdate.as_view(),name='post-update'),
    path('post/<username>/<int:pk>/delete/',PostDelete.as_view(),name='post-delete'),
    path('post/<username>/<int:pk>/',PostDetail.as_view(),name ='post-detail'),
    path('post/<username>/',UserList.as_view(),name='user-posts'),
]