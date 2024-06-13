def get_feedback(secret, guess):
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_digit = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - correct_position
    return correct_position, correct_digit

def player_turn(player, secret_length):
    print(f"\n{player}, it's your turn to set the secret number.")
    while True:
        secret = input(f"Enter a {secret_length}-digit secret number: ")
        if len(secret) == secret_length and secret.isdigit():
            break
        else:
            print(f"Invalid input. Please enter exactly {secret_length} digits.")
    
    attempts = 0
    while True:
        guess = input(f"\n{player}, enter your guess: ")
        if len(guess) != secret_length or not guess.isdigit():
            print(f"Invalid input. Please enter exactly {secret_length} digits.")
            continue
        
        attempts += 1
        if guess == secret:
            print(f"Congratulations {player}! You've guessed the number in {attempts} attempts.")
            return attempts
        
        correct_position, correct_digit = get_feedback(secret, guess)
        print(f"Feedback: {correct_position} digit(s) in the correct position, {correct_digit} correct digit(s) but in the wrong position.")

def mastermind_game():
    secret_length = 4  # You can change the length of the secret number here

    # Player 1's turn to set the number and Player 2 to guess
    player1 = "Player 1"
    player2 = "Player 2"
    
    print(f"\n{player1} and {player2}, welcome to the Mastermind game!")
    
    print(f"\n{player1}'s turn to set the number and {player2} to guess.")
    attempts_player2 = player_turn(player2, secret_length)
    
    print(f"\n{player2}'s turn to set the number and {player1} to guess.")
    attempts_player1 = player_turn(player1, secret_length)
    
    if attempts_player1 < attempts_player2:
        print(f"\n{player1} wins the game in {attempts_player1} attempts! Congratulations!")
    elif attempts_player1 > attempts_player2:
        print(f"\n{player2} wins the game in {attempts_player2} attempts! Congratulations!")
    else:
        print(f"\nIt's a draw! Both players guessed the numbers in {attempts_player1} attempts.")

if __name__ == "__main__":
    mastermind_game()
