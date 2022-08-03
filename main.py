import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

total_persons = len(names)
random_person = random.randint(0, total_persons - 1)  # так как начинается отсчет с 0, нужно от общего числла отнять 1.

print(f"{names[random_person]} is going to buy the meal today!")

