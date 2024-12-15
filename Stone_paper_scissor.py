import random

def get_choices():
  player_choice = input("Enter a choice (rock,paper,scissor):")
  computer_options = ["rock","paper","scissor"]
  computer_choice = random.choice(computer_options)
  choice = {"computer":computer_choice, "player":player_choice}
  return choice

def check_win(player, computer):
 print(f"You chose {player}, Computer chose {computer}")  
 if player == computer:
    return "It's a tie!"
 elif player=="rock": 
   if computer=="paper":
    return "Paper covers rock!, you lose"
   else:
    return "Rock smashes scissor!, you win!"
 elif player=="paper": 
   if computer=="rock":
    return "Paper covers rock!, you win!"
   else:
    return "Scissor cuts paper, you lose"
 elif player=="scissor": 
   if computer=="paper":
    return "Scissor cuts paper!, you win!"
   else:
    return "Rock smashes scissor!, you lose"
   
choices=get_choices()
result=check_win(choices["player"], choices["computer"])
print(result)