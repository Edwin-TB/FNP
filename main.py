i = 1
x1 = 1
x2 = 1
pee = [x1, x2]

while i < 9999:
    #print(x1)
    #print(x2)
    x1 = x1 + x2
    x2 = x1 + x2
    pee.append(x1)
    pee.append(x2)
    i += 1
# print(pee)
num = int(input("Which fibonacci number would you like?: "))
if num == 1:
    print("The 1st fibonacci number is: " + str(pee[num - 1]))
elif num == 2:
    print("The 2nd fibonacci number is: " + str(pee[num - 1]))
elif num == 3:
    print("The 3rd fibonacci number is: " + str(pee[num - 1]))
elif num > 3:
    print("The " + str(num) + "th fibonacci number is: " + str(pee[num - 1]))
