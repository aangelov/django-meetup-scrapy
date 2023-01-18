# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy_djangoitem import DjangoItem
import sys
import pathlib

sys.path.append((pathlib.Path(__file__) / '..' / '..' / '..' ).resolve())
from dscrapy.news.models import Article

class DnevnikItem(DjangoItem):
    django_model = Article
