import re,requests,parsel,time,math

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
file_url = '景区.csv'
indexUrl = "http://www.iweeeb.com" # 首页
index_data = requests.get("http://www.iweeeb.com/sceneries/") # 获取页面数据
pro_data = parsel.Selector(index_data.text) # 结构化页面数据
pro_name = pro_data.xpath("//table//a/text()").extract() # 获取省份名称
pro_link = pro_data.xpath("//table//a/@href").extract() # 获取省份连接
pro_link = [indexUrl + i for i in pro_link] # 拼接完整省份链接
pro_name_link = zip(pro_name,pro_link) # 将省份 名称和链接打包
# print(list(pro_name_link))

for i in pro_name_link:
    print('-------STR:' + i[0] + '-------')
    city_data = requests.get(i[1])
    city_data = parsel.Selector(city_data.text)
    city_name = city_data.xpath('//a[starts-with(@href,"/sceneries/city")]/text()').extract()  # 获取名称
    city_link = city_data.xpath('//a[starts-with(@href,"/sceneries/city")]/@href').extract()  # 获取链接
    city_link = [indexUrl + i for i in city_link]  # 拼接完整链接
    city_name_link = zip(city_name, city_link)  # 将名称和链接打包
    # print(list(city_name_link))
    time.sleep(1)
    for j in  city_name_link:
        num = re.compile('\d+').findall(j[0])[0] # 获取当前条件下景区个数
        page = math.ceil(int(num)/50) # 计算页面个数
        print('\t----'+j[0]+'----')
        for k in range(1, page + 1):
            sce_data = requests.get(j[1]+'pa-'+str(k))
            city_data = parsel.Selector(sce_data.text)
            sce_name = city_data.xpath('//div[@class="list"]/ul/li/a/text()').extract()
            sce_link = city_data.xpath('//div[@class="list"]/ul/li/a/@href').extract()
            sce_link = [indexUrl + i for i in sce_link]
            sc_name_lnik = zip(sce_name,sce_link)
            with open(file_url, 'a+') as f:
                [f.write(i[0] +'\t'+j[0]+'\t'+h+'\n') for h in sce_name]
            [print(i[0] +'\t'+j[0]+'\t'+h) for h in sce_name]
            # print(sce_name)
            time.sleep(1)
        # print('----' + j[0] + '----')
    print('-------END:' + i[0] + '-------')