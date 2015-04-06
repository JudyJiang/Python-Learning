import random

def generate_password(passlen=8):
	s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	passwordlen=passlen
	p =  "".join(random.sample(s,passlen ))
	print p