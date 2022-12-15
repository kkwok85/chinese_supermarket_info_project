

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









htmldata = getdata("https://www.gw-supermarket.com/deal/") 

soup = BeautifulSoup(htmldata, 'lxml') 


sidebar = soup.find('div', class_='with-sidebar-wrapper')
img = sidebar.find_all('img')


link[-1]
for link in soup.find_all('a'):
    link_p2 = link.get('href')

link_p1 = "http://feilongmarket.com/images/"

    
urllib.request.urlretrieve(link_p1 + link_p2, "local-filename_test.gif")

urllib.request.urlretrieve("http://feilongmarket.com/images/u12.gif", "local-filename_test.gif")





htmldata = getdata("https://www.hmart.com/weekly-sales-and-events/new-york-new-jersey/") 

soup = BeautifulSoup(htmldata, 'lxml') 


sidebar = soup.find('div', class_='img-wrapper')
img = sidebar.find_all('img')


link[-1]
for link in soup.find_all('a'):
    link_p2 = link.get('href')

link_p1 = "http://feilongmarket.com/images/"

    
urllib.request.urlretrieve(link_p1 + link_p2, "local-filename_test.gif")

urllib.request.urlretrieve("http://feilongmarket.com/images/u12.gif", "local-filename_test.gif")
