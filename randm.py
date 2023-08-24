import random

print("random numbers----------")

# random.random()                   rondom float number
# random.randint()                  random integer number between range
# random.randrange()                random odd even number in range  (1st number, 2nd number, odd/even)
# random.uniform()                  random float number between range
# random.sample()                   list of random numbers (range,range, numbers how much)
# random.shuffle()                  shuffle elements
# random.choice()                   select any number from list

n = random.random()
print("float random number = ", n)

n = random.randint(10, 15)
print("Random integer number between argument range = ", n)

# randomlist = []
# for i in range(0,5):
# n = random.randint(1,30)
# randomlist.append(n)
# print(randomlist)

n = random.randrange(5, 10, 1)
print("Random number odd = ", n)

n = random.uniform(5, 8)
print("Random float number = ", n)

n = random.sample(range(1, 11), 10)
print("List of random numbers = ", n)

l = [1, 3, 5, 7, 9, 0]
print("The list before shuffling : ", l)
random.shuffle(l)
print("The list after shufling : ", l)

print("One choice from list : ", random.choice(l))
