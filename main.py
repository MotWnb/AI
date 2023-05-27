# main.py

from news import get_news
from crawler import crawl


def main():
    news_list = get_news()
    for news in news_list:
        print(news['title'])
        print(news['link'])

    # 在获取新闻列表后继续进行更深入的爬取
    result = crawl(news_list)
    print(result)


if __name__ == '__main__':
    main()
