from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from jobs_board_scrapper_app.scrapper.scrapper.spiders.jobs_board_spider import JobsDataSpider

@defer.inlineCallbacks
def crawl():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    yield process.crawl(JobsDataSpider)
    process.stop()

@shared_task
def sync_db():
    crawl()
    reactor.run()
