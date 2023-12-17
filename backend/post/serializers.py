from rest_framework import serializers
from .models import Post,Comment,Reply

from taggit.models import Tag

from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """ this serializer for post model  for list and view"""
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    tags = serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields=('id','title','content','tags','image','created_at','edited_at','user')
    def get_tags(self, obj):
        return list(obj.tags.names())



class PostSerializerCreate(TaggitSerializer, serializers.ModelSerializer):
    """ this serializer for post model  for list and view"""
    "N.B: doesnot contain image or tags since image and tags has its own serrializer"
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at', 'edited_at', 'user')
        
        

class PostSerializerCreatetag(TaggitSerializer, serializers.ModelSerializer):
   
    "N.B: this serializer for image in post model, since tag need its own serializer because it is list type ."
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ('tags',)




        

        
        
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
        
        
       
