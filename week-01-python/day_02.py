##Loops
rows = 5

for row in range(1, rows + 1):
    for column in range(row):
        print("*", end="")
    print()


### For loops
for number in range(1, 6):
    print(number)

###
number = int(input("Enter a number: "))

if number < 2:
    print("Not prime")
else:
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")

###for loop
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1

    for value in range(1, number + 1):
        factorial = factorial * value

    print("Factorial:", factorial)

###break
for number in range(1, 6):
    if number == 4:
        break
    print(number)


###continue
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

###pass
for number in range(1, 4):
    if number == 2:
        pass
    print(number)

###nested loop
for row in range(1, 4):
    for column in range(1, 4):
        print(row, column)
