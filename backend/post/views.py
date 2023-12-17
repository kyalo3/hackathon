
from rest_framework import generics
from .models import Post,Comment,Reply
from .serializers import PostSerializer,PostSerializerUpdateAndCreate,PostImageUploadSerializer,CommentSerializer,ReplySerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated,BasePermission
from django.shortcuts import get_object_or_404

from rest_framework import viewsets



# we can list and create items by this view 

class PostCreate(generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializerUpdateAndCreate
 
    
class PostList(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    



    
    

#used to update some fields inside post table  
class ProductUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerUpdateAndCreate
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "post updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
          

    
    
""" image view"""


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostImageUploadSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'
    def get_queryset(self):
        
        id =self.kwargs.get(self.lookup_field)



        return Post.objects.filter(id=id)
    


class CommentCreate(generics.CreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    
class CommentList(generics.ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    


class ReplyCreate(generics.CreateAPIView):
    queryset=Reply.objects.all()
    serializer_class=ReplySerializer
 
    
class ReplyList(generics.ListAPIView):
    queryset=Reply.objects.all()
    serializer_class=ReplySerializer

    
    
