import random

ans = random.randint(1, 100)


response = int(input("guess a numebr from 1 to 100:"))
max = 100
min = 1

while response != ans:
    if response <= 100 and response >= 1:
        if response < ans:
            min = response
            response = int(input(f"pick a number between {min} to {max}: "))
        elif response > ans:
            max = response
            response = int(input(f"pick a number between {min} to {max}: "))
    else:
        print("that's not even in the limit!")


print(f"hooray! my number was {ans} !")