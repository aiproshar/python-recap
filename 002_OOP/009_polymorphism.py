
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

def process_stream(stream: Stream):
	print("Opening stream")
	stream.open()
	print("Processing stream")
	print("Closing stream")
	stream.close()

if __name__ == "__main__":
	stream_list: list[Stream] = [FileStream(), NetworkStream()]
	for stream in stream_list:
		process_stream(stream)
