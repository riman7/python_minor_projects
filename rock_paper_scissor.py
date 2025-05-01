import random

choices = ("r", "p", "s")                               #Tuple (not changeable list)
wining_case = [("r", "s"), ("p", "r"), ("s", "p")]      #List of tuples
emoji = {"r": "🪨", "p": "📄", "s": "✂️"}              #dictionary:{Key: vaulue,...}
score = {"user": 0, "computer": 0}
while True:
    user_choice = input("Rock, Paper or Scissor? (r, p or s): ").lower().strip()
    if user_choice not in choices:
        print("❌Invalid!")
    else:
        computer_choice = random.choice(choices)
        print(f"You choose {user_choice}{emoji[user_choice]}")
        print(f"I choose {computer_choice}{emoji[computer_choice]}")

        if user_choice == computer_choice:
            print("🤝It's a Draw")
        elif(user_choice, computer_choice) in wining_case:
            print("🎉Congratulation! You won.")
            score["user"] += 1
        else:
            print("😈I Won!")
            score["computer"] += 1

        print(f"Score → You: {score['user']} | Me: {score['computer']}")

        while True:
            x = input("\nDo you want to continue? (Y/N): ").lower().strip()
            if x == "n":
                print("👋 Thanks for playing!")
                exit()
            elif x == "y":
                print("\n--- Next Round ---")
                break
            else:
                print("❌ Invalid input! Please type 'Y' or 'N'.")