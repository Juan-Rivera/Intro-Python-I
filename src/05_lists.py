# YOUR CODE HERE
empty = []

nums = [10, 60, 20, 5]

#print(nums)

nums.append(77)

#print(nums)

for elem in nums:
    print(elem)

print("------------------------")

for n in range(2, 10):
    print(n)

print("------------------------")

for i in range(len(nums)):
    print(i, nums[i])

print("------------------------")

for index, value in enumerate(nums):
    print(index, value)