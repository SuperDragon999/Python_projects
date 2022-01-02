import random,time

print('Epic number guesser battle!\nGuess numbers from 1 to 1000!')
time.sleep(1)
def countdown():
    for i in reversed(range(1, 4)):
        string = '{:02d}:{:02d}'.format(0, i)
        print(string)
        time.sleep(1)
    print('Go!')

player_count = 0
player_count_1 = 0
difference = 0
name_1 = input('Player one name?')
name_2 = input('Player two name?')
num = random.randint(1, 1000)
winner = None
guess = 0

print(f'{name_1} get ready!')
countdown()
while guess != num:
    player_count += 1
    guess = input(f'Enter your guess: ')
    if guess.isnumeric():
        guess = int(guess)
    else:
        print('Numbers only, please!')
        player_count -= 1
    if guess > num:
        print('Too high, try again!')
    elif guess < num:
        print('Too low, try again!')
else:
    print('Great job!')
    time.sleep(1.5)

num = random.randint(1, 1000)

print(f'{name_2} get ready!')
countdown()
while guess != num:
    player_count_1 += 1
    guess = input(f'Enter your guess: ')
    if guess.isnumeric():
        guess = int(guess)
    else:
        print('Numbers only, please!')
    if guess > num:
        print('Too high, try again!')
    elif guess < num:
        print('Too low, try again!')
else:
    print('Great job!')
    time.sleep(1.5)

print('Game completed!\nThe winner is...' )
if player_count > player_count_1:
    difference = player_count - player_count_1
    winner = name_2
    loser = name_1
    loser_points = player_count
    winner_points = player_count_1
elif player_count < player_count_1:
    difference = player_count_1 - player_count
    winner = name_1
    loser = name_2
    loser_points = player_count_1
    winner_points = player_count
elif player_count == player_count_1:
    print(f'You tied!\nBoth of you guessed {player_count} times.')
    time.sleep(0.5)
    exit()
time.sleep(2.5)
print(f'{winner}!!!🎉🎉🎉')
time.sleep(0.5)
print(f'Results: {winner}: {winner_points} guesses, {loser}: {loser_points} guesses')