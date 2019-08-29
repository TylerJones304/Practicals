# OUTPUT_FILE = "name.txt"
# user_name = input("Please enter your name:")
# out_file = open(OUTPUT_FILE, 'w')
# print("Your name is:", user_name, file=out_file)
# out_file.close()


# Solution version

# out_file = open("name.txt", "w")
# name = input("What is your name? ")
# print(name, file=out_file)  # or out_file.write(name)
# out_file.close()

# in_file = open("name.txt", 'r')
# name = (in_file.read())
# in_file.close()
# print(name)
#
#
in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()

print(number1 + number2)

in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
