import random 

options = ["rock" , "paper" , "scissors"]

def game():
    while True:

        guest_choice = input("Enter rock, paper or scissors: ")
        computer_choice = random.choice(options)

        print(guest_choice)
        print(computer_choice)

        if guest_choice == computer_choice:
            print("It's tie")
        elif guest_choice == "rock" and computer_choice == "scissors":
            print(f"You win! Computer select: {computer_choice}")

        elif guest_choice == "paper" and computer_choice == "rock":
            print(f"You win! Computer select: {computer_choice}")

        elif guest_choice == "scissors" and computer_choice == "paper":
            print(f"You win! Computer select: {computer_choice}")
        else:
            print(f"You lose! Computer select: {computer_choice}")

            
game()