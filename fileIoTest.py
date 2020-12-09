from os import strerror

class FileIo:

	# Illustrate usage of opening file read stream
	def readSomeTxt(self):
		try:
			fo = open('newtext.txt', 'wt')
			for i in range(10):
				fo.write("line #" + str(i+1) + "\n")
			fo.close()
		except IOError as e:
			print("I/O error occurred: ", strerror(e.errno))

# Instantiate fileTester
fileTester = FileIo()

# Read some text
fileTester.readSomeTxt()