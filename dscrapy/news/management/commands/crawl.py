from django.core.management.base import BaseCommand

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
from scrapy import signals

from dnevnik.dnevnik.spiders.dnevnik import DnevnikSpider

from dscrapy.news.models import Article


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        results = []

        def crawler_results(signal, sender, item, response, spider):
            results.append(item)

        dispatcher.connect(crawler_results, signal=signals.item_passed)

        settings =  get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl(DnevnikSpider)
        process.start()

        for result in results:
            Article(**result).save()
