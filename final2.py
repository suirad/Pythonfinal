"Implements Question 2"
import math
nums = range(1, 21)
right_tris = list()

for n in nums:
    right_tris.append(math.sqrt(n*n + n*n))

for n in nums:
    print("a: {}, b: {}, c:{}".format(n, n, right_tris[nums.index(n)]))

