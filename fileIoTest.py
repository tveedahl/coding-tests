from os import strerror

class FileIo:

	# Illustrate usage of opening file read stream
	def readSomeTxt(self):
		try:
			cnt = 0
			s = open('text.txt', "rt")
			ch = s.read(1)
			while ch != '':
				print(ch, end='')
				cnt += 1
				ch = s.read(1)
			s.close()
			print("\n\nCharacters in file:", cnt)
		except IOError as e:
			print("I/O error occurred: ", strerr(e.errno))

	# Read text file by line via file stream
	def readTxtByLine(self):

# Instantiate fileTester
fileTester = FileIo()

# Read some text
fileTester.readSomeTxt()