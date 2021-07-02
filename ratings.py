"""Restaurant rating lister."""

ratings = {}
with open("scores.txt") as f:
    for line in f:
        (key, val) = line.split(':')
        ratings[key] = int(val)

for k, v in sorted(ratings.items()):
    print(k, "is rated at", v)

restaurant = input("Type in a restaurant.\n")

score = int(input("What is the restaurant's score?\n"))

ratings[restaurant] = score
for k, v in sorted(ratings.items()):
    print(k, "is rated at", v)


