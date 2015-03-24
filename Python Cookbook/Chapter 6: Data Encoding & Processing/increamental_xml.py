import os
from xml.etree.ElementTree import iterparse

#this is useful tip for any kind of large file reading if want to save memory
DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
f = os.path.join(DIR, 'data/test.xml')

def parse_and_remove(filename, path):
	path_parts = path.split('/')
	doc = iterparse(filename, ('start', 'end'))
	next(doc)

	tag_stack = []
	elem_stack = []
	for event, elem in doc:
		if event == 'start':
			tag_stack.append(elem.tag)
			elem_stack.append(elem)
		elif event == 'end':
			#print tag_stack
			if tag_stack == path_parts:
				yield elem
				elem_stack[-2].remove(elem)
			try:
				tag_stack.pop()
				elem_stack.pop()
			except IndexError:
				pass


