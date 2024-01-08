from zenrows import ZenRowsClient
from bs4 import BeautifulSoup
import csv

# url = "https://www.g2.com/categories/seo-tools"

url = "https://www.g2.com/categories/seo-tools?order=g2_score&page=2#product-list"

# f = open('g2_page1.txt', 'r')
# response = f.read()

# f2 = open('g2_page2.txt', 'r')
# response = f2.read()
try:
    client = ZenRowsClient("cffbda80d4dd6e9856aa6b834ba65f5c4d30bdfa")
    params = {"js_render":"true","premium_proxy":"true"}

    response = client.get(url, params=params)
    print(response.text)

# Write response (HTML of page) to a text file, to reduce number of times having to call the API and spend credits
    f2 = open("g2_page2.txt", "w")
    f2.write(response.text)
    f2.close()
except: 
    print("Failed to retrieve page template, double check the URL / API key used!")

if (response):
    soup = BeautifulSoup(response, 'html.parser')
    
    titles = soup.find_all('div', attrs={'itemprop': 'name'})
    
    image_links = soup.find_all('img', attrs={'itemprop': 'image'})
    
    with open('g2_data.csv', 'a', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        writer.writerow(["title", "image_link"])
        for (index, title) in enumerate(titles):
            image_link = image_links[index].get('data-deferred-image-src')
            writer.writerow([title.text, image_link])
    
    # print(titles)