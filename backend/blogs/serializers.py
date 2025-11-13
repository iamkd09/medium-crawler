from rest_framework import serializers
from .models import Blog, Tag, Response

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['id','author','content','posted_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    responses = ResponseSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ['id','title','creator','details','content','url','crawled_at','tags','responses']
