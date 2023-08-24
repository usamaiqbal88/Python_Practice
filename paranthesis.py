
print("Paranthesis Check-----------------------------------")

count = 0 

paran = "(){}[])" 

for p in paran:
    if p=="{" or p=="[" or p=="(":
        count +=1
    elif p == "}" or p == "]" or p == ")":
        count -=1
    
if count==0:
    print("Paranthesis Balanced.")
else:
    print("Paranthesis not balanced.")
    
                        
print("Check using Stack----------------------------------")

stack = []

paran = "()]"

for p in paran:
    if p == "{" or p == "[" or p == "(":
        stack.append(p)
    elif p == "}" or p == "]" or p == ")":
        if len(stack)==0:
            print("Paranthesis not balanced.")
            quit()
        stack.pop()
        

if len(stack)==0:
    print("Paranthesis balanced.")

