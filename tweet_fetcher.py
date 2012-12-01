#!/usr/bin/python

import otter
import codecs
import sys

sys.stdout = codecs.getwriter('utf-8')(sys.stdout) 

kw = otter.loadrc() # load beta 

# rc = otter.Resource('searchcount', **kw)
# rc(q='gangnam style site:twitter.com')
# print rc.response

for i in range(110,130):
    rs = otter.Resource('search')
    rs(q='gangnam style', window='d'+str(i), type='tweet')

    for page in rs:
        for item in page.response.list:
            print item.title, item.url

# rt = otter.Resource('trackbacks', **kw)
# rt(url='https://www.youtube.com/watch?v=9bZkp7q19f0', sort_method='date')

# for page in rt:
#     print page.response.total
#     for item in page.response.list:
#         print item.author

    
