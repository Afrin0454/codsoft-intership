import random

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS GAME =====")

while True:

    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        user = "Rock"
    elif choice == "2":
        user = "Paper"
    elif choice == "3":
        user = "Scissors"
    else:
        print("Invalid Choice!")
        continue

    computer = random.choice(["Rock", "Paper", "Scissors"])

    print("\nYou chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore")
    print("You      :", user_score)
    print("Computer :", computer_score)

    play = input("\nDo you want to play again? (yes/no): ").lower()

    if play != "yes":
        print("\nFinal Score")
        print("You      :", user_score)
        print("Computer :", computer_score)
        print("Thank you for playing!")
        break