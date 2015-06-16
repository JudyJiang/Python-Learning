#import flask
'''
Python cookbook recipe 8.13
Data model and type checking using descriptor.
'''
class Descriptor(object): #OMG, without the object, everything will be wrong
	def __init__(self, name=None, **opt):
		self.name = name
		for key, value in opt.items():
			setattr(self, key, value)

	def __set__(self, instance, value):
		#print ('set value: ', self.name, value)
		instance.__dict__[self.name] = value

class Typed(Descriptor):
	expected_type = type(None)

	def __set__(self, instance, value):
		if not isinstance(value, self.expected_type):
			raise TypeError('expected ' + str(self.expected_type))
		super(Typed, self).__set__(instance, value)


class Unsigned(Descriptor):
	def __set__(self, instance, value):
		if value < 0:
			raise ValueError('Expected >= 0')
		super(Unsigned, self).__set__(instance, value)


class MaxSized(Descriptor):
	def __init__(self, name=None, **opts):
		if 'size' not in opts:
			raise TypeError('missing size option')
		super(MaxSized, self).__init__(name, **opts)

	def __set__(self, instance, value):
		if len(value) >= self.size:
			raise ValueError('size must be < ' + str(self.size))
		super(MaxSized, self).__set__(instance, value)

class Integer(Typed):
	expected_type = int

class UnsignedInteger(Integer, Unsigned):
	pass

class Float(Typed):
	expected_type = float

class UnsignedFloat(Float, Unsigned):
	pass

class String(Typed):
	expected_type = str

class SizedString(String, MaxSized):
	pass


class Stock(object): #object is necessary in python2.7+
	name = SizedString('name', size=8)
	shares = UnsignedInteger('share') #this is just the name of this checked type,
	price = UnsignedFloat('price')
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price


'''
decorator can decorates both functions  and classes...
'''
def check_attributes(**kwargs):
	def decorate(cls):
		for key, value in kwargs.items():#here value is a class or a class instance
			if isinstance(value, Descriptor):
			#	print 'yes ', key, value
				value.name = key
				setattr(cls, key, value)
			else:
			#	print 'not ', key, value
				setattr(cls, key, value(key))
		return cls
	return decorate


@check_attributes(name=SizedString(size=8), #cause there's a parameter here size=8..there's no initialization for unsigned.
	                  shares=UnsignedInteger,
	                  price=UnsignedFloat)
class Stock(object):
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price




'''
another decorator
'''

def Typed(expected_type, cls=None):
	print cls
	if cls is None:
		return lambda cls: Typed(expected_type, cls)
	super_set = cls.__set__
	def __set__(self, instance, value):
		if not isinstance(value, expected_type):
			raise TypeError('expected ' + str(expected_type))
		super_set(self, instance, value)
	cls.__set__ = __set__
	return cls

def Unsigned(cls):
	print cls
	super_set = cls.__set__
	def __set__(self, instance, value):
		if value < 0:
			raise ValueError("Expected >= 0")
		super_set(self, instance, value)
	cls.__set__ = __set__
	return cls



@Typed(int)
class Integer(Descriptor):
	pass

@Unsigned
class UnsignedInteger(Integer):
	pass