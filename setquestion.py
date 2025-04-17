list_1 = [6,4,10,5,8,67,17,12,6,10]
list_2 = [2,4,8,17,8,12,75,67]

# converting list to set
set_1 = set(list_1)
set_2 = set(list_2)

# Find the common elements in the two lists using set intersection & operator
common_element = set_1 & set_2

print(f"{common_element} is the common elements in the two lists")

# find unique elements in both lists 
set = set_1 - common_element
print(f"{set} is the difference between the two sets")

sets = set_2 - common_element
print(f"{sets} is the difference between the two sets")    