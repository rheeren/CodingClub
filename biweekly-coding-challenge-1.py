multiplesum = 0
for x in range(999):
  if x % 3 == 0 or x % 5 == 0:
    multiplesum = multiplesum + x
print(multiplesum)