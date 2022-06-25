import random

def kalaha_inputs():
    
    gamer_1 = "exit"
    gamer_2 = "exit"
    
    print("Välkommen till Kalaha!\n(skriv exit om du vill lämna spelet)")
    
    while True:
        
        k = input("Hur många kulor i varje skål (3 till 6)? ")
        
        if k == "exit":
            break
        
        elif k != "3" and k != "4" and k != "5" and k != "6":
            print("Var god välj mellan 3, 4, 5 och 6 kulor!")
        
        else: break
    
    if k != "exit":   
        while True:
        
            gamer_1 = input("Är spelare 1 en människa (J/N)?: ")
        
            if gamer_1 == "exit":
                break
            
            elif gamer_1 != "J" and gamer_1 != "N":
                print("Var god svara med J eller N")
            
            else: break
    
    if gamer_1 != "exit":    
        while True:
        
            gamer_2 = input("Är spelare 2 en människa (J/N)?: ")
            
            if gamer_2 == "exit":
                break
        
            elif gamer_2 != "J" and gamer_2 != "N":
                print("Var god svara med J eller N") 
            
            else: break
                
    if gamer_1 != "exit" and gamer_2 != "exit":
        print("\nSpelare 1 är överst med bo till vänster "
              "och spelare 2 är underst med bo till höger.")
        kalaha(int(k), 1, gamer_1, gamer_2)
        
def kalaha_game(winner, bowl_dict):
    
    if winner == 1:
        print("\n", "  ", bowl_dict[5], " ", bowl_dict[4], " ", bowl_dict[3], 
              " ", bowl_dict[2], " ", bowl_dict[1], " ", bowl_dict[0], "\n", 
              bowl_dict[6], "                       ", bowl_dict[13], "\n", 
              "  ", bowl_dict[7], " ", bowl_dict[8], " ", bowl_dict[9], " ", 
              bowl_dict[10], " ", bowl_dict[11], " ", bowl_dict[12], "\n")
              #the board printed in the concole.
        print("Player 1 wins!")
    
    elif winner == 2:
        print("\n", "  ", bowl_dict[5], " ", bowl_dict[4], " ", bowl_dict[3], 
              " ", bowl_dict[2], " ", bowl_dict[1], " ", bowl_dict[0], "\n", 
              bowl_dict[6], "                       ", bowl_dict[13], "\n", 
              "  ", bowl_dict[7], " ", bowl_dict[8], " ", bowl_dict[9], " ", 
              bowl_dict[10], " ", bowl_dict[11], " ", bowl_dict[12], "\n")
              #the board printed in the concole.
        print("Player 2 wins!")
    
    elif winner == 0:
        print("\n", "  ", bowl_dict[5], " ", bowl_dict[4], " ", bowl_dict[3], 
              " ", bowl_dict[2], " ", bowl_dict[1], " ", bowl_dict[0], "\n", 
              bowl_dict[6], "                       ", bowl_dict[13], "\n", 
              "  ", bowl_dict[7], " ", bowl_dict[8], " ", bowl_dict[9], " ", 
              bowl_dict[10], " ", bowl_dict[11], " ", bowl_dict[12], "\n")
              #the board printed in the concole.
        print("Tie!")
        
    
    
def kalaha(k, turn, gamer_1, gamer_2):
    '''
    Parameters
    ----------
    k : integer
        The number of rocks in each bowl.
        
    turn : integer
        Checks which player's turn it is.
        
    gamer_1 : string
        Checks wether or not player is a person.
        
    gamer_2 : string
        Checks wether or not player is a person.
    '''
    
    bowl_dict = {} #the board for the Kalaha game
    
    for bowl in range(14): #the 14 bowls of the Kalaha game
        
        if bowl == 6: #home-bowl of Player 1
            bowl_dict.update({bowl: 0}) #empty in the beginning
        
        elif bowl == 13: #home-bowl of Player 2
            bowl_dict.update({bowl: 0}) #empty in the beginning
        
        else:
            bowl_dict.update({bowl: k}) #other bowls will be filled up
    
    turns(k, turn, gamer_1, gamer_2, bowl_dict) #runs the program turns()
            
            

def turns(k, turn, gamer_1, gamer_2, bowl_dict):
    '''
    Parameters
    ----------
    bowl_dict : dictionary
        A dictionary that represents the board of a Kalaha game.
        
    turn : integer
        Checks which player's turn it is.
        
    gamer_1 : string
        Checks wether or not player is a person.
        
    gamer_2 : string
        Checks wether or not player is a person.
    '''
        
    if turn % 2 == 1: #if turn is uneven, it's player 1 turn
        bowl_choice_player_1(k, turn, gamer_1, gamer_2, bowl_dict)
    
    elif turn % 2 == 0: #if turn is even, it's player 2 turn
        bowl_choice_player_2(k, turn, gamer_1, gamer_2, bowl_dict)
            
        

