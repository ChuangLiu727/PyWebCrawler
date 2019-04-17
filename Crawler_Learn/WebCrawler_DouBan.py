# coding=UTF-8
#https://movie.douban.com/top250
#每页有25条电影，共有10页。
#电影列表在页面上的位置为一个class属性为grid_view的ol标签中。
#每条电影信息放在这个ol标签的一个li标签里。

import requests
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_URL = 'http://movie.douban.com/top250'

def download_page(url):
    #手动指定User-Agent为Chrome浏览器，再此访问就得到了真实的网页源码。服务器通过校验请求的U-A来识别爬虫
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url).content
    return data


def parse_html(html):
    #创建了一个BeautifulSoup对象
    soup = BeautifulSoup(html)
    #使用刚刚创建的对象搜索这篇html文档中查找那个class为grid_view的ol标签
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    movie_name_list = []
    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class': 'title'}).getText()
        movie_name_list.append(movie_name)
        #print movie_name
    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    #如果有下一页，则返回下一页的url
    if next_page:
        return movie_name_list, DOWNLOAD_URL + next_page['href']
    return movie_name_list, None


def main():
    url = DOWNLOAD_URL

    with codecs.open('movies', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))

if __name__ == '__main__':
    main()
