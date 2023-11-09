import scrapy


class MoeStatsSpiderSpider(scrapy.Spider):
    name = "moe_stats_spider"
    allowed_domains = ["stats.moe.gov.tw"]
    start_urls = ["https://stats.moe.gov.tw/bcode/"]

    def parse(self, response):
        pass
