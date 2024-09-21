import random

answer = random.randint(1, 100)

# print(answer)

while True:

    user_input = input('Enter a number: ')
    user_input = int(user_input)

    # print(user_input)
    print(f'You have entered {user_input}')

    if user_input == answer:
        print('Correct!')
        break
    elif user_input > answer:
        print('Too large!')
    else:
        print('Too small!')
