import lxml.html
import urllib.request as urllib2
import pprint
import http.cookiejar as cookielib
def form_parsing(html):
   tree = lxml.html.fromstring(html)
   data = {}
   for e in tree.cssselect('form input'):
      if e.get('name'):
         data[e.get('name')] = e.get('value')
   return data
REGISTER_URL = '<a target="_blank" rel="nofollow" href="http://example.webscraping.com/user/register">http://example.webscraping.com/user/register</a>'
ckj = cookielib.CookieJar()
browser = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckj))
html = browser.open('<a target="_blank" rel="nofollow" href="http://example.webscraping.com/places/default/user/register?_next"> http://example.webscraping.com/places/default/user/register?_next</a> = /places/default/index').read()
form = form_parsing(html)
pprint.pprint(form)