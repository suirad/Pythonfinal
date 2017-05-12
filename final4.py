"Implements Question 4"
from random import randint

nums = list()
dupes = set()

for n in range(1, 30):
    nums.append(randint(1,30))

print("Numlist: " + str(nums))
for n in nums:
    if nums.count(n) > 1:
        dupes.add(n)

print("Duplicates: " + str(dupes))
