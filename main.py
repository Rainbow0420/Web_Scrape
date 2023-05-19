# import requests
# r = requests.get('https://authoraditiagarwal.com/')
# print(r.text[:200])
import urllib3
import urllib.request
from bs4 import BeautifulSoup
import builtwith
import whois
import re
import requests
from lxml import html 

# Sample 1 
http = urllib3.PoolManager()
r = http.request('GET', 'https://authoraditiagarwal.com')
soup = BeautifulSoup(r.data, 'lxml')
print (soup.title)
print (soup.title.text)
print(builtwith.parse('http://authoraditiagarwal.com'))
# print(whois.whois('microsoft.com'))

# Sample 2
response = urllib.request.urlopen('http://example.webscraping.com/places/default/view/India-102')
html = response.read()
text = html.decode()
print("finalData",re.findall('<td class="w2p_fw">(.*?)</td>',text))

# Sample 3
url = 'https://authoraditiagarwal.com/leadershipmanagement/'
path = '//*[@id="panel-836-0-0-1"]/div/div/p[1]'
response = requests.get(url)
byte_string = response.content
source_code = html.fromstring(byte_string)
tree = source_code.xpath(path)
print(tree[0].text_content()) 