import requests
from lxml import etree


def get_news():
    url = 'https://news.sina.com.cn/'
    page = requests.get(url)
    html = etree.HTML(page.content)

    news_list = []
    lis = html.xpath('//ul[@class="list_14"]/li/a')
    count = 0
    for li in lis:
        if count >= 20 and "组图" not in li.xpath('text()')[0]:
            break  # 如果已经获取了>=20条新闻，并且当前新闻不是“组图”，停止获取
        if "组图" in li.xpath('text()')[0]:
            continue  # 如果当前新闻是“组图”，跳过本次循环
        title = li.xpath('text()')[0].strip()
        link = li.xpath('@href')[0]
        news_list.append({'title': title, 'link': link})
        count += 1

    return news_list
