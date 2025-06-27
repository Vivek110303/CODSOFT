import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("------------------------------------")

    wins = 0
    losses = 0
    ties = 0
    round_number = 1

    while True:
        print(f"\n🔁 Round {round_number}")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("😐 It's a tie!")
            ties += 1
        elif winner == "user":
            print("🎉 You win this round!")
            wins += 1
        else:
            print("💻 Computer wins this round!")
            losses += 1

        print(f"📊 Scoreboard:")
        print(f"✔️ Wins: {wins}")
        print(f"❌ Losses: {losses}")
        print(f"🤝 Ties: {ties}")

        play_again = input("\nDo you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print("\n🏁 Final Summary:")
            print(f"🧑 You won {wins} time(s).")
            print(f"💻 Computer won {losses} time(s).")
            print(f"🤝 Tied {ties} time(s).")

            if wins > losses:
                print("🏆 Overall Winner: YOU!")
            elif wins < losses:
                print("😞 Overall Winner: COMPUTER!")
            else:
                print("🤝 The game ended in a DRAW!")

            break

        round_number += 1


play_game()
