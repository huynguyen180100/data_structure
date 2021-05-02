import requests
from bs4 import BeautifulSoup

url = "https://tiki.vn/thuc-pham/c15074"

html_content = requests.get(url).text
#parse the html content
soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify()) # print the parsed data of html

#print(soup.title)
links = soup.findAll("div","product-item")
for link in links:
    print("Ten hang" + link["data-view-d"])