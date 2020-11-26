import requests


def test_good_proxy_url():
    '''
    从proxyUrl.txt中选取可以使用的代理ip
    :return: good_proxy_url_list
    '''
    good_proxy_url_list = []
    with open(r'C:\Users\94826\Desktop\文件\学习\爬虫学习\project\request_test\baidu_tieba\proxyUrl.txt','r',encoding='utf-8') as fp:
        proxyhttp_list=fp.readlines()
    for proxyhttp in proxyhttp_list:

        if proxyhttp.split(':')[0] =='http':
            proxies={'http':proxyhttp.strip()}
        elif proxyhttp.split(':')[0] =='https':
            proxies={'https':proxyhttp.strip()}
        #print(proxies)
        try:
            response = requests.get('http://httpbin.org/get', proxies=proxies)
            good_proxy_url_list.append(proxies)
        except requests.exceptions.ConnectionError as e:
            print('Error', e.args)
    return good_proxy_url_list
if __name__ == '__main__':
    good_proxy_url_list=test_good_proxy_url()
    print(good_proxy_url_list)
