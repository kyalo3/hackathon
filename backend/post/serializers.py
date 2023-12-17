from rest_framework import serializers
from .models import Post,Comment,Reply

class PostSerializer(serializers.ModelSerializer):
    """ this serializer for post model  for list and view"""
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Post
        fields=('id','title','content','tags','image','created_at','edited_at','user')
        

class PostSerializerCreate(serializers.ModelSerializer):
    """ this serializer for post model  for list and view"""
    "N.B: doesnot contain image since image has its own serrializer"
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Post
        fields=('id','title','content','tags','created_at','edited_at','user')
        

        
        
class PostImageUploadSerializer(serializers.HyperlinkedModelSerializer):
    """ this serializer for image in post model, since image need its own serializer because it is file type . """
    class Meta:
        model = Post
        fields= (
            'id',
            'image'
        )
        
        
class CommentSerializer(serializers.ModelSerializer):
    """ this serializer for comment model """
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Comment
        fields=('id','content','created_at','post','user')
        
 
class ReplySerializer(serializers.ModelSerializer):
    """ this serializer for Reply model """
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Reply
        fields=('id','reply_post','content','comment','created_at','user')
        
        
       
