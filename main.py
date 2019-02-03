# import module we need
import random

# file i/o functions for hostorical results
# def load_results():
#    text_file = open("history.txt", "r")
#    history = text_file.read().split(",")
#    text_file.close()
#    return history

# def save_results( w, t, l):
#    text_file = open('history.txt, 'w')
#    text_file.write( w + ',' + t + ',' + 1)
#    text_file.close

# welcome message
# results = load_results()
wins = 0  # int(results[0])
ties = 0  # int(retuls[1])
losses = 0  # int(results[2])
print('Welcome to Rock, Paper, Scissors!')
print('Wins: %s, Ties: %s, Losses: %s' % (wins, ties, losses))
print('Pease choose to continue...')

# initialize user, computer choices
computer = random.randint(1, 3)
user = int(input('[1] Rock [2] Paper [3] Scissors [9] Quit\n'))

# gameplay loop
while not user == 9:
    # user chooses ROCK
    if user == 1:
        if computer == 1:
            print('Computer chose rock...tie')
            ties += 1
        elif computer == 2:
            print('Computer chose paper...computer wins :(')
            wins += 1
        else:
            print('Computer chose scissors...computer wins :(')
            losses += 1

# user chooses PAPER
    if user == 2:
        if computer == 1:
            print('Computer chose rock...you win :)')
            wins += 1
        elif computer == 2:
            print('Computer chose paper...tie!')
            ties += 1
        else:
            print('Computer chose scissors...computer wins :(')
            losses += 1

# user chooses SCISSORS
    if user == 3:
        if computer == 1:
            print('Computer chose rock...computer wins :(')
            losses += 1
        elif computer == 2:
            print('Computer chose paper...you win!')
            wins += 1
        else:
            print('Computer chose scissors...its a tie!')
            ties += 1
    else:
        print('Entry not a valid choice')
    # print updated stats
    print("wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

# promt user to make another selection
    print('Please choose to continue...')
    # initialize user, computer choices
    computer = random.randint(1, 3)
    user = int(input('[1] Rock [2] Paper [3] Scissors [9] Quit\n'))

# game over, save results
# save_results(wins, ties, losses)
