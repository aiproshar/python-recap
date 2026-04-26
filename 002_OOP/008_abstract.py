
class StreamExample:
	def open(self):
		pass
	def close(self):
		pass
	'''
	We want every class that inherits stream, like file stream, networks steam must implement open and close
	Yes we expect them to implement but cannot force it
	We want Stream class to set behaviour, not implementation. File and Network stream both will implement on their own ways
	This is where we use ABC (abstract base class)
	'''

from abc import ABC, abstractmethod

class Stream(ABC):
	@abstractmethod
	def open(self):
		pass
	@abstractmethod
	def close(self):
		pass

'''
One interesting thing, any class with abstract methods is an abstract class, means you cannot create object of it
'''
try:
	abstract_object = Stream()
except BaseException as e:
	print("Abstract class creation error:", e)

'''
Every class that inherits stream, like file stream, networks steam must implement open and close
Or we get error
'''
class FileStream(Stream):
	def open(self):
		pass
	def close(self):
		pass


class NetworkStream(Stream):
	def open(self):
		pass
	def close(self):
		pass

file_stream = FileStream()
network_stream = NetworkStream()