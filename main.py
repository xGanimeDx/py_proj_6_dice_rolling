import random

play = True

while play:
    first_computer = random.randint(1, 6)
    second_computer = random.randint(1, 6)
    first_human = random.randint(1, 6)
    second_human = random.randint(1, 6)

    print(f'Computer has: {first_computer} and {second_computer}')
    print(f'You have: {first_human} and {second_human}')

    sum_computer = first_computer + second_computer
    sum_human = first_human + second_human

    if sum_human > sum_computer:
        print('You win!')
    elif sum_computer > sum_human:
        print('Computer wins!')
    else:
        print('Draw')

    replay = input('Do you want to play again? Y or N ')
    if replay == 'N':
        play = False