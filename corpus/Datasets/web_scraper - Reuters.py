# -*- coding: utf-8 -*-
from lxml import html
import requests
import write_functions as w

def scrape_webpages(url,upper_bound_page_no, name_text_class):
    elements = []
    
    for p in range(1, int(upper_bound_page_no)+1):
        #request_page = requests.get('%s%s'%(url,p))
        tree = html.fromstring(requests.get('%s%s'%(url[:-1],p)).content)
        elements += tree.find_class(name_text_class)
        
    print "Found %d lines"%len(elements)
    return elements

uri_string = 'http://www.reuters.com/news/archive/businessNews?view=page&page=1'
output1 = []
tree = html.fromstring(requests.get('%s'%uri_string).content)
# print html.tostring(tree) # Useful for scanning the 

text_class = 'story-title'
max_page_no = 400
categories = ['business', 'world', 'politics', 'technology']
headlines = []
for c in categories:
    cat_uri = 'http://www.reuters.com/news/archive/%sNews?view=page&page=1'%c
    cat_headlines = scrape_webpages(cat_uri, max_page_no, text_class)
    for hl in cat_headlines:
        headlines.append(hl)

for h in range(len(headlines)):
    headlines[h] = headlines[h].text_content().strip()

# Write away the gathered headlines:
w.write_to_pickle("reuters_scraped", headlines)
