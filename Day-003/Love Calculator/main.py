# Love Calculator
# 💪 This is a Difficult Challenge 💪

print("Welcome to Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
both_name = (name1+name2).lower()
true_count = 0
love_count = 0

for letter in both_name:
    if letter == 't' or letter == 'r' or letter == 'u' or letter == 'e':
        true_count += 1
for letter in both_name:
    if letter == 'l' or letter == 'o' or letter == 'v' or letter == 'e':
        love_count += 1

# count()
# true_count += both_name.count("t")
# true_count += both_name.count("r")
# true_count += both_name.count("u")
# true_count += both_name.count("e")
# love_count += both_name.count("l")
# love_count += both_name.count("o")
# love_count += both_name.count("v")
# love_count += both_name.count("e")

score = true_count*10 + love_count

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
