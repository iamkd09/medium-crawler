from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name

class Blog(models.Model):
    medium_id = models.CharField(max_length=255, blank=True, null=True)  # optional unique id if available
    title = models.CharField(max_length=500)
    creator = models.CharField(max_length=255)
    details = models.TextField(blank=True)      # short snippet
    content = models.TextField(blank=True)      # full content (or HTML)
    url = models.URLField(blank=True, null=True)
    crawled_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blogs')

    def __str__(self):
        return self.title[:80]

class Response(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='responses')
    author = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    posted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.author}: {self.content[:50]}"