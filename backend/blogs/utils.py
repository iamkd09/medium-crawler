import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from .models import Blog, Tag
from pprint import pprint


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0 Safari/537.36"
}

def crawl_medium_tag(tag_name):
    """
    Crawl 10 latest blogs for a given tag from Medium.com
    Returns a list of dicts with blog info
    """
    url = f"https://medium.com/tag/{tag_name}/latest"
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    articles = soup.find_all("article")
    results = []

    for article in articles[:10]:
        # extract title
        title_tag = article.find("h2")
        title = title_tag.text.strip() if title_tag else "Untitled"

        # extract creator/author
        author_tag = article.find("a", {"data-testid": "authorName"})
        creator = author_tag.text.strip() if author_tag else "Unknown"

        # extract short description/details
        detail_tag = article.find("p")
        details = detail_tag.text.strip() if detail_tag else ""

        # extract blog URL
        link_tag = article.find("a", href=True)
        url = None
        if link_tag and link_tag["href"].startswith("https://medium.com/"):
            url = link_tag["href"].split("?")[0]

        results.append({
            "title": title,
            "creator": creator,
            "details": details,
            "url": url,
        })

    # save to DB
    tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
    for data in results:
        blog, created = Blog.objects.get_or_create(
            title=data["title"],
            creator=data["creator"],
            defaults={
                "details": data["details"],
                "url": data["url"],
                "crawled_at": timezone.now(),
            }
        )
        blog.tags.add(tag_obj)
    return results
