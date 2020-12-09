from os import strerror

class ByteArrayTest:

    def impByteArr(self):
        data = bytearray(10)

        for i in range(len(data)):
            data[i] = 10 - i
        
        for b in data:
            print(hex(b))
    
    def writeByteArr(self):
        data = bytearray(10)

        for i in range(len(data)):
            data[i] = 10 + i

        try:
            bf = open('file.bin', 'wb')
            bf.write(data)
            bf.close()
        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))
    
    def readByteArrFile(self):
        data = bytearray(10)

        try:
            bf = open('file.bin', 'rb')
            bf.readinto(data)
            bf.close()

            for b in data:
                print(hex(b), end=' ')
        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))
    
    def readByteArrStr(self):
        try:
            bf = open('file.bin', 'rb')
            data = bytearray(bf.read())
            data2 = bytearray(bf.read(5))
            bf.close()

            for b in data:
                print(hex(b), end=' ')
            
            for c in data2:
                print(hex(c), end=' ')

        except IOError as e:
            print("I/O error occurred:", strerror(e.errno))

byteArrTest = ByteArrayTest()
byteArrTest.readByteArrStr()