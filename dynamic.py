import requests
import string
import re
import urllib.request
from selenium import webdriver

# response = urllib.request.urlopen('http://tutorialpoint.com/search')
# html = response.read()
# text = html.decode()
# re.findall('(.*?)',text)


# PAGE_SIZE = 15
# url = 'https://www.tutorialspoint.com/index.htm/' + 'search.json?page={}&page_size={}&search_term=a'
# countries = set()
# for letter in string.ascii_lowercase:
#    print('Searching with %s' % letter)
#    page = 0
#    while True:
#       response = requests.get(url.format(page, PAGE_SIZE, letter))
#       data = response.json()
#       print('adding %d records from the page %d' %(len(data.get('records')),page))
#       for record in data.get('records'):countries.add(record['country'])
#       page += 1
#       if page >= data['num_pages']:
#         break
#       with open('countries.txt', 'w') as countries_file:
#          countries_file.write('n'.join(sorted(countries))) 

path = r'C:\\Users\\gaurav\\Desktop\\Chromedriver'
driver = webdriver.Chrome(executable_path = path)
driver.get('http://google.com/search')
driver.find_element_by_id('search_term').send_keys('.')
js = "document.getElementById('page_size').options[1].text = '100';"
driver.execute_script(js)
driver.find_element_by_id('search').click()
driver.implicitly_wait(45)
driver.implicitly_wait(45)
links = driver.find_elements_by_css_selector('#results a')
countries = [link.text for link in links]
print(countries)
driver.close()
