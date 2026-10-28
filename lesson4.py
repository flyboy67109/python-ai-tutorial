# Exercise 1
nums = [10, 20, 30, 40, 50]
print(nums[0])     # [10, 20]
print(nums[-1])
print(nums[1:4])     # [30, 40, 50]
print(nums[::-1])   # reversed

# Exercise 2
words = []
while True:
    word = input("Enter a word: ")
    if word == "done":
        break

    words.append(word)

print(words)

# Exercise 3
nums = [4, 8, 15, 16, 23, 42]

print(sum(nums))
print(min(nums))
print(max(nums))
print(sum(nums) / len(nums))

# Exercise 4
ages = {"Tom": 29, "Dick": 30, "Harry": 31}

for name, age in ages.items():
    print(f"{name} is {age} years old")

ages["George"] = 29                    # add a fourth person

print(ages.get("Sally", "n/a"))        # n/a (Sally isn't in the dict)
print(ages.get("Tom", "n/a"))          # 29

# Exercise 5
squares = [n * n for n in range(20) if n % 3 == 0]
print(squares)

# Exercise 6
text = "the quick brown fox jumps over the lazy dog"

counts = {}
for ch in text:
    if ch != " ":
        counts[ch] = counts.get(ch, 0) + 1

top3 = sorted(counts, key=counts.get, reverse=True)[:3]
print(top3)      # ['o', 'e', 't']

# Exercise 7
grid = [[row * col for col in range(1, 4)] for row in range(1, 4)]

for row in grid:
    print(row)
