from zenrows import ZenRowsClient
from bs4 import BeautifulSoup

url = "https://www.g2.com/categories/seo-tools"
f = open('demofile.txt', 'r')
response = f.read()
# try:
#     client = ZenRowsClient("cffbda80d4dd6e9856aa6b834ba65f5c4d30bdfa")
#     params = {"js_render":"true","json_response":"true","premium_proxy":"true",}

#     response = client.get(url, params=params)
#     f = open("demofile.txt", "w")
#     f.write(response.text)
#     f.close()
# except:
#     print("Failed to retrieve page template, double check the URL / API key used!")

if (response):
    soup = BeautifulSoup(response, 'html.parser')

    sections = soup.find_all('div')
    
    print(sections)