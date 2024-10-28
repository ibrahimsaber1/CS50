mystr= input("camal case: ")

mylist = list(mystr)

mylist2 = []
for i in range(len(mylist)):
    if mylist[i] == mylist[i].upper():
        mylist[i] = mylist[i].lower()
        mylist2.append('_')
        mylist2.append( mylist[i])
    else:
        mylist2.append( mylist[i])
print("snake_case:", "".join(mylist2))
