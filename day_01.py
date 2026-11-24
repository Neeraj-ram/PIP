name = input("Enter your name: ")
age = int(input("Enter your age:"))
height = float(input("Enter your height in meter :"))
city = input("Enter your city name:")

print(f"My name is {name}, my age is {age}, my height is {height} in meter and i live in city {city}.")

###
a = 11
b = 25
c = 22

print("Sum of the numbers is:", a+b+c)
print("Difference of the numbers is:", a-b-c)
print("Product of the numbers is:", a*b*c)
print("Division of the numbers is:", a/b/c)

###
length = int(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area of the rectangle is:", area)
print("Perimeter of the rectangle is:", perimeter)


####
price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount Amount:", discount_amount)
print("Final Price:", final_price)


###

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

si = (p * r * t) / 100

print("Simple Interest:", si)
