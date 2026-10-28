# Exercise 1
for n in range(1, 11):
    print(n)

for n in range(10,0,-1):
    print(n)

# Exercise 2
number = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{i} x {number} = {i*number}")

# Exercise 3
total = int(0)
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        print(total)
        break
    else:
        total = total + number

# Exercise 4
vowels = "aeiou"
word = input("What is your word?")
count = 0
for letter in word:
    if letter.lower() in vowels:
        count += 1

print(f"{count} vowels")

# Exercise 5
names = ["Ann", "Bob", "Cy"]
scores = [90, 72, 85]
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name}: {score}")

# Exercise 6
for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
