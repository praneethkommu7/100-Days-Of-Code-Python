# Leap Year
# 💪This is a Difficult Challenge 💪

year = int(input("Which year do you want to check? "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year.")
    # if year%100!=0:
    #     print("Leap year.")
    # else:
    #     if year%400==0:
    #         print("Leap year.")
    #     else:
    #         print("Not leap year.")

else:
    print("Not leap year.")
