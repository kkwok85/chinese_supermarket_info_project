

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

soup = BeautifulSoup(htmldata, 'lxml') 


link = soup.find_all('a')


link[-1]
for link in soup.find_all('a'):
    link_p2 = link.get('href')

link_p1 = "http://feilongmarket.com/images/"

    
urllib.request.urlretrieve(link_p1 + link_p2, "local-filename_test.jpg")

urllib.request.urlretrieve("http://feilongmarket.com/images/u12.gif", "local-filename_test.jpg")



