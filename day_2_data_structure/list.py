# Find max, min,sum and reverse a list

data = [14,5,8,3,8,37,42,9,88,75,1,95]

max_num= 9
for i in data:
    if max_num <= i:
        # new_data.append(i)
        max_num = i

print(f"{max_num} is the maximum number in the  list")

min = 5 
for i in data:
    if min >= i:
        min = i
print(f"{min} is the minimum number in the list")

Total = sum(data)
print(f"{Total} is the sum of the numbers in the list")

data.reverse()
print(f"{data} is the reversed list") 