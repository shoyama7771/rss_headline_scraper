
import requests
from bs4 import BeautifulSoup

#rss_url = "https://news.yahoo.co.jp/rss/topics/top-picks.xml" #Yahoo!ニュース
#rss_url = "https://www3.nhk.or.jp/rss/news/cat0.xml"  #NHKニュース
rss_url = "https://www.asahi.com/rss/asahi/newsheadlines.rdf"  #朝日新聞
#rss_url = "https://b.hatena.ne.jp/hotentry.rss"  #なてなブックマーク
res = requests.get(rss_url)
soup = BeautifulSoup(res.content, features="xml")

items = soup.find_all("item")
for item in items:
    print("見出し:", item.title.text)
    print("URL:", item.link.text)


