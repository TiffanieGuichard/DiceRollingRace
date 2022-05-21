import random

def init_size():
  number_cells = int(input("enter the size of the court:"))
  while number_cells < 3:
    print("Sorry this size is not valide. The cell must be at least equal to 3")
    number_cells = int(input("enter the size of the court:"))
  return number_cells  

def players_turn():
  dice = input("say 'throw' to throw the dice:")
  #dice = dice.lower()
  while not(dice.lower() == "throw"):
    print("Sorry this is not valide.")
    dice = input("say 'throw' to throw the dice:")
  number = random.randint(1,6)
  return number

def computer_turn():
  number = random.randint(1,6)
  return number

def winner(total_number_p, total_number_c):
  winner = max(total_number_p, total_number_c)
  if winner == total_number_p:
    print("You won the race!")
  else: 
    print("Computer won the race!")
  print("You are on the cell number",total_number_p )
  print("Computer is on the cell number",total_number_c )

def main_code():
  number_cells = init_size()
  total_number_p = 1
  total_number_c = 1
  while total_number_p < number_cells or total_number_c < number_cells:
    number_dice_p = players_turn()
    total_number_p += number_dice_p
    print("You throw the number", number_dice_p, "you are on the cell", total_number_p, "out of", number_cells)
    if total_number_p >= number_cells:
      break
    number_dice_c = computer_turn()
    total_number_c += number_dice_c
    print("The computer throw the number", number_dice_c, "it is on the cell", total_number_c, "out of", number_cells)
    if total_number_c >= number_cells:
      break
  winner(total_number_p, total_number_c)

main_code()
rep = input("Do you want to play again?: (Yes/No)")
while not(rep.lower() == "yes" or rep.lower() == "no"):
  print("Sorry this is invalid:", rep)
  rep = input("Do you want to play again?: (Yes/No)")
while rep.lower() == "yes":
  main_code()
  rep = input("Do you want to play again?: (Yes/No)")
  while not(rep.lower() == "yes" or rep.lower() == "no"):
    print("Sorry this is invalid:", rep)
    rep = input("Do you want to play again?: (Yes/No)")
