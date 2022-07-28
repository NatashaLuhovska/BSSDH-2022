import scrapy

class ArticleSpider(scrapy.Spider):
  name='article'
  start_urls = ['https://en.wikipedia.org/wiki/Lion%27s_mane_jellyfish', 'https://en.wikipedia.org/wiki/Sherlock_Holmes',
  'https://en.wikipedia.org/wiki/Jellyfish#Phases']

  def parse(self, response):
    title = response.css('h1.firstHeading::text').get()
    #subtitle = response.css('h2.article-lead::text').get()


    print('Title is: ' + title)
    #print('Subtitle is: ' + subtitle)