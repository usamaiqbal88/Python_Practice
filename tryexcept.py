 
from tkinter import EXCEPTION


print("Try, Except, Else, Finally")

print("Enter values: ") 
x = int(input())
y = int( input())

try:
    print(x+z)

except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print("Nothing went wrong")   
    print(x+y)     

finally:
    print("This line is necessary")    
print("fine")
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")