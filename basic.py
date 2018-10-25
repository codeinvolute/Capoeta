from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq
from urllib.parse import urlparse
from brain import heart

print ('Enter your URL')

url = input()

uClient = uReq(url)
mainUrl = urlparse(url).netloc
mainArray= mainUrl.split(".")
if len(mainArray) == 2:
    mainUrl = "www." + mainUrl
else: 
    mainUrl = mainUrl
html_page = uClient.read()

uClient.close()
page_soup = soup(html_page, "html.parser")
if mainUrl in heart.keys():
    #do something.
    print(mainUrl + " exists!!")
else:
    #get inputs and save it to brain.
    print(mainUrl + " does not exist.")