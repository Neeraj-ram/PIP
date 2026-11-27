###List
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers[0] = 5
print(numbers)
print(numbers[1])

###Tuple
user = ("Arun", 25, "Developer")

print(user)
print(user[0])
print(user[1])
print(user[2])

###Set
statuses = ["success","failed","success","pending","failed"]
unique_statuses = set(statuses)
print(unique_statuses)

###Dictionaries
config = {"model": "ris-model","temperature": 0.7,"max_tokens": 100}
print(config["model"])

###