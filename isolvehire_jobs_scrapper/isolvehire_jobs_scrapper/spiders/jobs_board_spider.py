from pathlib import Path
from html2text import html2text
import scrapy


class JobsDataSpider(scrapy.Spider):
    name = "jobs"

    def start_requests(self):
        urls = [
            'https://arkbh.isolvedhire.com/jobs/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        job_urls = response.xpath(
            '//div[@id="job_listings"]//a/@href').getall()
        yield from response.follow_all(job_urls, self.parse_job_data)

    def parse_job_data(self, response):
        yield {"Title": response.xpath(f'//a[@href="{"/" + ("/".join(response.url.split("/")[-2:]))}"]/text()').get(),
               "Location": response.xpath('//ul[@class="job-items"]//li//span/b[@title="Location"]/../../span[2]/text()').get(),
               "Pay": response.xpath('//ul[@class="job-items"]//li//span/b[@title="Pay"]/../../span[2]/text()').get(),
               "Pay Type": response.xpath('//ul[@class="job-items"]//li//span/b[@title="Pay Type"]/../../span[2]/text()').get(),
               "Employment Type": response.xpath('//ul[@class="job-items"]//li//span/b[@title="Employment Type"]/../../span[2]/text()').get(),
               "Job Benefits": response.xpath('//ul[@class="job-items"]/../p/i/text()').get(),
               "Job Description": ' '.join((response.xpath('//div[@id="mainArea"]/div[1]/div/div[1]/div[2]//*/text()').extract()))
               }
