import time

class TimeThis:
	"""docstring for time_this"""

	def __init__(self, num_rums=10):
		self.num_rums = num_rums

	
	def __call__(self, func):
		# Обертка получает аргументы
		def time_counter(*args, **kwargs):
			avg_time = 0
			for i in range(self.num_rums):
				t0 = time.time()
				# Обертка передаёт эти аргументы функции
				func()
				t1 = time.time()
				avg_time += (t1-t0)
			avg_time /= self.num_rums
			print('Выполнение заняло {} секунд'.format(avg_time))
		return time_counter

	def __enter__(self):
		self.t0 = time.time()
		return  

	def __exit__(self, *args):
		t1 = time.time()
		avg_time = (t1-self.t0)
		print('Разность времени - {}'.format(avg_time))
