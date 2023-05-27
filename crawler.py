# crawler.py

import requests
import re
from lxml import etree


def crawl(news_list):
    result = {}
    for news in news_list:
        page = requests.get(news['link'])
        html = etree.HTML(page.content)
        content = html.xpath('//div[@class="article"]/p//text()')
        article = ''.join(content).replace('\u3000', '') # replace \u3000 with empty string
        article = re.sub('责任编辑.*$', '', article) # remove any lines starting with "责任编辑"
        article = re.sub('编辑.*$', '', article) # remove any lines starting with "编辑"
        article = re.sub('审校.*$', '', article) # remove any lines starting with "审校"
        news['article'] = article
    return news_list
