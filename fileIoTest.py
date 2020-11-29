from os import strerror

class FileIo:

	# Illustrate usage of opening file read stream
	def readSomeTxt(self):
		try:
			ccnt = lcnt = 0
			s = open('text.txt', 'rt')
			line = s.readline()
			while line != '':
				lcnt += 1
				for ch in line:
					print(ch, end='')
					ccnt += 1
				line = s.readline()
			s.close()
			print("\n\nCharacters in file:", ccnt)
			print("Lines in file:     ", lcnt)
		except IOError as e:
			print("I/O error occurred:", strerr(e.errno))

# Instantiate fileTester
fileTester = FileIo()

# Read some text
fileTester.readSomeTxt()