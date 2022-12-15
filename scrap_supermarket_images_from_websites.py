

from bs4 import BeautifulSoup 
import requests 
import urllib



def getdata(url): 
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }
    r = requests.get(url, headers = header) 
    return r.text 


htmldata = getdata("http://feilongmarket.com/images/") 
htmldata = getdata("http://feilongmarket.com/images/") 

soup = BeautifulSoup(htmldata, 'lxml') 


link = soup.find_all('a')


link[-1]
for link in soup.find_all('a'):
    link_p2 = link.get('href')

link_p1 = "http://feilongmarket.com/images/"

    
urllib.request.urlretrieve(link_p1 + link_p2, "local-filename_test.gif")

urllib.request.urlretrieve("http://feilongmarket.com/images/u12.gif", "local-filename_test.gif")






# scrap hmart data
htmldata = getdata("https://www.hmart.com/weekly-sales-and-events/new-york-new-jersey/") 

soup = BeautifulSoup(htmldata, 'lxml') 


#link = soup.find_all('div', class_='img-wrapper')[1]


link_result = []

# find all links
for link in soup.find_all("div", class_ = "img-wrapper"):
    for img in link.find_all("img", src=True):  # searching for img with src attribute
        link_result.append(img["src"])

urllib.request.urlretrieve(link_result[1], "h_mart.jpg")






# scrap ifresh data
htmldata = getdata("https://www.ifreshmarket.com/en/flyers/") 

soup = BeautifulSoup(htmldata, 'lxml') 


link = soup.find_all('a', class_='waves')


link_result = []

# find all links
for link in soup.find_all("div", class_ = "service-box style-1"):
    for img in link.find_all("a", class_='waves'):  # searching for img with src attribute
        link_result.append(img.get('href') )

urllib.request.urlretrieve(link_result[0], "ifresh.jpg")


