from characters import letters, symbols, numbers
import random

print("Welcome to the PyPassword Generator!")
num_letters = int(input('How many letters would you like in your password?\n'))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
final_pass = ''
for _ in range(num_letters - (num_numbers + num_symbols)):
    final_pass += letters[random.randint(0, len(letters) - 1)]

for _ in range(num_symbols):
    final_pass += symbols[random.randint(0, len(symbols) - 1)]

for _ in range(num_numbers):
    final_pass += numbers[random.randint(0, len(numbers) - 1)]

print(f"Here is your password: {final_pass}")

# Hard Level - Order of characters randomised:
l = list(final_pass)
random.shuffle(l)
shuffled_pass = ''.join(l)
print(f"Shuffled password is: {shuffled_pass}")
