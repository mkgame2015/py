from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen('https://morvanzhou.github.io/tutorials/data-manipulation/scraping/2-02-beautifulsoup-css/').read().decode('utf-8')
soup =BeautifulSoup(html,features='lxml')
li = soup.find_all('li')
# for i in li:
#     print(i.get_text())
print(li)