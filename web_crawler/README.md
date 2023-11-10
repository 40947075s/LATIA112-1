# HW2: Web Crawler

尋找與教育相關的網頁資料，並對資料分別使用Beautiful Soup、Selenium、Scrapy爬取後儲存成CSV檔案，且需要附上程式註解說明。

> 註：[爬蟲主程式碼](web_crawler/spiders/moe_stats_spider.py)

> 註：爬取到的資料被儲存為[output.csv](output.csv)。

## 執行方式

確認是否已安裝好相關套件，若無，請按以下指令安裝：

```bash
pip install scrapy
pip install selenium
pip install beautifulsoup4
```

進入專案資料夾，並執行scrapy指令使用爬蟲：

```bash
scrapy crawl moe_stats_spider
```
