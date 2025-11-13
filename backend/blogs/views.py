from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog, Tag
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404
import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from .models import Blog, Tag
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import crawl_medium_tag


@api_view(['GET'])
def blog_list(request):
    tag = request.GET.get('tag')
    if tag:
        blogs = Blog.objects.filter(tags__name__iexact=tag).order_by('-crawled_at')
    else:
        blogs = Blog.objects.all().order_by('-crawled_at')[:50]
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crawl_tag(request, tag_name):
    data = crawl_medium_tag(tag_name)
    if not data:
        return Response({"message": "No blogs found or failed to crawl"}, status=400)
    return Response({"tag": tag_name, "count": len(data), "blogs": data})

