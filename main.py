import random

def determine_winner (users_choice,computers_coice) :
    
    if users_choice == computers_coice :
        return 'draw'
    
    if(
        (users_choice == 'rock' and computers_coice == 'scissor') or
        (users_choice == 'paper' and computers_coice == 'rock') or
        (users_choice == 'scissor' and computers_coice == 'paper')
        ) :

        return 'user'
    
    else :
        return "computer"


def play() :

    scores = {'user' : 0, 'computer' : 0, 'draw' : 0}
    choices = ['rock', 'paper', 'scissor']

    print()
    print('           ===============================================')
    print()
    print('                \033[32m🥌 🎮 🕹️  WELCOME TO THE GAME 🥌 🎮 🕹️\033[0m     ')
    print()
    print('           ===============================================     ')
    

    while (True) :
        print()
        print('                         choose your object                     ')

        print()
        print('__________________________________________________________________')
        print('|                                                                 |')
        print('|                                                                 |')
        print('|     --------------      --------------     --------------       |')
        print('|         Rock 🪨            Paper 📃           Scissor ✂️          |')
        print('|     --------------      --------------     --------------       |')
        print('|                                                                 |')
        print('|_________________________________________________________________|')
        print('                       |                   |')
        print('                       |  press Q to exit  |')
        print('                       |___________________|')
        print()
        print()

        users_choice = input("\033[37m\033[1mEnter Your Choice 🌍 :\033[0m ").lower().strip()

        if(users_choice == 'q') :
            break

        if(users_choice not in choices) :
            print()
            print('❌ Invalid choice please try again ⚠️');
            print()
            print('--------------------------------------------------------')
            continue

        computer_choice = random.choice(choices)

        print()
        print('Your choice :',users_choice)
        print()
        print('Computers Choice 🖥️  :',computer_choice)
        print()

        winner = determine_winner(users_choice,computer_choice)

        if(winner == 'draw') :
            print('--------------------------------------------------------')
            print("          📍 It's a Draw! Match again 📍")
            print('--------------------------------------------------------')
            scores['draw'] += 1
            continue

        print('--------------------------------------------------------')
        print('     🥳 🍾 🎆 and the winner is 🥳 🍾 🎆 :',winner)
        print('--------------------------------------------------------')


        scores[winner] += 1
        print()
        print('\033[37m\033[1mSCORES :\033[0m')
        print()
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print()
        print('      USER              COMPUTER              DRAW')
        print()
        print(f'        {scores["user"]}                   {scores["computer"]}                   {scores["draw"]}')
        print()
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print()


play()












