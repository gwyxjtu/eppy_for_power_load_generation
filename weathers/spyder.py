import requests
import zipfile
import tempfile
from lxml import etree
 
def get_data(url):
    #url = "https://energyplus.net/weather-download/asia_wmo_region_2/CHN//CHN_Anhui.Huoshan.583140_CSWD/all"
    response = requests.get(url)
    return url, response.content
def unzip(filename,data):
    _tmp_file = tempfile.TemporaryFile()  # 创建临时文件
    #print(_tmp_file)
 
    _tmp_file.write(data)  # byte字节数据写入临时文件
    # _tmp_file.seek(0)
 
    zf = zipfile.ZipFile(_tmp_file, mode='r')
    for names in zf.namelist():
        f = zf.extract(names, './'+filename)  # 解压到zip目录文件下
        print(f)
    zf.close()
if __name__ == '__main__':

    url_main = 'https://energyplus.net/weather-region/asia_wmo_region_2/CHN'
    response = requests.get(url_main)
    #print(response.content)
    html = etree.HTML(response.content)
    name_city = html.xpath('/html/body/div[2]/div/section/div/section/div/a/@href ')
    #print(name_city)

    for i in range(len(name_city)):
        #print(name_i)
        s = name_city[i].split('/')
        # print("https://energyplus.net/weather-download/asia_wmo_region_2/CHN//"+s[-1]+"/all")
        url = "https://energyplus.net/weather-download/asia_wmo_region_2/CHN//"+s[-1]+"/all"
        print(url)
        url, data = get_data(url)
        unzip(s[-1],data)
        exit(0)
    # url = "https://energyplus.net/weather-download/asia_wmo_region_2/CHN//CHN_Anhui.Huoshan.583140_CSWD/all"
    # url, data = get_data(url)  # data为byte字节
 
