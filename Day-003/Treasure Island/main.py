from logo import logo
print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
if left_right == 'left':
    swim_wait = input("You reached a lake. There is a island in the middle of the lake. "
                      "Type 'wait' to wait for a boat. Type 'swim' to swim across ")
    if swim_wait == 'wait':
        color = input("Well Great you arrived safe. There is a cave with 3 doors. "
                      "red, yellow, blue. Which color do you choose? ")
        if color == 'blue':
            print("Eaten by beasts. Game Over💀")
        elif color == "red":
            print("Burned by fire. Game Over💀")
        elif color == "yellow":
            print("You Win!🏴‍☠️")
        else:
            print("Game Over💀")
    else:
        print("Attacked by trout. Game Over💀")
else:
    print("Fall into a hole. Game Over💀")