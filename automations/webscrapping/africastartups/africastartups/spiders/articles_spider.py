import scrapy

class ArticlesSpider(scrapy.Spider):
    name = "articles"
    start_urls = [
        'https://www.howwemadeitinafrica.com/category/countries/rwanda/'
    ]

    def parse(self, response):
        for article in response.css('article'):
            title = article.css('header h1::text').get()
            link = article.css('a::attr(href)').get()
            yield response.follow(link, self.parse_article, meta={'title': title, 'link': link})

    def parse_article(self, response):
        title = response.meta['title']
        link = response.meta['link']
        content = ' '.join(response.css('div.entry-content p::text').getall())

        yield {
            'title': title,
            'link': link,
            'content': content,
        }
