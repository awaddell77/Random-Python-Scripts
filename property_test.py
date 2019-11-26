#property test
#property(fget, fset, fdel, doc)
#Returns a property attribute from the given getter, setter and deleter.
class T_class_a:
		def __init__(self, a):
			self._name = a

		
		def get_name(self):
			return self._name

		
		def set_name(self, n_name):
			if n_name == 'Bob': print("Bob is not valid, name unchanged")
			else:
				self._name = n_name
			return
		
		
		
		def del_name(self):
			del self._name
		name = property(get_name, set_name, del_name)


#the same thing but with decorators and metaprogrammeing
'''The main work of decorators is they are used to add functionality to the existing code. 
Also called metaprogramming, as a part of the program tries to modify another part of the program
at compile time.'''
class T_class_b:
		def __init__(self, a):
			self._name = a

		@property
		def name(self):
			return self._name

		@name.setter
		def name(self, n_name):
			if n_name == 'Bob': print("Bob is not valid, name unchanged")
			else:
				self._name = n_name
			return
		@name.getter
		def name(self):
			return self._name
		@name.deleter
		def name(self):
			del self._name


m_inst_b = T_class_b('Mary')
m_inst_a = T_class_a("Jane")
