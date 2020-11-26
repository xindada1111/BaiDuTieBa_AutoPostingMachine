#coding:utf-8
import requests
from lxml import etree
import os
import time

def request(url,xpath):
    '''
    :param url:
    :param xpath:
    :return: ret  xpath过滤后的结果
    '''
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

    res=requests.get(url,headers=headers)
    res.encoding = res.apparent_encoding
    response=res.text
    html=etree.HTML(response)
    ret=html.xpath(xpath)
    return ret

def parse_url_list():
    '''
    爬取跟‘天猫入驻’相关的贴吧链接
    :return:
    '''
    url='https://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=python%C5%C0%B3%E6&rn=10&un=&only_thread=0&sm=1&sd=&ed=&pn={}'
    for i in range(1,200):   #修改页数
        url=url.format(i)
        xpath='//div[@class="s_post_list"]/div/span/a/@href'
        url_list=request(url,xpath)
        url_list=['https://tieba.baidu.com'+i for i in url_list]
        for detail_url in url_list:
            #print(detail_url)
            parse_tieba_name(detail_url)
            time.sleep(2)
def parse_tieba_name(url):
    xpath='//a[@class="card_title_fname"]/text()'
    tieba_name=request(url,xpath)
    if tieba_name:
        name=tieba_name[0].strip()
        print(name)
        filename=os.getcwd()+'/贴吧.txt'
        with open(filename, 'a', encoding='utf-8') as fp:
            fp.write(name + '\n')
def processing_text():
    '''
    去除重复的贴吧名，以及去除 ‘XXX吧’ 的‘吧’字
    :return:
    '''
    filename = os.getcwd() + '/贴吧.txt'
    with open(filename,'r',encoding='utf-8') as fp:
        tieba_name_lst=fp.readlines()
    #print(tieba_name_lst)
    with open(filename, 'w', encoding='utf-8') as fp:
         for tieba_name in set(tieba_name_lst):
            fp.write(tieba_name[:-2]+'\n')  #去除贴吧名最后一个字
def main():
    #parse_url_list()
    processing_text()

if __name__ == '__main__':
    main()
