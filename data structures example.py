        #This is a 'List' type of data structure


myList = []

myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)

print(myList)

print(myList.index(3))


myList.remove(4)

print(myList)

print()
print()


        #This is a 'Tuple' type of data structure


numbers=(1,2,2,2,2,1,3)

print(numbers.index(2))         # with index()

print()
print()


t1=(1,2,2,2,2,1,3)              # this will count how many same numbers

print(t1.count(1))    

print(t1.count(2))    

print(t1.count(3))




t1=(1,2,2,2,2,1,3)
l1 = list(t1)
l1.insert(3,'ins')
t1 = tuple(l1)
print(t1)


print()
print()





#dictionary

d = {'key':'value'}



d = {'key':'value'}

print(d.keys())

print(d.values())


print()

d = {'firstNum':5, 'secondNum':2}

print(d.keys())

print(d.values())

Total = d['firstNum'] + d['secondNum']

print('Total = ', Total)

print()
print()
print()


#to get values from dictionary object

Total = d.get('firstNum') + d.get('secondNum')

print('Total = ', Total)


print()
print()


#to add item to dictionary


d.update({'item3': 3})


print()
print()
print()


#Converting dictionary object to List object

v=list(d.values())

k=list(d.keys())

print(v[0])

print(k[0])


print()
print()
print()



            # so here the tuple () becomes the list []
t1=(1,2,2,2,2,1,3)  

l1 = list(t1)   

print(l1)

print()
print()

                # this will sort the list [] in order from lowest to higher number
l1.sort()
print(">>>", l1)

print()
print()


sl=l1.sort()

print (">>> ", sl)
