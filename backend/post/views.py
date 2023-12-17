
from rest_framework import generics
from .models import Post,Comment,Reply
from .serializers import PostSerializer,PostSerializerCreate,PostImageUploadSerializer,CommentSerializer,ReplySerializer,PostSerializerCreatetag
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated,BasePermission
from django.shortcuts import get_object_or_404

from rest_framework import viewsets



# we can list and create items by this view 

class PostCreate(generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializerCreate
   
           
   
 
    
class PostList(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
              
class PostCreatetag(generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializerCreatetag
    
""" image view"""


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostImageUploadSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'
    def get_queryset(self):
        
        id =self.kwargs.get(self.lookup_field)



        return Post.objects.filter(id=id)
    


class CommentCreateView(generics.CreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    
class CommentListView(generics.ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    lookup_field = 'user_comment'
    def get_queryset(self):
            
        id =self.kwargs.get(self.lookup_field)

        # And use it as you wish in the filtering below:

        return CommentSerializer.objects.filter(user_comment=id)
    


class ReplyCreateView(generics.CreateAPIView):
    queryset=Reply.objects.all()
    serializer_class=ReplySerializer
    
 
    
class ReplyListView(generics.ListAPIView):
    queryset=Reply.objects.all()
    serializer_class=ReplySerializer
    lookup_field = 'user_reply'
    def get_queryset(self):
        
        id =self.kwargs.get(self.lookup_field)

        # And use it as you wish in the filtering below:

        return ReplySerializer.objects.filter(user_reply=id)
    

    
    
