
from abc import ABC, abstractmethod

class Stream(ABC):
	@abstractmethod
	def open(self):
		pass
	@abstractmethod
	def close(self):
		pass


class FileStream(Stream):
	def open(self):
		print("Opening file stream")
	def close(self):
		print("Closing file stream")


class NetworkStream(Stream):
	def open(self):
		print("Opening network stream")
	def close(self):
		print("Closing network stream")

'''
This is the actual polymorphism
Our process stream taking different types of stream, each object's open and close is different function
Changing behaviour during runtime
We cannot know which draw we will call, until runtime. That's why this is called runtime polymorphism
'''
def process_stream(stream_object: Stream):
	print("Opening stream")
	stream_object.open()
	print("Processing stream")
	print("Closing stream")
	stream_object.close()

if __name__ == "__main__":
	stream_list: list[Stream] = [FileStream(), NetworkStream()]
	for stream in stream_list:
		process_stream(stream)








'''
But to be honest, python runs on duck typing, its a dynamically typed language
This will just be fine

If it walks like a duck and quacks like a duck, it is a duck. That is python philosophy
It only looks for existence for certain methods, doesn't care base class 
'''
print("\n\n\nStart of DUCK Type Example \n\n")

class FileStream(Stream):
	def open(self):
		print("Opening file stream")
	def close(self):
		print("Closing file stream")


class NetworkStream(Stream):
	def open(self):
		print("Opening network stream")
	def close(self):
		print("Closing network stream")




if __name__ == "__main__":
	stream_list = [FileStream(), NetworkStream()]
	for stream_object in stream_list:
		# Duck typing, as long as we have open close method, python happy
		stream_object.open()
		stream_object.close()

