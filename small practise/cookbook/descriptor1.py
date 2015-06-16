class Descriptor(object):
	def __init__(self, name=None, **opt):
		self.name = name
		for key, value in opt.items():
			setattr(self, key, value)


    #descriptor, class that use the __set__ or __get__
    #second argu is "instance" cause class instance can be set value to
	def __set__(self, instance, value):
		instance.__dict__[self.name] = value
		#everything in python is an object
		#everything has a dictionary to lookup its key-value pair
		pass



#type is a Descriptor sub-class. so is Unsigned, MaxSized
#Integer is Typed's director sub-class.
#The design is good.. clear.. every parent class and sub-class is focused on its own goal
class Typed(Descriptor):
	expected_type = type(None)

	def __set__(self, instance, value):
		if not isinstance(value, self.expected_type):
			raise TypeError('Expected: ' + str(self.expected_type))
		super(Typed, self).__set__(instance, value)


class Unsigned(Descriptor):
	def __set__(self, instance, value):
		if value < 0:
			raise ValueError('Expected >= 0')
		super(Unsigned, self).__set__(instance, value)


class MaxSized(Descriptor):
	def __init__(self, name=None, **opts):
		if 'size' not in opts:
			raise TypeError("Missing size option")
		super(MaxSized, self).__init__(name, **opts)

	def __set__(self, instance, value):
		if len(value) >= self.size:
			raise ValueError("Size Must be < " + str(self.size))
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


#use descriptor as class wrapped type directly
class Stock(object):
	name = SizedString('name', size=8)
	shares = UnsignedInteger('share')
	price = UnsignedFloat('price')
	def __init__(self, name, shares, price):
		self.name = name
		self.shares = shares
		self.price = price

		
