
def main():
      #set a buffer size so memory does not overflow
      #the graphic is 476KB
      buffersize=50000
      picturefile=open('waterlilies.jpg','rb')
      newfilename=input("Enter the new file name to copy image to: ")
      copiedfile=open(newfilename, 'wb') #open binary file for writing

      #read 50000 bytes at a time
      buffer=picturefile.read(buffersize)
      while len(buffer):
            copiedfile.write(buffer)
            print('.', end =' ')
            buffer=picturefile.read(buffersize)
      
main()
