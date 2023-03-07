from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from jobs_board_scrapper_app.scrapper.scrapper.spiders.jobs_board_spider import JobsDataSpider


@defer.inlineCallbacks
def crawl():
    runner = CrawlerRunner(get_project_settings())

    spider = JobsDataSpider()

    crawler = runner.crawl(spider)
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    yield crawler

def sync_db():
    configure_logging()
    runner = CrawlerRunner(get_project_settings())

    d = runner.crawl(JobsDataSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
