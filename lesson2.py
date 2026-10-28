# Exercise 1
number = int(input("What is your number?"))
if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("number is zero")

# Exercise 2
temperature = int(input("What is your temperature in Fahrenheit?"))
if temperature < 50:
    print("temperature is cold")
elif temperature >= 50 and temperature <= 80:
    print("temperature is nice")
elif temperature > 80:
    print("temperature is hot")

# Exercise 3
vowels = "aeiou"
letter = input("What is your letter?")

if letter.lower() in vowels:
    print("Vowel")
else:
    print("Not Vowel")

# Exercise 4
year = int(input("What is the year?"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")

# Exercise 5
number = int(input("What is your number?"))
message = ("number is positive" if number > 0
           else "number is negative" if number < 0
           else "number is zero")
print(message)

vowels = "aeiou"
letter = input("What is your letter?")
message = ('Vowel' if letter in vowels else 'letter')
print(message)
