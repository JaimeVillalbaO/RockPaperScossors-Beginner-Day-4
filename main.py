rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
import sys
import os

game_over = False
while not game_over :
    choice = int(input('What do you choose? Type 0  for rock, 1 for paper or 2 for scissors. '))
    computer_choice = random.randint(0,2)
    print('\nYour choise is: ') 
    if choice == 0:
        print(rock)
    elif choice ==1 :
        print(paper)
    elif choice == 2:
        print(scissors)
    else :
        print('You type an invalid number, you lose.')
        sys.exit()

    print('Computer choise is: ')
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else :
        print(scissors)

    if choice ==  computer_choice :
        print('it\'s a draw. ')
    elif choice == 0 and computer_choice == 2 or choice == 1 and computer_choice == 0 or choice == 2 and computer_choice == 1:
        print('You win !!!')
    else:
        print('You lose :(')

    play_again =input('Do you want to play again ? type yes or no: ')
    os.system('cls') 
    
    if play_again == 'no' :
        game_over = True

        
    