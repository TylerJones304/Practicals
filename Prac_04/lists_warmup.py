numbers = [3, 1, 4, 1, 5, 9, 2]
'9' in numbers

# numbers [0] will print 3, as it's the first number
# numbers [-1] will print 2, as -1 prints the last number in the list
# numbers [3] will print the second 1 in the list as the fourth number
# numbers [:-1] will print every number except for the 2 at the end
# numbers [3:4] will print the second 1
# 5 in numbers will print true as 5 is in the list
# 7 in numbers will return false as it is not in the list
# numbers + [6, 5, 3] will print the whole list with these numbers added on
# at the end

numbers[0] = 'ten'
print(numbers)

numbers[-1] = '1'
print(numbers)

print(numbers[2:])

# numbers = [3, 1, 4, 1, 5, 9, 2]
# 9 in numbers
# True
