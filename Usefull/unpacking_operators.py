num_list = [1,2,3,4,5]

def num_sum(num1,num2,num3,num4,num5):
    return num1 + num2 + num3 + num4 + num5

# old-fashion way
print(num_sum(num_list[0], num_list[1], num_list[2], num_list[3], num_list[4]))

#unpacking way
print(num_sum(*num_list))

first, *unused, last = [1, 2, 3, 5, 7]
print(first)
print(*unused)
print(last)