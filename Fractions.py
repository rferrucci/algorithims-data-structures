#!/usr/bin/env python

"""essesntially, replicating the Fraction class on my own, following
programming exercises for learning algorithms and data structures. 
https://interactivepython.org/runestone/static/pythonds/index.html
Excercises 1.7

"""
def gcd(m,n):
	"""outputs greatest common devisor
	"""
	while m%n != 0:

		oldm = m
		oldn = n

		m = oldn
		n = oldm%oldn
		
	return n

class Fraction:
	def __init__(self, top, bottom):
		"""initializes the fraction, first testing to make sure numerator
		and denominator are integers, then reduces using gcd funcction
		"""
		try:
			if not isinstance(top, int):
				raise ValueError("{} is not integer".format(top))
			if not isinstance(bottom, int):
				raise ValueError("{} is not integer".format(bottom))
		except ValueError as e:
			print('caught this error: ' + repr(e))
		else:
			self.numerator = top
			self.denominator = bottom
			
			common = gcd(self.numerator, self.denominator)
			self.numerator /= common			
			self.denominator /= common
	def __str__(self):
		return str(self.numerator) + "/" + str(self.denominator)
	def __repr__(self):
		return '{0:s}:{1:s}'.format(self.__class__,self.__str__())
	def __add__(self, other):
		"""returns tuple of numerator, denominator pairs from sum of two
		fractions
		"""
		numerator = self.numerator * other.denominator + \
		                    other.numerator * self.denominator
		denominator = self.denominator * other.denominator

		common = gcd(numerator,denominator)
		return Fraction(numerator/common, denominator/common)
	def __sub__(self, other):
		"""returns tuple of numerator, denominator pairs from difference 
		between two fractions
		"""
		numerator = self.numerator * other.denominator - \
		                    other.numerator * self.denominator
		denominator = self.denominator * other.denominator
		common = gcd(numerator,denominator)
		return Fraction(numerator/common,denominator/common)
		
	def __mul__(self, other):
		"""returns tuple of numerator, denominator pairs from product of two
		fractions
		"""
		numerator = self.numerator * other.numerator
		denominator = self.denominator * other.denominator
		common = gcd(numerator,denominator)
		return Fraction(numerator/common,denominator/common)
	def __truediv__(self, other):
		"""returns quotient of numerator, denominator pairs from sum of two
		fractions
		"""
		numerator = self.numerator * other.denominator
		denominator = self.denominator * other.numerator
		common = gcd(numerator,denominator)
		return Fraction(numerator/common,denominator/common)
	def __radd__(self, other):
		"""returns tuple of numerator, denominator pairs from sum of two
		numbers where second is a Fraction and first is not in the class
		"""
		if other == 0:
			return self
		else:
			return self.__add__(other)
	def __iadd__(self, other):
		"""returns tuple of numerator, denominator pairs from sum of two
		fractions using i+=n
		"""
		numerator = self.numerator * other.denominator \
		+ self.denominator * other.numerator
		denominator = self.denominator * other.denominator
		common = gcd(numerator,denominator)
		return Fraction(numerator/common,denominator/common)
		"""following are a set of equality operators for fractions
		"""
	def __gt__(self, other):
		number1 = self.numerator * other.denominator
		number2 = self.denominator * other.numerator
		return number1 > number2
	def __ge__(self, other):
		number1 = self.numerator * other.denominator
		number2 = self.denominator * other.numerator
		return number1 >= number2
	def __lt__(self, other):
		number1 = self.numerator * other.denominator
		number2 = self.denominator * other.numerator
		return number1 < number2
	def __le__(self, other):
		number1 = self.numerator * other.denominator
		number2 = self.denominator * other.numerator
		return number1 <= number2	
	def __ne__(self, other):
		number1 = self.numerator * other.denominator
		number2 = self.denominator * other.numerator
		return number1 != number2
		#__gt__, __ge__, __lt__, __le__			
	def getNum(self):
		return self.numerator
	def getDen(self):
		return self.denominator
