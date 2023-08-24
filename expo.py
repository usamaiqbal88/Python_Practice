
base = int(input("Enter Base = "))
expo = int(input("Enter Exponent = "))

r = 1

for i in range(expo,0,-1):
    print(i)
    r = r * base
    print(r)

# while expo !=0:
#     r = r * base
#     expo -= 1
        
print("Result = ",r)    

# r = pow(base,expo)
# print(r)

arr=[2,4,3,6,9]

for i in range(len(arr)-1,-1,-1):
    print(arr[i])

print(arr[-1])
# for i in range(6,0,-1):
#     print(i)