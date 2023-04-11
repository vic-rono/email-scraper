# importing the modules
# requests for bulding network requests(HTTP library)
# deque container data type that adds and removes items from containers
# urlib parses the URLs
# beautiful soup pulls  data from HTML files
# url processing

import requests
import requests.exceptions
from collections import deque
import urllib.parse
import re
from bs4 import BeautifulSoup

int_url = str(input('[+] ENTER URL:'))  # force it to string

# setting scrap levels

unscraped_urls = deque([int_url])

# buld an unordered collection of unique elements
# stor unscraped urls
scraped_urls = set()
emails = set()

# SCRAPING


# oh len like .length in JavaScript
# deque from the collections module is an easier for loop basically
count = 0

try:
    while len(unscraped_urls):
        count += 1
        if count == 100:
            break
    url = unscraped_urls.popleft()
    scraped_urls.add(url)

    # fallback for ctrl z (quit)
except KeyboardInterrupt:
    print('Exiting..../(-_-)/')

# urlib.parse breaking down url into various components and extract information needed
# to extract data from different parts of the URL.
# /about to try to build a resolvable URL from URL extracted from the source code

# url.split will return 5 bits of information https(addressing scheme), network locations, path, query and fragment
# victorrono.com/about?id=1#top

parts = urllib.parse.urlsplit(url)
base_url = '{0.scheme}://{0.netloc}'.format(parts)

if '/' in parts.path:
    path = url[:url.rfind('/') + 1]
else:
    path = url
print('[%d][Scraping %s' % (count, url))

response = requests.get(url)
new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",response.text, re.I))
emails.update(new_emails)

#SPIDER
#beatifulsoup looks for anchor tags

supu = BeautifulSoup(response.text, "html.parser")
for anchor in supu.find_all("a"):
   if "href" in anchor.attrs:
        link = anchor.attrs["href"]
   else:
        link = ''
   if link.startswith('/'):
        link = base_url + link
   elif not link.startswith('http'):
        link = path + link
   if not link in unscraped_urls and not link in scraped_urls:
       unscraped_urls.append(link)


for email in emails:
    print(email)





