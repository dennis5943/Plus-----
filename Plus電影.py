import re
import requests
from bs4 import BeautifulSoup

url = "http://www.plus28.com/logging.php?action=login"
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Host":"www.plus28.com",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"}

data = {
"referer":"http://www.plus28.com/index.php",
"loginfield":"username",
"username":"[your username]",
"password":"[your password]",
"questionid":"0",
"loginsubmit":"true"}

s = requests.Session()
res = s.post(url,headers = headers,data = data)

data2 = {"adult":"1","agreedsubmit":"是，願意遵守。".encode(encoding='big5')}
res = s.post("http://www.plus28.com/forumdisplay.php?fid=9",headers = headers,data = data2)
res.encoding = 'big5'

# ==============開始分析資料================
soup = BeautifulSoup(res.text,"html5lib")
articles_table = soup.find("table",id = "forum_9")

for tbody in articles_table.find_all("tbody"):
    stype = tbody.find("em").a.contents[0]
    title = tbody.find("span").a.contents[0]
    link = tbody.find("span").a["href"]
    date = tbody.find("td","author").find("em").contents[0]
    print(date,"[",stype,"]",title)
    print("http://www.plus28.com/" + link.strip())
    #print(tbody.prettify())
    print("==================")
