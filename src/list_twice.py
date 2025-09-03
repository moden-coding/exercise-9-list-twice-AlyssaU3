# Write your solution here
list = []
while True:
    user=int(input("New Item: "))
    if user != 0:
        list.append(user)
        
        print(f"The list now: {list}")
        #list.sort()
        print(f"The list in order: {sorted(list)}")
    else:
        print("Bye!")
    if user==0:
        break
        
        

