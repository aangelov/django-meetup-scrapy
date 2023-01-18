from scrapy import Request, Spider


class DnevnikSpider(Spider):
    name = 'dnevnik'
    allowed_domains = ['www.dnevnik.bg']
    start_urls = ['https://www.dnevnik.bg/novini/']
    domain = 'https://www.dnevnik.bg'

    def extract_article(self, response, row):
        article = {}

        article['url'] = row.css('.text a::attr(href)').get()
        article['title'] = row.css('.text a::text').get()

        return article

    def find_news(self, response):
        news = []
        rows = response.css('.secondary-article-v2')
        for row in rows:
            news.append(self.extract_article(response, row))

        return news

    def parse_article(self, response):
        article = {}

        article['title'] = response.css('.content h1::text').get()
        article['url'] = response.url
        article['pub_date'] = response.css('.article-tools time::attr(datetime)')[0].extract()
        article['body'] = response.css('.article-content').get()

        yield article

    def parse(self, response):
        news = self.find_news(response)

        for article in news:
            yield Request(
                f"{self.domain}{article['url']}",
                callback=self.parse_article,
            )
