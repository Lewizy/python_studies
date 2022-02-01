iterated_tuple = ("first", "second", "third")
printed_iterated = iter(iterated_tuple)

print(next(printed_iterated))#first
print(next(printed_iterated))#second
print(next(printed_iterated))#third

for i in iterated_tuple:
	print(i)

#itarable string
iterated_string = "iter"
print_interated_string = iter(iterated_string)
print(next(print_interated_string))#i 
print(next(print_interated_string)) #t

for i in iterated_string:
	print(i)

#class iter
class myNumbers:
	
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

x_myNum = myNumbers()
myIter = iter(x_myNum)

for x in myIter:
	print(x)#1,2,....20
