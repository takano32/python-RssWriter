from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print "Encountered the beginning of a %s tag" % tag
		print(type(tag))
		for attr in attrs:
			if attr[0] == 'back':
				print(attr[1])
			
		
	def handle_endtag(self, tag):
		print "Encountered the end of a %s tag" % tag



filename = '/home/takano32/tmp/htmlparse.html'
infile = open(filename)

body = infile.read()
parser = MyHTMLParser()
parser.feed(body)
parser.close()

#lines = infile.readlines()
#for line in lines:
#	print(line.rstrip())


