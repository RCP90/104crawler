'''104職缺'''
from bs4 import BeautifulSoup
import requests
import prettytable
keyword=input("請輸入職缺關鍵字：")
t = prettytable.PrettyTable(["公司名稱","職缺名稱"], encoding="utf8")
for page in range(1,3,1):
    r1 = requests.get(
        "https://www.104.com.tw/jobs/search/",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        },
        params={
            "ro":"0",
            "keyword":keyword,
            "page":"page",
            "mode":"s",
            "jobsource":"2018indexpoc"
      }
    )
    b1=BeautifulSoup(r1.text,"html.parser")
    a1=b1.find_all("article",{"class":"job-list-item"})
    for a2 in a1:
        t.add_row([a2.attrs["data-cust-name"],a2.attrs["data-job-name"]])
print(t)