def bowl_choice_player_1(k, turn, gamer_1, gamer_2, bowl_dict):
    '''
    Parameters
    ----------
    bowl_dict : dictionary
        A dictionary that represents the board of a Kalaha game.
        
    turn : integer
        Checks which player's turn it is.
        
    gamer_1 : string
        Checks wether or not player is a person.
        
    gamer_2 : string
        Checks wether or not player is a person.
    '''

    if gamer_1 == "J": #checks if player is a person
        
        print("\nSpelare 1 tur!")
        
        print("Brädet ser ut sähär:")
    
        print("\n", "  ", bowl_dict[5], " ", bowl_dict[4], " ", bowl_dict[3], 
              " ", bowl_dict[2], " ", bowl_dict[1], " ", bowl_dict[0], "\n", 
              bowl_dict[6], "                       ", bowl_dict[13], "\n", 
              "  ", bowl_dict[7], " ", bowl_dict[8], " ", bowl_dict[9], " ", 
              bowl_dict[10], " ", bowl_dict[11], " ", bowl_dict[12], "\n")
              #the board printed in the concole.
        
        while True: #loop for 
            
            bowl = input("Spelare 1, vilken skål väljer du " 
                         "(1-6, 1 är närmast ditt bo)?: ")

            if bowl == "exit":
                break
            
            else: #translation between user and program.
            
                if bowl == "1": #if user chooses bowl 1.
                    bowl = 5 #translated for the program.
                    if bowl_dict[bowl] == 0: #if bowl is empty
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break #if bowl isn't empty
                    
                elif bowl == "2":
                    bowl = 4
                    if bowl_dict[bowl] == 0:
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break
                    
                elif bowl == "3":
                    bowl = 3
                    if bowl_dict[bowl] == 0:
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break
                    
                elif bowl == "4":
                    bowl = 2
                    if bowl_dict[bowl] == 0:
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break
                    
                elif bowl == "5":
                    bowl = 1
                    if bowl_dict[bowl] == 0:
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break
                    
                elif bowl == "6":
                    bowl = 0
                    if bowl_dict[bowl] == 0:
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break
                    
                else:
                    print("Välj bland skålarna 1, 2, 3, 4, 5 och 6!")
                    
    elif gamer_1 == "N":  
        
        while True:
            
            bowl_list = [5, 4, 3, 2, 1, 0]
            bowl = random.choice(bowl_list)
            
            if bowl_dict[bowl] == 0:
                continue
            
            else: break
        
        print("\nDatorspelare 1 valde att spela skål", bowl_list.index(bowl) + 1)
        
    if bowl != "exit":
        player_1(k, turn, gamer_1, gamer_2, bowl_dict, bowl)



def bowl_choice_player_2(k, turn, gamer_1, gamer_2, bowl_dict):
    '''
    Parameters
    ----------
    bowl_dict : dictionary
        A dictionary that represents the board of a Kalaha game.
        
    turn : integer
        Checks which player's turn it is.
        
    gamer_1 : string
        Checks wether or not player is a person.
        
    gamer_2 : string
        Checks wether or not player is a person.
    '''
    
    if gamer_2 == "J":
        
        print("\nSpelare 2 tur!")
        
        print("Brädet ser ut sähär:")
    
        print("\n", "  ", bowl_dict[5], " ", bowl_dict[4], " ", bowl_dict[3], 
              " ", bowl_dict[2], " ", bowl_dict[1], " ", bowl_dict[0], "\n", 
              bowl_dict[6], "                       ", bowl_dict[13], "\n", 
              "  ", bowl_dict[7], " ", bowl_dict[8], " ", bowl_dict[9], " ", 
              bowl_dict[10], " ", bowl_dict[11], " ", bowl_dict[12], "\n")
              #the board printed in the concole.
        
        while True:
            
            bowl = input("Spelare 2, vilken skål väljer du " 
                         "(1-6, 1 är närmast ditt bo)?: ")

            if bowl == "exit":
                break
            
            else: #translation between user and program.
            
                if bowl == "1": #if user chooses bowl 1.
                    bowl = 12 #translated for the program.
                    if bowl_dict[bowl] == 0: #if bowl is empty
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break #if bowl isn't empty
                    
                elif bowl == "2":
                    bowl = 11
                    if bowl_dict[bowl] == 0:
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break
                    
                elif bowl == "3":
                    bowl = 10
                    if bowl_dict[bowl] == 0:
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break
                    
                elif bowl == "4":
                    bowl = 9
                    if bowl_dict[bowl] == 0:
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break
                    
                elif bowl == "5":
                    bowl = 8
                    if bowl_dict[bowl] == 0:
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break
                    
                elif bowl == "6":
                    bowl = 7
                    if bowl_dict[bowl] == 0:
                        print("Skålen är tom, välj en skål med stenar i!")
                    else: break

                else:
                    print("Välj bland skålarna 1, 2, 3, 4, 5 och 6!")
                    
    elif gamer_2 == "N":  
        
        while True:
            
            bowl_list = [5, 4, 3, 2, 1, 0]
            bowl = random.choice(bowl_list) + 7
            
            if bowl_dict[bowl] == 0:
                continue
            
            else: break
        
        print("\nDatorspelare 2 valde att spela skål", bowl_list.index(bowl - 7) + 1)
        
    if bowl != "exit":
        player_2(k, turn, gamer_1, gamer_2, bowl_dict, bowl)
    
    
        
