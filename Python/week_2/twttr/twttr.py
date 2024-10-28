

str1 = input("input : ")

list1 = list(str1)

list2 = []

for i in list1:
    if i.lower() not in ('a','o','u','i','e'):
        list2.append(i)
print("".join(list2) ,end="")
