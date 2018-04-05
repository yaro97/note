#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yaro
# 抓取雅必备的2546个单词，以备后续 anki 制作卡片
# 抓取网页：https://www.shanbay.com/wordbook/176896/


import requests
from pyquery import PyQuery as pq

## ========以下内容为抓取词典及词典内容========

def get_list(list_url):
    """
    获取开始列表页的html
    :param list_url:
    :return:
    """
    list_html = requests.get(list_url)
    return list_html.text


def parse_list(list_html):
    """
    解析出各个详情页的url
    :param list_html:
    :return:
    """
    doc = pq(list_html)
    detail_urls = doc('.wordbook-wordlist-name a').items()
    for detail_url in detail_urls:
        yield detail_url.attr('href')


def get_detail(detail_url):
    """
    获得详情页的html
    :param detail_url:
    :return:
    """
    detail_html = requests.get(detail_url)
    return detail_html.text


def parse_detail(detail_html):
    """
    解析出某个详情页中的所有的单词
    :param detail_html:
    :return:
    """
    doc = pq(detail_html)
    words = doc('.row strong').items()
    means = doc('.span10').items()
    for word, mean in zip(words, means):
        yield word.text(), mean.text()


## ==========以下内容为写入mdict源码===========

def save_to_file(word, mean):
    with open('word.txt', 'a', encoding='utf-8') as f:
        
        # 写入mdict源码格式的文件，引用外部css文件为“test.css”
                
        f.write(word + '\n')

        f.write('<link rel="stylesheet" href="test.css" type="text/css">')
        f.write("<h1>" + word + "</h1>")
        f.write('<div class = "mean">')
        f.write(mean)
        f.write('</div>' + '\n')
        
        f.write('</>' + '\n')


## ==========主函数，执行抓取相应内容，并写入源码文件==============

def main():
    list_url = 'https://www.shanbay.com/wordbook/176896/'
    list_html = get_list(list_url)
    for detail_url in parse_list(list_html):
        base_detail_url = 'https://www.shanbay.com' + detail_url + '?page={}'
        detail_urls = [base_detail_url.format(i) for i in range(1, 11)]
        for url in detail_urls:
            detail_html = get_detail(url)
            result = parse_detail(detail_html)
            # print(type(result), result)
            for word, mean in result:
                print(word, mean)
                save_to_file(word, mean)


if __name__ == '__main__':
    main()
