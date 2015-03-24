'''A metaclass is a class/object which defines a type/class of other classes. 
In Python a metaclass can be a class, a function or any object that supports calling "Interface!"

This is because to create a class object, its metaclass is called with the class name, 
base class and attributes (methods)
When no metaclass is defined (which is usually the case), the default metaclass 'type' is used'''

class Meta(type):
	def __new__(meta, name, base, attr):
		print 'creating new class'
		print 'meta name: ', meta
		print 'name?: ', name
		print 'base class: ', base
		print 'attributes: ', attr
		#food = {}
		attr['food'] = {}
		return super(Meta, meta).__new__(meta, name, base, attr)


	def __init__(cls, name, bases, attrs):
		print '\n'
		print 'class name: ', cls
		print 'class bases: ', bases
		print 'class attributes: ', attrs
		return super(Meta, cls).__init__(name, bases, attrs)

	def __call__(cls, *args, **kwds):
		print '\n'
		print 'call of: ', str(cls)
		print 'args: ', str(args)
		return type.__call__(cls, *args,**kwds)


#metaclass creats the class frame of "MyClass"
class MyClass(object):
	__metaclass__ = Meta 
	def __init__(self, a, b):
	#	print self.__class__.__name__
	#         this is the way to get the class's name
		print "has two arguments: {} {}".format( a, b)



k = MyClass(1, 2)