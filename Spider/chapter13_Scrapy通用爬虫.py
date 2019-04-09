

#****** 13.10 Scrapy通用爬虫 ******

#  将各个站点的Spider的公共部分保留下来，不同的部分提取出来作为单独的配置，如爬取规则、页面解析方式等抽离出来做成一个配置文件，name在新增一个爬虫的时候，
#  只需要实现这些网站的爬取规则和提取规则即可。

# 对接项目-scrapyuniversal
#   以中华科技类新闻为例，了解CrawlSpider和Item Loader的用法，提取其可配置信息实现可配置化。
#   抓取新闻类表中的所有分页的新闻详情，包括标题、正文、时间、来源等。
#   以往创建的Spder模板是Basic，这次需要选择crawlspider
#       scrapy genspider -t crawl xx xx.xx.com

