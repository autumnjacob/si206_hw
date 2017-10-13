import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

taglist=list()
url=input("Enter URL: ")
count=int(input("Enter count:"))
position=int(input("Enter position:"))
for i in range(count):
    print ("Retrieving:",url)
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html)
    tags=soup('a')
    for tag in tags:
        taglist.append(tag)
    url = taglist[position-1].get('href', None)
    del taglist[:]
print ("Retrieving:",url)