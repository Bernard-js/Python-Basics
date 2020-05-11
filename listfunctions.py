lucky_numbers = [2, 4, 95, 73, 33, 19]
friends = ["Karen", "Matt", "Roddrick", "Thomas", "Joshua"]

friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Thomas")
print(friends)

friends2 = friends.copy()
print(friends2)

friends.pop()
print(friends)

print(friends.index("Joshua"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

print(friends.count("Jim"))

friends.clear()
print(friends)



