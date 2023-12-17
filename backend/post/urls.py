from django.urls import path,include
from .views import ImageUploadViewSet,PostCreate,PostList,ReplyCreateView,ReplyListView,CommentCreateView,CommentListView
from rest_framework.routers import DefaultRouter
app_name='post'

router=DefaultRouter()

router.register(r'imageupload', ImageUploadViewSet)
urlpatterns = [
    path('', include(router.urls)),
 
    # posts all endpoints
    path('post/all',PostList.as_view(),name='list_posts'),
    path('product/create',PostCreate.as_view(),name='post_add'),
    # posts all endpoints
    path('comment/create',CommentCreateView.as_view(),name='comment_add'),
    path('comment/list/<int:user_comment>',CommentListView.as_view(),name='comment_list'),
    # posts all endpoints
    path('reply/list/<int:user_reply>',ReplyListView.as_view(),name='reply_list'),
    path('reply/create',ReplyCreateView.as_view(),name='reply_add'),
    
    
    
    
    
    ]
   