# creating an empty list

my_list = []

# inserting values to my list

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

# adding a avlue to my_list at a specific position

my_list.insert(1, 15)
print(my_list)
# joining my_list with another
myList2 = [50, 60, 70]

my_list.extend(myList2)

print(my_list)
#  removing an element from my_list
my_list.remove(70)
print(my_list)

#  sort list in ascending order
my_list.sort()
print(my_list)

print (my_list.index(30))