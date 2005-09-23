from RSS import ns, CollectionChannel
class Rss_gen:
    def generate(self, items):
        cc = CollectionChannel()
        channel = {
            (ns.rdf, 'about'): u'http://hoge/rss.rdf',
            (ns.rss10, 'title'): u'hoge',
            (ns.rss10, 'link'): u'http://hoge/',
            (ns.rss10, 'description'): u"¤Û¤²",
            }
        cc.setMD((ns.rss10, 'channel'), channel)
        
        for i in items:
            o = {}
            o[(ns.rss10, 'title')] = i['title']
            o[(ns.rss10, 'link')] = i['link']
            o[(ns.content, 'encoded')] = i['description']
            o[(ns.dc, 'creator')] = i['author']
            o[(ns.dc, 'date')] = i['date']
            cc.addItem(o)
            
            return cc.output(cc.listItems())


items = list()
items.append({'title': 'hoge',
              'link': 'fuga.example.com',
              'description': 'this is an article description.',
              'author': 'takano32',
              'date', '2005-09-23 17:00:00'})
rss_gen = Rss_gen(items)
rss_gen.generate()
