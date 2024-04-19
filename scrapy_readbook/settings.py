# Scrapy settings for scrapy_readbook project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_readbook"

SPIDER_MODULES = ["scrapy_readbook.spiders"]
NEWSPIDER_MODULE = "scrapy_readbook.spiders"

DEFAULT_REQUEST_HEADERS = {
    'User - Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Cookie':'ll="118159"; bid=QriEcd4RrPA; __utmc=30149280; __utmc=81379588; _vwo_uuid_v2=D38C6963B1E43402DC0598D031B7E9DAA|d41a0107a52af66eb7f2b97edd86adc7; __yadk_uid=kbjdBCCN9I30ecEpGFnQvURKbpM0FHQ3; __utmz=30149280.1690021569.6.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=81379588.1690021569.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1690031389%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D9DFMDtPElHU0PisoGsm6AfEl6XEhKuTYzEoYEyNrKMIOeUa2op5ZyZkxh9hBMU0a%26wd%3D%26eqid%3D847fae080012810a0000000664bbaebd%22%5D; _pk_ses.100001.3ac3=*; __utma=30149280.2035635660.1689064084.1690025222.1690031390.8; __utma=81379588.588536361.1690015662.1690025222.1690031390.5; __utmt_douban=1; __utmt=1; viewed="36402006_36369244_35031587_36256156_36398795_36330616_36427040_36390509_36314892_36420864"; __gads=ID=61023eb97b8ac9f1-22d8e7abe4df0082:T=1690015742:RT=1690032230:S=ALNI_MaPrfa4Qm4FqgTDiT-TJaw9omrg4A; __gpi=UID=00000d0047cc8fdf:T=1690015742:RT=1690032230:S=ALNI_MYYwqrrtncxUYJk7C2c4-gUMDJ_JA; _pk_id.100001.3ac3=b2b9c8d83c54a053.1690015662..1690032326.undefined.; __utmb=30149280.18.10.1690031390; __utmb=81379588.18.10.1690031390'
}
HTTPERROR_ALLOWED_CODES = [403]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# DOWNLOADER_MIDDLEWARES = {
# 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
# }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapy_readbook (+http://www.yourdomain.com)"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# 将日志打印进logmes.log中
LOG_FILE='logmes.log'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "scrapy_readbook.middlewares.ScrapyReadbookSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "scrapy_readbook.middlewares.ScrapyReadbookDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWROD = '923105'
DB_NAME = 'book_management'
DB_CHARSET = 'utf8'

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
"scrapy_readbook.pipelines.ScrapyReadbookPipeline": 300,
 "scrapy_readbook.pipelines.MysqlPipeline": 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
