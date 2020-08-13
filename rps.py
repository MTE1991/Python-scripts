from random import choice

rps = ["Rock", "Paper", "Scissor"]

print("\t -: Rock, Paper, Scissor game :-")

user_choice = str(input("""Choose one of these three:

A. Rock
B. Paper
C. Scissor

Your choice: """))

if user_choice == "A":
  r = rps[0]
  c = choice(rps)
  print("Opponent's choice,", c)
  if rps[0] == c:
    print("You won!")
  else: print("You lost!")

elif user_choice == "B":
  r = rps[0]
  c = choice(rps)
  print("Opponent choice,", c)
  if rps[0] == c:
    print("You won!")
  else: print("You lost!")

elif user_choice == "C":
  r = rps[0]
  c = choice(rps)
  print("Opponent choice,", c)
  if rps[0] == c:
    print("You won!")
  else: print("You lost!")
