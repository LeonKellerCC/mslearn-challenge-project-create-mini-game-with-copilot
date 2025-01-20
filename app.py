import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'

def main():
    score = {'win': 0, 'lose': 0, 'tie': 0}
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid option. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(player_choice, computer_choice)
        score[result] += 1
        
        if result == 'win':
            print("You win!")
        elif result == 'lose':
            print("You lose!")
        else:
            print("It's a tie!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print(f"Final score - Wins: {score['win']}, Losses: {score['lose']}, Ties: {score['tie']}")

if __name__ == "__main__":
    main()