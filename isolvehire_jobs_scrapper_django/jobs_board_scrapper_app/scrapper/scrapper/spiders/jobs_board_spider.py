import scrapy
from jobs_board_scrapper_app.models import Job


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
        job = Job(url=response.url,
                  title=response.xpath(
                      f'//a[@href="{"/" + ("/".join(response.url.split("/")[-2:]))}"]/text()').get(),
                  location=response.xpath(
                      '//ul[@class="job-items"]//li//span/b[@title="Location"]/../../span[2]/text()').get(),
                  pay=response.xpath(
                      '//ul[@class="job-items"]//li//span/b[@title="Pay"]/../../span[2]/text()').get(),
                  pay_type=response.xpath(
                      '//ul[@class="job-items"]//li//span/b[@title="Pay Type"]/../../span[2]/text()').get(),
                  employment_type=response.xpath(
                      '//ul[@class="job-items"]//li//span/b[@title="Employment Type"]/../../span[2]/text()').get(),
                  job_benefits=response.xpath(
                      '//ul[@class="job-items"]/../p/i/text()').get(),
                  job_description=' '.join((response.xpath('//div[@id="mainArea"]/div[1]/div/div[1]/div[2]//*/text()').extract())))
        if not Job.objects.filter(url=job.url):
            job.save()
        yield {"url": Job.url,
               "title": Job.title,
               "location": Job.location,
               "pay": Job.pay,
               "pay_type": Job.pay_type,
               "employment_type": Job.employment_type,
               "job_benefits": Job.job_benefits,
               "job_description": Job.job_description}
