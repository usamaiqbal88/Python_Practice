# from asyncore import file_dispatcher
from multiprocessing import context

#  modes

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


print("File handling-------")

f= open("data.txt", "a")
# content=f.writelines("This is my 7th semester.")
# content=f.read()         
# context=f.readline()    read 1 line
# content=f.readlines()     read all lines
# print(content)

f.close()

f1=open("abc.txt","r")    
# f1.write("Hi, this is a file")
c=f1.read()
print(c)
print(f1.tell())

f1.close()

# for data in f:          # copying data from 1 file to other.
#     f1.write(data)