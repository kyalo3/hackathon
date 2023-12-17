from django.db import models
from taggit.managers import TaggableManager  
from django.shortcuts import get_object_or_404


def upload_to(instance,filename):
    return 'post/{filename}'.format(filename=filename)
class Post(models.Model):
    title=models.CharField(max_length=40)
    content=models.TextField(null=True, max_length=5000)

    tags = TaggableManager()
    image=models.ImageField(upload_to="post/images/",null=True)

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    edited_at=models.DateTimeField(auto_now=True)
    # user=models.ForeignKey(User ,on_delete=models.CASCADE,null=True,related_name='user_posts')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        return f"/media/{self.image}"
 
    @classmethod
    def get_all_object(cls):
        return cls.objects.all()
    
    @classmethod
    def get_specific_object(cls,id):
        return get_object_or_404(cls,pk=id)
    
    
    
   

class Comment(models.Model):
    content=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    post=models.ForeignKey(Post ,on_delete=models.CASCADE,null=True,related_name='post_comments')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_replies(self):
        return self.replies.all()
    
   
class Reply(models.Model):
    reply_post=models.ForeignKey(Post ,on_delete=models.CASCADE,null=True,related_name='re_post')
    comment=models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    content=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user.username