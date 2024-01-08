from zenrows import ZenRowsClient
from bs4 import BeautifulSoup
import csv

url = "https://www.g2.com/categories/seo-tools"
f = open('g2_page1.txt', 'r')
response = f.read()
# try:
#     client = ZenRowsClient("cffbda80d4dd6e9856aa6b834ba65f5c4d30bdfa")
#     params = {"js_render":"true","premium_proxy":"true"}

#     response = client.get(url, params=params)
#     print(response.text)

# Write response (HTML of page) to a text file, to reduce number of times having to call the API and spend credits``
#     f = open("g2_page1.txt", "w")
#     f.write(response.text)
#     f.close()
# except: 
#     print("Failed to retrieve page template, double check the URL / API key used!")

if (response):
    soup = BeautifulSoup(response, 'html.parser')
    
    sections = soup.find('div', attrs={'itemprop': 'name'}).text
    # for link in links:
    #     print(link.get('href'))
    
    print(sections)