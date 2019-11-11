# Rock Paper Scissors by Kofi
import random, time, sys
print('ROCK, PAPER, SCISSORS')
print()
print('-Rock beats scissors.')
print('-Paper beats scissors.')
print('-Scissors beats paper.')
# These variables keep track of the number of wins,losses and ties

wins = 0
losses = 0
ties = 0

while True: # The main game loop:
    while True: # Keep asking until player enters R/P/S/Q:
        print(f'{wins} Wins, {losses} Losses, {ties} Ties')
        print('Enter your move: (R)ock  (P)aper  (S)cissors or (Q)uit')
        playerMove = input().upper()
        if playerMove == 'Q':
            sys.exit()
        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R,P,S, or Q')

    if playerMove == 'R':
        playerMove = 'ROCK'
        print("ROCK versus...")
        # PlayerMove = 'ROCK'
    elif playerMove == 'P':
        playerMove = 'PAPER'
        print('PAPER versus...')
    elif playerMove == 'S':
        playerMove = 'SCISSORS'
        print('SCISSORS versus...')

    # Count to three with dramatic choices
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    # global computerMove
    # Display what the computer choose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'ROCK'
    elif randomNumber == 2:
        computerMove = 'PAPER'
    elif randomNumber == 3:
        computerMove = 'SCISSORS'
    print(computerMove)
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties = ties + 1
    elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'PAPER' and computerMove == 'ROCK':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
        print('You win!')
        wins = wins + 1

    elif playerMove == 'ROCK' and computerMove == 'PAPER':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
        print('You Lose!')
        losses = losses + 1

# Display and record the win/loss/tie: