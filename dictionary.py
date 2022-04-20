#list
list1 = ["juan","pedro","luis","hugo"]
print(list1)


#nested list
nl1 = ["juan","pedro",["pato","perro","gato"],"luis","hugo"]
print(nl1[2][1])

#append vaca item to nested list
nl1[2].append("vaca")
print(nl1[2])

print(nl1)

#Insert item at the begining of the list
nl1.insert(0,"bestia")
print(nl1)


#Iterate through nested list

for list in nl1:
    print(list, end=" ")


#List slicing
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7])
# Prints ['c', 'd', 'e', 'f', 'g']