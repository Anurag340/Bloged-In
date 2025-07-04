from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, UserProfile, Post, Comment, Like, Tag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'post_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_post_count(self, obj):
        return obj.posts.count()

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'username', 'bio', 'profile_picture', 'website', 
                 'location', 'date_of_birth', 'is_verified', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'username', 'is_verified', 'created_at', 'updated_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['id', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    username = serializers.CharField(source='author.username', read_only=True)
    replies = serializers.SerializerMethodField()
    reply_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'username', 'parent', 'content', 
                 'is_approved', 'replies', 'reply_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'username', 'is_approved', 'replies', 
                           'reply_count', 'created_at', 'updated_at']
    
    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True, context=self.context).data
        return []
    
    def get_reply_count(self, obj):
        return obj.replies.count()

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Like
        fields = ['id', 'user', 'username', 'post', 'like_type', 'created_at']
        read_only_fields = ['id', 'user', 'username', 'created_at']

class PostListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'category', 'excerpt', 
                 'featured_image', 'status', 'is_featured', 'view_count', 
                 'comment_count', 'like_count', 'tags', 'created_at', 'published_at']
        read_only_fields = ['id', 'slug', 'author', 'view_count', 'comment_count', 
                           'like_count', 'created_at', 'published_at']
    
    def get_comment_count(self, obj):
        return obj.comments.filter(is_approved=True).count()
    
    def get_like_count(self, obj):
        return obj.likes.count()

class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'category', 'content', 'excerpt', 
                 'featured_image', 'status', 'is_featured', 'allow_comments', 
                 'view_count', 'comment_count', 'like_count', 'tags', 'comments', 
                 'likes', 'created_at', 'updated_at', 'published_at']
        read_only_fields = ['id', 'slug', 'author', 'view_count', 'comment_count', 
                           'like_count', 'created_at', 'updated_at', 'published_at']
    
    def get_comment_count(self, obj):
        return obj.comments.filter(is_approved=True).count()
    
    def get_like_count(self, obj):
        return obj.likes.count()

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'excerpt', 'featured_image', 
                 'status', 'is_featured', 'allow_comments']
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'parent', 'content']
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'like_type']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        # Check if user already liked this post
        like, created = Like.objects.get_or_create(
            user=validated_data['user'],
            post=validated_data['post'],
            defaults={'like_type': validated_data['like_type']}
        )
        if not created:
            # Update existing like
            like.like_type = validated_data['like_type']
            like.save()
        return like 