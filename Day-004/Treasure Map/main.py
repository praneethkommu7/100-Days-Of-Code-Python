row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

number = input("Where do you want to put the treasure? ")

# The first digit in the input will specify the column
# The second digit in the input will specify the row
map[int(number[1]) - 1][int(number[0]) - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")