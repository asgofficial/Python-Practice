fruits = {
    "Apple", "Mango", "Orange", "Banana", "Pineapple",
    "Guava", "Grapes", "Papaya", "Strawberry", "Watermelon"
}

summer_fruit = {
    "Mango", "Watermelon", "Papaya", "Pineapple", "Litchi"
}


winter_fruit = {
    "Apple", "Orange", "Strawberry", "Guava", "Pomegranate"
}


print("Fruits:", fruits)
print("Summer Fruits:", summer_fruit)
print("Winter Fruits:", winter_fruit)

print("\nFruits present in both fruits and winter fruits:")
print(fruits.intersection(winter_fruit))

print("\nFruits present only in summer fruit but not in fruits:")
print(summer_fruit.difference(fruits))

print("\nFruits present in summer fruits, winter fruits and fruits:")
print(fruits.intersection(summer_fruit, winter_fruit))


print("\nIs Orange present in fruits?")

if "Orange" in fruits:
    print("Yes, Orange is present in fruits.")
else:
    print("No, Orange is not present in fruits.")


print("\nPineapple is present in:")

if "Pineapple" in fruits:
    print("- Fruits")

if "Pineapple" in summer_fruit:
    print("- Summer Fruits")

if "Pineapple" in winter_fruit:
    print("- Winter Fruits")