
print("Check Anagram Strings")

str1 = 'silent anD'
str2 = 'listen daN'

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

str1= sorted(str1)
str2= sorted(str2)

# dic1 = []
# dic2 = []
# for char in str1:
#     dic1.append(char)
# for char in str2:
#     dic2.append(char)
# print(dic1,dic2)
# if dic1==dic2:
#     print("strings are anagram")
# else:
#     print("Not anagram.")

print(str1,str2)
if str1 == str2:
    print("Strings are anagram.")
else:
    print("Not Anagram.")