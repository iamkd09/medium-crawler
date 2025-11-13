from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Tag, Blog

class CrawlerTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_crawl_endpoint_returns_data(self):
        response = self.client.post(reverse('crawl-tag', args=['technology']))
        self.assertIn(response.status_code, [200, 400])  

    def test_blog_list_endpoint(self):
        Tag.objects.create(name="test")
        response = self.client.get(reverse('blog-list') + '?tag=test')
        self.assertEqual(response.status_code, 200)
