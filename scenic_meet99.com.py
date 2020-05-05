import requests
import re, time

def append_url(url,add_url):
    '''
    网址拼接
    :param url: 被拼接的网址列表
    :param add_url: 要拼接的网址的前缀
    :return: 拼接后的网址列表
    '''
    url_after = list(map(lambda i: add_url + i, url))
    return url_after

def get_rst(url="https://www.meet99.com/maps/loadchild/lvyou/", re_rule="lvyou-(.*)\.html",url_add="https://www.meet99.com/maps/loadchild/lvyou/"):
    '''

    :param url: 目标地址
    :param re_rule: 匹配条件
    :return: 匹配结果（列表类型）
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    # proxy = {'HTTP': '125.110.109.87:9000'}
    data = requests.get(url, headers=headers,).text
    re_rst = re.compile(re_rule).findall(data)
    rst = append_url(re_rst,url_add)
    time.sleep(1)
    return rst
def for_url(url, re_rule="lvyou-(.*)\.html",add_url=""):
    '''
    传入：父列表，匹配规则
    返回：获取到的所有子列表的整合
    '''
    list = []
    for i in url:
        if "---" in i:
            continue
        rst = get_rst(i, re_rule)
        list.append('---' + i + '---')
        list.extend(rst)
        list.append('---' + i + '---')
        print('---' + i + '---')
        print(append_url(rst,add_url))
        print('---' + i + '---')
        time.sleep(1)
        # return list
    return list

url_main = "https://www.meet99.com/"  # 主站点


province = get_rst()  # 提取省份
print(province)
city = for_url(province)
print(city)
street = for_url(city,add_url="https://www.meet99.com/lvyou-")
