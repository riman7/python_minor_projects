import random
while True:
    choice = input("Wanna Roll dice? (Y/N): ").lower()
    if choice == "n":
        break
    elif choice == "y":
        print(f"({random.randrange(1,6)}, {random.randrange(1,6)})")
    else:
        print("Invalid choice!")
print("Thank for Playing - By Riman Maharjan.")