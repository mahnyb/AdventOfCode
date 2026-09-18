input = open("2015/Day1_input.txt")
input = input.read()


floor = 0 
# # ( means + 1 
# # ) means - 1

for i in range(len(input)):

    if input[i] == "(":
        floor += 1
    elif input[i] == ")":
        floor -= 1

print (floor)
