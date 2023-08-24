print("Iterators")

#Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol,
#  which consist of the methods __iter__() and __next__().

mylist=[10,"sam",30,40,50]

iterator= iter(mylist)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

# iterator is memory efficient, while traversing at a time, load one element memory at a time
# store one variable in memory at a time.
# In for loop, all the indexes are loaded in memory in one time.

for i in mylist:
    print(i)

# string= "burgur"    # string alphabets can be iterated

# it= iter(string)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# StopIteration

print("-----------------")

class counting:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a <= 10:
            x=self.a 
            self.a += 1
            return x
        else:
            raise StopIteration

count= counting()
itr=iter(count)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

for f in itr:
    print(f)
