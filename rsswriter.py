#! /usr/bin/env python
# coding: euc-jp
from RSS import ns, CollectionChannel, TrackingChannel
class Rss_gen:
    def generate(self, items):
        cc = CollectionChannel()
        channel = {
            (ns.rdf, 'about'): 'http://hoge/rss.rdf',
            (ns.rss10, 'title'): 'hoge',
            (ns.rss10, 'link'): 'http://hoge/',
            (ns.rss10, 'description'): "ほげ",
            }
        cc.setMD((ns.rss10, 'channel'), channel)
        
        for i in items:
            o = {}
            o[(ns.rss10, 'title')] = i['title']
            o[(ns.rss10, 'link')] = i['link']
            o[(ns.content, 'description')] = i['description']
            #o[(ns.dc, 'creator')] = i['author']
            #o[(ns.dc, 'date')] = i['date']
            cc.addItem(o)
            print(o)
            
        return cc.output(cc.listItems())



items = list()
item = dict()
item['title'] = 'hoge'
item['link'] = 'http://fuga.example.com/'
item['description'] = 'this is an article description.'
#item['author'] = 'takano32'
#item['date'] = '2005-09-23 17:00:00'
items.append(item)
rss_gen = Rss_gen()
print(rss_gen.generate(items))
