from bs4 import BeautifulSoup
import requests

url="https://tutsgalaxy.com"

data=requests.get(url)

url2="https://www.yify-torrent.org/popular.html"

data2=requests.get(url2)

url3="https://www.yify-torrent.org/latest.html"

data3=requests.get(url3)

print("---------------Courses---------------")
print()

soup=BeautifulSoup(data.text,'html.parser')

for article in soup.find_all('article'):
    headline=article.h3.a.text
    link=article.h3.a
    print(headline)
    print()

print("------------Movies by Popular------------")
print()

soup2=BeautifulSoup(data2.text,'html.parser')

for article in soup2.find_all('article'):
    movie=article.figcaption.h3.a.text
    print(movie)
    print()

print("------------Movies by Latest------------")
print()

soup3=BeautifulSoup(data3.text,'html.parser')

for article in soup3.find_all('article'):
    movie=article.figcaption.h3.a.text
    print(movie)
print()
