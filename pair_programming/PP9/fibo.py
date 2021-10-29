class Fibonacci:
	def __init__(self, n): 
		self.n = n
	def __iter__(self):
		return FibonacciIterator(self.n)


class FibonacciIterator:
	def __init__(self, n): 
		self.first = 0
		self.second = 1
		self.index = 0
		self.n = n

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == self.n:
			raise StopIteration
		else:
			self.curr = self.first+self.second
			self.first = self.second
			self.second = self.curr
			self.index += 1

		return self.curr



# Demo

fib = Fibonacci(10) # Create a Fibonacci iterator called fib that contains 10 terms
print(list(iter(fib))) # Iterate over the iterator and create a list.


