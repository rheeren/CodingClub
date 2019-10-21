sumofsquares = 0
squareofsums = 0

for x in range(101):
  sumofsquares = sumofsquares + x**2
  squareofsums = squareofsums + x

squareofsums = squareofsums**2

print(f"The difference between the sum of the squares and the square of the sum for the first one hundred natural numbers is {(squareofsums-sumofsquares)}")