def player_1(k, turn, gamer_1, gamer_2, bowl_dict, bowl):
    '''
    Parameters
    ----------
    bowl_dict : dictionary
        A dictionary that represents the board of a Kalaha game.
        
    turn : integer
        Checks which player's turn it is.
        
    gamer_1 : string
        Checks wether or not player is a person.
        
    gamer_2 : string
        Checks wether or not player is a person.
    
    bowl : integer
        The bowl thaa has been chosen for this round
    '''
    
    rocks = bowl_dict[bowl]
        
    turns = 1
    bowl_dict.update({bowl: 0})
        
    while rocks > 1:
                
        if bowl + turns == 14:
            turns -= 14
                    
        else:
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1
            turns += 1
                
    while rocks == 1:
                    
        if bowl + turns == 14:
            turns -= 14
                        
        elif bowl + turns == 6:
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1
            turn -= 1
                    
        else:
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1
                                
    turn += 1
    
    winner(k, turn, gamer_1, gamer_2, bowl_dict)
            

                        
def player_2(k, turn, gamer_1, gamer_2, bowl_dict, bowl):
    '''
    Parameters
    ----------
    bowl_dict : dictionary
        A dictionary that represents the board of a Kalaha game.
        
    turn : integer
        Checks which player's turn it is.
        
    gamer_1 : string
        Checks wether or not player is a person.
        
    gamer_2 : string
        Checks wether or not player is a person.
    
    bowl : integer
        The bowl thaa has been chosen for this round
    '''
        
    rocks = bowl_dict[bowl]
    
    turns = 1
    bowl_dict.update({bowl: 0})
        
    while rocks > 1:
                
        if bowl + turns == 14:
            turns -= 14
                    
        else:
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1
            turns += 1
                
    while rocks == 1:
                    
        if bowl + turns == 14:
            turns -= 14
                        
        elif bowl + turns == 13:
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1
            turn -= 1
                    
        else:
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1
        
    turn += 1
    
    winner(k, turn, gamer_1, gamer_2, bowl_dict)
            
    
    
def winner(k, turn, gamer_1, gamer_2, bowl_dict):
    
    if sum([bowl_dict[0], bowl_dict[1], bowl_dict[2], 
            bowl_dict[3], bowl_dict[4], bowl_dict[5]]) == 0:
        #if player 1 bowls are empty
                        
        bowl_dict.update({13: bowl_dict[13]
                             +bowl_dict[7]
                             +bowl_dict[8]
                             +bowl_dict[9]
                             +bowl_dict[10]
                             +bowl_dict[11]
                             +bowl_dict[12]})
        #rocks in player 2's bowls will be put in player 2's home bowl.
                        
        bowl_dict.update({7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}) #empty bowls
        
        if bowl_dict[6] > 6 * k: #if player 1 has most rocks, player 1 win.
            kalaha_game(1, bowl_dict)
        elif bowl_dict[13] > 6 * k: #if player 2 has most rocks, player 2 win.
            kalaha_game(2, bowl_dict)
        else: kalaha_game(0, bowl_dict) #if nobody has most rocks, both have same number. Tie.
                
    elif sum([bowl_dict[7], bowl_dict[8], bowl_dict[9], 
              bowl_dict[10], bowl_dict[11], bowl_dict[12]]) == 0:
        #if player 2 bowls are empty
                        
        bowl_dict.update({6: bowl_dict[6]
                            +bowl_dict[0]
                            +bowl_dict[1]
                            +bowl_dict[2]
                            +bowl_dict[3]
                            +bowl_dict[4]
                            +bowl_dict[5]})
        #rocks in player 1's bowls will be put in player 1's home bowl.
                        
        bowl_dict.update({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}) #empty bowls.
                       
        if bowl_dict[6] > 6 * k: #if player 1 has most rocks, player 1 win.
            kalaha_game(1, bowl_dict)
        elif bowl_dict[13] > 6 * k: #if player 2 has most rocks, player 2 win.
            kalaha_game(2, bowl_dict)
        else: kalaha_game(0, bowl_dict) #if nobody has most rocks, both have same number. Tie.
    
    elif bowl_dict[6] > 6 * k: #if player 1 has enough rocks to win the game.
        kalaha_game(1, bowl_dict)
    
    elif bowl_dict[13] > 6* k: #if player 2 has enough rocks to win the game.
        kalaha_game(2, bowl_dict)
    
    else: #if no player has won yet, loop continues.
        turns(k, turn, gamer_1, gamer_2, bowl_dict)    
#-----------------------------------------------------------------------------
def main():
    
    kalaha_inputs()

if __name__ == '__main__':
    main() 