from django.contrib.sitemaps import Sitemap
from .models import Book


class BooksSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Book.read.all()

    def lastmod(self, obj):
        return obj.updated
