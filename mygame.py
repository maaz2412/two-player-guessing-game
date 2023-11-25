#game to guess number
import os
names_list = []
updated_list = []
counter_new = 2
class game_information:
    def __init__(self):
        self.secret_num = None
    def verifyuser_choice(self, x):
        if x == 2:
            print(x, "Number of players are playing the game. ")
            for i in range(2):
                z = input(f"Enter the nickname for {x} players. ")
                names_list.append(z)
                if i == 0:
                    nickname_1 = names_list[i]
                elif i == 1:
                    nickname_2 = names_list[i]
            print(f"Welcome! {nickname_1}(is player#1 ), and {nickname_2}(is player#2 )") 
        else:
            print("Incorrect number of players. ")          
    def game_mechanism(self, player_choice):
        g = 2
        if(player_choice==1):
            print(f"player#{player_choice} has entered the secret number which player#2 will guess. ")
            while g > 0:
                print(f"You have {g} no of tries to make the right guess else you loose. ")
                guess_number = int(input("Make a guess of the the number Range[0-10] "))
                if guess_number == self.secret_num:
                    print("You guessed right! ")
                    break
                else:
                    print("You Failed to guess. ")
                    continue
        elif(player_choice == 2):
            print(f"Player#{player_choice} has entered the secret number that the player#1 will guess. ")
            while g > 0:
                print(f"You have {g} no of tries to make the right guess else you loose. ")
                guess_number = int(input("Make a guess of the number Range[0-10] "))
                
                if guess_number == self.secret_num:
                    print("You Guessed right! ")
                    break
                else:
                    print("You failed to guess! ")
                    continue
    def secret_number (self, player):
        if player == 1:
               print(f"{player} please enter the secret number. ")
               self.secret_num = int(input("Enter the secret number. Range[0-10] "))
               if 0<= self.secret_num <=10:
                   if 0<= self.secret_num <=10:
                       os.system('cls'if os.name=='nt' else'cls')             
        elif player == 2:
               print(f"{player} please enter the secret number. Range[1-10] ")
               self.secret_num = int(input("Enter the secret number. Range[1-10] "))
               if 0<= self.secret_num <=10:
                   os.system('cls'if os.name=='nt' else'cls')
        else:
            print("Error!. ")
myobj = game_information()
no_players = int(input("Enter the number of players that are playing the game (players should be 2!.)"))
myobj.verifyuser_choice(no_players)
player_choice_ = int(input("Who wants to enter the secret number? For player#1 to enter press 1 and for player#2 press 2."))
myobj.secret_number(player=player_choice_)
player_to_guess = player_choice_
myobj.game_mechanism(player_to_guess)











    





        