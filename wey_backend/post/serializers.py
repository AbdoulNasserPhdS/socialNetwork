from rest_framework import serializers

from .models import Post, PostAttachment,Like,Comment, Trend

from account.serializers import UserSerializer


class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ('id', 'get_image',)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id','created_by')


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id','created_by','created_at_formatted_comment','comment')


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)
    like=LikeSerializer(read_only=True, many=True)
    comments=CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'body','created_by','likes_count','created_at_formatted', 'attachments','like','comments','comments_count')
        
        
class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trend
        fields = ('id','hashtag','occurences')
