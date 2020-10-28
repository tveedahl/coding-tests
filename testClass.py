from random import seed, randint

class TestClass:

	# Constructor
	def __init__(self):
		self.number = 12

	# Test yield operator or keyword
	def fun(self, n):
		for i in range(n):
			yield i

	def lambdaTest(self):
		# Test lambda functions
		two = lambda : 2
		sqr = lambda x : x * x
		pwr = lambda x, y : x ** y

		for a in range(-2, 3):
			print(sqr(a), end=" ")
			print(pwr(a, two()))

	def mapFuncTest(self):
		# Illustrate use of lambdas in map function
		list1 = [x for x in range(5)]
		list2 = list(map(lambda x: 2 ** x, list1))
		print(list2)
		for x in map(lambda x: x * x, list2):
			print(x, end=' ')
			print()

	def filterFuncTest(self):
		# Illustrate use of lambda function in filter function
		seed()
		data = [ randint(-10,10) for x in range(5) ]
		filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
		print(data)
		print(filtered)

	def closureTest(self, par):
		loc = par
		def inner():
			return loc
		return inner

tester = TestClass()
# print(tester.fun(5))
# tester.lambdaTest()
# tester.filterFuncTest()

# Implement closure test
var = 1
fun = tester.closureTest(var)
print(fun())