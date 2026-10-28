# Exercise 1
def average(nums):
    total = 0
    for num in nums:
        total += num

    return total/len(nums)

print(average([1,2,3]))
print(average([1,2,3,4,5,6]))

# Exercise 2
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

triple = make_multiplier(3)
double = make_multiplier(2)

print(triple(5))    # 15
print(double(5))    # 10
print(triple(10))   # 30

# Exercise 3
words = ["pear", "fig", "banana", "kiwi"]
print(sorted(words, key=lambda w: w[-1]))

# Exercise 4
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

print(dot([1, 2, 3], [4, 5, 6]))
