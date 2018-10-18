#timer
#default is minutes
class Timer:
	def __init__(self, amount_of_time):
		self._amount_of_time = amount_of_time

		self._units_conv = 60
		self._start_time = time() / self.units_conv
	
	def units(self, conversion_factor):
		#sets the units_conv to a new int 
		try:
			conversion_factor = int(conversion_factor)
		except ValueError as VE:
			return
		self._units_conv = int(conversion_factor)
		return
	def start_timer(self):
		#print({0})


