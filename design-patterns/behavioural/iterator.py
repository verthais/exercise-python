class Zoom:
	def __iter__(self):
		return ZoomIterator()


class ZoomIterator:
	def __init__(self):
		self.index = 0

	def __next__(self):
		if self.index > 22:
			raise StopIteration
		
		self.index += 1
		return self.index


def count_to(count):
	"""Our iterator implementation"""
	
	#Our list
	numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

	#Our built-in iterator
	#Creates a tuple such as (1, "eins")
	iterator = zip(range(count), numbers_in_german)
	
	#Iterate through our iterable list
	#Extract the German numbers
	#Put them in a generator called number
	for position, number in iterator:
		
		#Returns a 'generator' containing numbers in German
		yield number 

def main():
	#Let's test the generator returned by our iterator
	for num in count_to(3):
		print("{}".format(num))

	for num in count_to(4):
		print("{}".format(num))
	
	zoom = Zoom()

	for z in zoom:
		print(z)

if __name__ == '__main__':
	main()