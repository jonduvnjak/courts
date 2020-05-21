import requests
import urllib3.request
import time
from bs4 import BeautifulSoup

url = 'http://eresources.hcourt.gov.au/browse?col=0.html'

response = requests.get(url)

#print ("%s" %(response)) 
soup = BeautifulSoup(response.text, "html.parser")
#soup.findAll('a')
#one_a_tag = soup.findAll("a")[0]
#print one_a_tag
#print (soup.get_text())
#print soup.a
#a_tag = soup.a
#print a_tag
#print (soup.prettify())
