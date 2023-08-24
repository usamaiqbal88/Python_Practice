
print("--------------------------------------")

x = int(input("Enter Number to check = "))

if x < 0:
    pass
elif x > 1:
    for i in range(2, x):
        if (x % i) == 0:
            print("Number is not prime.")
            break
    else:
        print("Number is prime.")
else:
    print("Number is not prime")


print("---------------------------------------")
        
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        
    return True

limit = int(input("enter limit = "))           
count = 0
num = 2

while count<limit:
    if is_prime(num):
        print(num)
        count +=1
    num +=1







print("----------------------------------------")
num = int(input("eter="))
for i in range(2,num):
    if num%i == 0:
        print("Number is not prime.")
        break
else:
    print("Number is prime.") 
        