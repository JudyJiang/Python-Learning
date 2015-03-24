import os
import file
from xml.etree.ElementTree import parse, Element


class XMLNamespaces:
	def __init__(self, **kwargs):
		self.namespace = {}
		for name, uri in kwargs.items():
			self.register(name, uri)

	def register(self, name, uri):
		self.namespace[name] = '{' + uri + '}'

	def __call__(self, path):
		#format_map is the function that
		#maps {} into key, value within the namespace
		return path.format_map(self.namespace)


def test_namespace():
	f = os.path.join(file.DATA, 'namespace.xml')
	doc = parse(f)
	ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
	print doc.find(ns('content/{html}html'))
	


test_namespace()
'''
f = os.path.join(file.DATA, 'pred.xml')
doc = parse(f)
root = doc.getroot()

root.remove(root.find('sri'))
root.remove(root.find('cr'))

index = root.getchildren().index(root.find('nm'))
e = Element('spam')
e.text = 'This is a test'
root.insert(index, e)

doc.write('newpred.xml', xml_declaration=True)
'''