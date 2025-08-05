import random

user_score = 0
computer_score = 0
tie_score = 0

while True:
    
    print("\nYou have three choices to select!")

    print("1. Rock")

    print("2. Paper")

    print("3. Scissors")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        user_move = "Rock"

    elif choice == "2":
        user_move = "Paper"

    elif choice == "3":
        user_move = "Scissor"

    else:
        print("❌ Invalid choice!")
        continue

    computer_move = random.choice(["Rock", "Paper", "Scissor"])

    print(f"\n🧍 Your move: {user_move}")
    print(f"🤖 Computer's move: {computer_move}")

    if user_move == computer_move:
        print("🤝 Match Tie!!")
        tie_score += 1

    elif user_move == "Rock" and computer_move == "Paper":
        print("❌ You lose the match!!")
        computer_score += 1

    elif user_move == "Rock" and computer_move == "Scissor":
        print("✅ You win the match!!")
        user_score += 1

    elif user_move == "Paper" and computer_move == "Rock":
        print("✅ You win the match!!")
        user_score += 1

    elif user_move == "Paper" and computer_move == "Scissor":
        print("❌ You lose the match!!")
        computer_score += 1

    elif user_move == "Scissor" and computer_move == "Paper":
        print("✅ You win the match!!")
        user_score += 1

    elif user_move == "Scissor" and computer_move == "Rock":
        print("❌ You lose the match!!")
        computer_score += 1

    # Show scoreboard
    print("\n📊 Current Scoreboard:")

    print(f"👤 You: {user_score}")

    print(f"🤖 Computer: {computer_score}")

    print(f"⚖️  Ties: {tie_score}")

    again = input("\nDo you want to play again? (y/n): ")

    if again.lower() != "y":

        print("\n🏁 Final Scoreboard:")

        print(f"👤 You: {user_score}")

        print(f"🤖 Computer: {computer_score}")

        print(f"⚖️  Ties: {tie_score}")

        print("\n🎉 Thanks for playing! See you next time!")

        break
