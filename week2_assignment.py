my_list = []
print(my_list)

#appending list to add (10,20,30,40)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#adding 15 to my current list
my_list.insert(1,15) # 15 will be added to second position
print(my_list)

#extending my list by adding (50,60,70)
my_list.extend([50,60,70])
print(my_list)

# removing the last element
my_list.pop() 
print(my_list)