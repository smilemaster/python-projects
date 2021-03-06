import json
from urllib.parse import urlencode

import re
from bs4 import  BeautifulSoup
import  requests
from requests import RequestException


def get_page_index(offset,keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload':  'true',
        'count': '20',
        'cur_tab': 3,
        'from': 'gallery'
     }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code ==200:
            return response.text
        return  None
    except RequestException:
        print("请求索引页失败")
        return  None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')



def get_page_detail(url):
    try:
        kv = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url,headers = kv)
        if response.status_code ==200:
            return response.text
        return  None
    except RequestException:
        print("请求详情页失败")
        return  None


def parse_page_detail(html,url):
    soup  = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    # print(title)
    image_pattern = re.compile('gallery: JSON.parse\("(.*?)"\),\s+siblingList',re.S)
    # image_pattern = re.compile('gallery: JSON.parse\("(.*?)"\)',re.S)
    urls = re.findall(image_pattern, html)
    d = ",".join(urls)
    s = d.replace('\\', "")
    j = json.loads(s)
    images_urls = [item.get('url') for item in j["sub_images"]]
    return {
    "title": title,
    "url": url,
    "images_urls": images_urls
    }
    # result = re.search(image_pattern,html)
    # d=result.group(1)
    # if result:
    #
    #     data = json.loads(result)
    #     images_urls = [item.get('url') for item in data["sub_images"]]
    #     return {
    #     'title': title,
    #     'url': url,
    #     'images_urls': images_urls
    #     }
        # print(data)
    #     if data and 'sub_images' in data.keys():
    #         sub_images = data.get('sub_images')
    #         images = [item.get('url') for item in sub_images]
    #         for item in sub_images:
    #             images = item.get('url')
    #         return {
    #             'title':title,
    #             'url':url,
    #             'image':images
    #
    #         }


def main():
    html = get_page_index(0,'街拍')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result =parse_page_detail(html,url)
            print(result)

main()




