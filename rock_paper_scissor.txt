import random
print("Welcome to Rock Paper Scissor Game")


def get_choices():
    player_choice = input("Enter your choice(rock, paper, scissor): ")
    p_choice = player_choice.lower()
    options = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(options)
    choices = {"player": p_choice, "computer": computer_choice}
    return choices


def chk_win(player, computer):
    print(f" Player chose: {player} Computer chose: {computer}")
    if player == computer:
        return "Its a tie"
    elif player == 'rock':
        if computer == 'scissor':
            return "Rock  smashes Scissor.You Win!"
        else:
            return"Paper wraps the Rock.You Lose"
    elif player == 'paper':
        if computer == 'rock':
            return "Paper wraps the Rock.You Win!"
        else:
            return "Scissor cut the paper.You Lose"
    elif player == 'scissor':
        if computer == 'paper':
            return "Scissor cut the paper.You Win!"
        else:
            return "Rock  smashes Scissor.You Lose "


choices = get_choices()
result = chk_win(choices["player"], choices["computer"])
print(result)


