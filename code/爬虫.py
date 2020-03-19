import requests  
import re
def main(limit):
    url = 'https://maoyan.com/board/4?offset=' + str(limit)
    htmlData = requestMaoYanData(url) #模拟浏览器请求当时当，并且返回爬取到的数据
    result = parseHtmlData(htmlData) #对爬取到的数据进行解析

    with open('../result/movie.txt','a',encoding = 'utf-8') as f:    #存数据
        for data in result:
            print(data)
            f.write('序号：'+data[0]+'\n'+'电影名：'+data[1]+data[2]+' '+data[3]+'\n'+'评分：'+data[4]+data[5]+'\n'+'\n')



def requestMaoYanData(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/55.0.2883.87 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parseHtmlData(htmlData):
    pattern = re.compile('.*?board-index-.*?">(.*?)</i>.*?class="name">.*?'
                         + '"boarditem-click".*?"{movieId:.*?}">+(.*?)</a>.*?class="star">'
                         + '(.*?)</p>.*?class="releasetime">(.*?)</p>.*?<p class="score">'
                         + '<i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>', re.S)
    parseData = re.findall(pattern,htmlData)
    
    return parseData
if __name__ == '__main__':
    for i in range(0,100,10):
        main(i)