class Template():
	def __init__(self, template):
		self.template = template 

	def open(**kwargs):
		#this works for string template type,
		#if other object, may use format_map
		return self.template.format(**kwargs)


#can be rewrite to another funcion (class -> function)

def template(template):
	def str_fun(**kwargs):
		return template.format(**kwargs)
	return str_fun


def test1():
	f_str = template("{name} dosn't want to go to the {tech} training")
	print f_str(name="Judy", tech="Github")