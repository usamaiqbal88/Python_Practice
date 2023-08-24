print("--------------------Factorial-----------------")

print("Enter number")
num = int(input())


print("Using Looooooop ------------------------")
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("The for loop factorial of ", num, "is ", fact)


print("Using Recursion---------------")
def factorial(n):
    if  n==0:
        return 1
    return n*factorial(n-1)
print("The recursion factorial of ", num, "is ", factorial(num))


print("Using while loop----------")
fact = 1
while (num > 0):
    fact = fact*num
    num = num-1

print("The while loop factorial of that number is ", fact)






















print("------------------------------")
print("------------------------------")

print("For looop")
num=4
fact = 1

for i in range(1,num+1):
    fact=fact*i
print(fact)

print("While loop")
fact = 1
num = 4
while(num>0):
    fact=fact*num
    num=num-1
print(fact)        

print("Recursive")
n=4
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(n))

    


