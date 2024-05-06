import random
rock = """
   _______
  /       \\
 /  _____  \\
/  /     \\  \\
\\  \\     /  /
 \\  \\___/  /
  \\_______/
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""





image=[rock,paper,scissor]
user_choice=int(input("ENTER YOUR CHOICE.\n FOR rock = 0, paper = 1,scissor = 2\n"))
if(user_choice >= 0 and user_choice<= 2):
    print("Enter your choice")
    print(image[user_choice])
else:
    print(f"Invalid choice")
computer_choice=random.randint(0,2)
print(f"Enter computer_choice :- {image[computer_choice]}")

if(computer_choice==0 or user_choice==1):
    print(f"User wins {image[user_choice]} ")
elif(computer_choice==0 and user_choice==2):
    print("Computer wins")
elif(computer_choice==1 and user_choice== 2):
    print("User wins")
elif(computer_choice==1 and user_choice==0):
    print("Computer wins")
elif(computer_choice==2 and user_choice==0):
    print("User wins")
elif(computer_choice==2 and user_choice==1):
    print("Computer wins")
else:
    print("Draw")

