import random
import matplotlib.pyplot as plt

def kalaha_inputs():
    '''
    Ask for what strategy should be used for each player, how many rocks will
    be in each bowl, and how many games will be simulated. Strategy 1 is for
    using the bowl with most rocks in it while strategy 2 is for any bowl with
    rocks in. Results will be plotted with a bar graph after all requested 
    simulations have been conducted. 
    '''
    gamer_1 = "exit" #default definition
    gamer_2 = "exit" #default definition
    k       = "exit" #default definition
    
    while True: #while loop for handling errors
        
        gamer_1 = input("Välj '1' för att välja skål slumpmässigt, välj '2' "
                        "för att välja skål skålen med mest stenar i. \n \n"
                        "Vilken strategi ska spelare 1 ha? ")
        
        if gamer_1 == "exit": #if exit, leave loop.
            break
            
        elif gamer_1 != "1" and gamer_1 != "2": 
            #if input is not fit as a parameter
            print("Var god svara 1 eller 2")
            
        else: break #if everything was entered correctly
    
    if gamer_1 != "exit": #if first input was exit, the program ends.
        
        while True: #while loop for handling errors
        
            gamer_2 = input("Vilken strategi ska spelare 2 ha? ")
            
            if gamer_2 == "exit":
                break
        
            elif gamer_2 != "1" and gamer_2 != "2":
                #if input is not fit as a parameter
                print("Var god svara 1 eller 2") 
            
            else: break
        
    if gamer_2 != "exit":
        
        while True: #while loop for handling errors
        
            k = input("Hur många kulor i varje skål (3 till 6)? ")
        
            if k == "exit": #if exit, leave loop.
                break
        
            elif k != "3" and k != "4" and k != "5" and k != "6":
                #if input is not fit as a parameter
                print("Var god välj mellan 3, 4, 5 och 6 kulor!")
        
            else: break
    
    if k != "exit":   
        
        while True: #while loop for handling errors
        
            n_games = input("Hur många partier vill du simulera? ")
            
            if n_games == "exit": #if exit, leave loop.
                break
            
            try:
                int(n_games) #checks wether n_games is integer or not.
                break
            
            except:
                print("Var god skriv ett heltal!") #integer is required
    
    if gamer_1 != "exit":
        
        kalaha_simulations(int(gamer_1), int(gamer_2), int(k), int(n_games))



def kalaha_simulations(gamer_1, gamer_2, k, n_games):
    '''
    Parameters
    ----------
    gamer_1 : Integer
        The strategy requested for player 1
        
    gamer_2 : Integer
        The strategy requested for player 2
        
    k : Integer
        The number of rocks in each bowl
        
    n_games : Integer
        The requested number of simulations
    '''   
    gamer_1_win = 0
    gamer_2_win = 0
    tie = 0
        
    n_games_list = [] #for number of games being simulated
    error = [] #for games that haven't been counted
        
    while len(n_games_list) < n_games:
        n_games_list.append(1) #each iterations is one game
        
    for games in n_games_list:
        if kalaha(gamer_1, gamer_2, k, n_games, 1) == 1:
            gamer_1_win += 1 #if player 1 wins
                
        elif kalaha(gamer_1, gamer_2, k, n_games, 1) == 2:
            gamer_2_win += 1 #if player 2 wins
            
        elif kalaha(gamer_1, gamer_2, k, n_games, 1) == 0:
            tie += 1 #when tie
                
        else:
            error.append(kalaha(gamer_1, gamer_2, k, n_games, 1))
            #if game isn't counted by above program
    
    for game in error: #for games that haven't been counted by above program.
        
        if game == 1:
            gamer_1_win += 1 #if player 1 wins
        elif game == 2:
            gamer_2_win += 1 #if player 2 wins
        elif game == 0:
            tie += 1 #when tie

    print("Spelare 1 vann", gamer_1_win, "av", n_games, "spel!")
    print("Spelare 2 vann", gamer_2_win, "av", n_games, "spel!")
    print(tie, "av", n_games, "spel blev oavgjorda!")
    
    plt.clf() #delete old graph from previous simulation
    
    plt.bar(1, gamer_1_win) #player 1 bar
    plt.savefig('Kalaha_Simulations.pdf')
    plt.bar(2, gamer_2_win) #player 2 bar
    plt.savefig('Kalaha_Simulations.pdf')
    plt.bar(3, tie) #tie
    plt.savefig('Kalaha_Simulations.pdf')
    
    

def kalaha(gamer_1, gamer_2, k, n_games, turn):
    '''
    Parameters
    ----------
    gamer_1 : Integer
        An indicator for the strategy requested for player 1
        
    gamer_2 : Integer
        An indicator for the strategy requested for player 2
        
    k : Integer
        The number of rocks in each bowl
        
    n_games : Integer
        The requested number of simulations

    Returns
    -------
    Integer
        An indicator for the winner of the game.
    '''
    
    bowl_dict = {} #creation of the board.
    
    for bowl in range(14): #each key is one bowl
        
        if bowl == 6:
            bowl_dict.update({bowl: 0}) #player 1 bowl is empty
        
        elif bowl == 13:
            bowl_dict.update({bowl: 0}) #player 2 bowl is empty
        
        else:
            bowl_dict.update({bowl: k}) #every other bowl with requested k rocks.
    
    return turns(gamer_1, gamer_2, k, n_games, turn, bowl_dict)
            
            

def turns(gamer_1, gamer_2, k, n_games, turn, bowl_dict):
    '''
    Parameters
    ----------
    gamer_1 : Integer
        An indicator for the strategy requested for player 1
        
    gamer_2 : Integer
        An indicator for the strategy requested for player 2
        
    k : Integer
        The number of rocks in each bowl
        
    n_games : Integer
        The requested number of simulations
        
    bowl_dict : Dictionary
        A dictionary that simulates the board for the kalaha game.

    Returns
    -------
    Integer
        An indicator for the winner of the game.
    '''
        
    if turn % 2 == 1: #if "turn" is uneven, it's player 1 turn
        return bowl_choice_player_1(gamer_1, gamer_2, k, n_games, turn, bowl_dict)
    
    elif turn % 2 == 0: #if "turn" is even, it's player 2 turn
        return bowl_choice_player_2(gamer_1, gamer_2, k, n_games, turn, bowl_dict)
            
        

def bowl_choice_player_1(gamer_1, gamer_2, k, n_games, turn, bowl_dict):
    '''
    Parameters
    ----------
    gamer_1 : Integer
        An indicator for the strategy requested for player 1
        
    gamer_2 : Integer
        An indicator for the strategy requested for player 2
        
    k : Integer
        The number of rocks in each bowl
        
    n_games : Integer
        The requested number of simulations
        
    bowl_dict : Dictionary
        A dictionary that simulates the board for the kalaha game.

    Returns
    -------
    Integer
        An indicator for the winner of the game.
    '''
    
    if gamer_1 == 1: #if strategy 1 was requested
        
        bowl_list = [0, 1, 2, 3, 4, 5] #0 is bowl 6, 5 is bowl 1.
        bowl_rocks = [] #list of rocks in ech bowl
        
        for bowl in bowl_list:
            bowl_rocks.append(bowl_dict[bowl]) #number of rocks added to list.
        
        while True:
            
            bowl = random.choice(bowl_list) #chooses a random bowl
            
            if bowl_dict[bowl] < max(bowl_rocks):
                continue #if bowl has less rocks than bowl with most rocks,
                         #another bowl will be chosen.
            
            else: break #when adequate bowl has been found.
        
    elif gamer_1 == 2: #if strategy 2 has been requested
        
        while True:
            
            bowl_list = [0, 1, 2, 3, 4, 5] #0 is bowl 6, 5 is bowl 1.
            bowl = random.choice(bowl_list) #choses a random bowl
            
            if bowl_dict[bowl] == 0: #if bowl doesn't have rocks in them,
                continue             #another bowl will be chosen 
            
            else: break #when bowl with rocks in them has ben found.
        
    if bowl != "exit":
        return player_1(gamer_1, gamer_2, k, n_games, turn, bowl_dict, bowl)



def bowl_choice_player_2(gamer_1, gamer_2, k, n_games, turn, bowl_dict): 
    '''
    Parameters
    ----------
    gamer_1 : Integer
        An indicator for the strategy requested for player 1
        
    gamer_2 : Integer
        An indicator for the strategy requested for player 2
        
    k : Integer
        The number of rocks in each bowl
        
    n_games : Integer
        The requested number of simulations
        
    bowl_dict : Dictionary
        A dictionary that simulates the board for the kalaha game.

    Returns
    -------
    Integer
        An indicator for the winner of the game.
    '''
    
    if gamer_2 == 1:
        
        bowl_list = [7, 8, 9, 10, 11, 12] #7 is bowl 6, 12 is bowl 1.
        bowl_rocks = [] #list of rocks in ech bowl
        
        for bowl in bowl_list:
            bowl_rocks.append(bowl_dict[bowl]) #number of rocks added to list
        
        while True:
            
            bowl = random.choice(bowl_list) #chooses a random bowl
            
            if bowl_dict[bowl] < max(bowl_rocks):
                continue #if bowl has less rocks than bowl with most rocks,
                         #another bowl will be chosen.
            
            else: break        
        
    elif gamer_2 == 2:
        
        while True:
            
            bowl_list = [7, 8, 9, 10, 11, 12]
            bowl = random.choice(bowl_list) #chooses a random bowl
            
            if bowl_dict[bowl] == 0: #if bowl doesn't have rocks in them,
                continue             #another bowl will be chosen 
            
            else: break #when bowl with rocks in them has ben found.
        
    if bowl != "exit":
        return player_2(gamer_1, gamer_2, k, n_games, turn, bowl_dict, bowl)
    
    
        
def player_1(gamer_1, gamer_2, k, n_games, turn, bowl_dict, bowl):
    '''
    Parameters
    ----------
    gamer_1 : Integer
        An indicator for the strategy requested for player 1
        
    gamer_2 : Integer
        An indicator for the strategy requested for player 2
        
    k : Integer
        The number of rocks in each bowl
        
    n_games : Integer
        The requested number of simulations
        
    bowl_dict : Dictionary
        A dictionary that simulates the board for the kalaha game.
    
    bowl : Integer
        An indicator for the bowl chosen

    Returns
    -------
    Integer
        An indicator for the winner of the game.
    '''
    
    rocks = bowl_dict[bowl] #the number rocks of the bowl will be stored here.
    bowl_dict.update({bowl: 0}) #the rocks are taken out if the bowl.   
    turns = 1 #for each clockwise following bowl
       
    while rocks > 1: #the main procedure in the game, putting one rock in bowl
                
        if bowl + turns == 14:
            turns -= 14 #goes to bowl 6 of player 1.
                    
        else:
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1 #rock that has been put in bowl.
            turns += 1 #next bowl
                
    while rocks == 1: #last rock holds special rules, is dealt with here.
                    
        if bowl + turns == 14:
            turns -= 14 #goes to bowl 6 of player 1.
                        
        elif bowl + turns == 6: #if in player 1's bowl.
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1 #rocks is now 0, loop ends.
            turn -= 1 #when turn gets +1 later, it is players turn again.
                    
        else: #if last bowl is not player 1's home bowl.
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1 
                                
    turn += 1 #next player's turn.
    
    return winner(gamer_1, gamer_2, k, n_games, turn, bowl_dict)
            

                        
def player_2(gamer_1, gamer_2, k, n_games, turn, bowl_dict, bowl):
    '''
    Parameters
    ----------
    gamer_1 : Integer
        An indicator for the strategy requested for player 1
        
    gamer_2 : Integer
        An indicator for the strategy requested for player 2
        
    k : Integer
        The number of rocks in each bowl
        
    n_games : Integer
        The requested number of simulations
        
    bowl_dict : Dictionary
        A dictionary that simulates the board for the kalaha game.
        
    bowl : Integer
        An indicator for the bowl chosen

    Returns
    -------
    Integer
        An indicator for the winner of the game.
    '''
        
    rocks = bowl_dict[bowl] #the number rocks of the bowl will be stored here.
    bowl_dict.update({bowl: 0}) #the rocks are taken out if the bowl.   
    turns = 1 #for each clockwise following bowl
        
    while rocks > 1: #the main procedure in the game, putting one rock in bowl
                
        if bowl + turns == 14:
            turns -= 14 #goes to bowl 6 of player 1.
                    
        else:
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1 #rock that has been put in bowl.
            turns += 1 #next bowl
                
    while rocks == 1: #last rock holds special rules, is dealt with here.
                    
        if bowl + turns == 14:
            turns -= 14 #goes to bowl 6 of player 1.
                        
        elif bowl + turns == 13: #if in player 2's bowl.
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1 #rocks is now 0, loop ends.
            turn -= 1 #when turn gets +1 later, it is players turn again.
                    
        else: #if last bowl is not player 2's home bowl.
            bowl_dict.update({bowl + turns: bowl_dict[bowl + turns] + 1})
            rocks -= 1 
                                
    turn += 1 #next player's turn.
    
    return winner(gamer_1, gamer_2, k, n_games, turn, bowl_dict)
            
    
    
def winner(gamer_1, gamer_2, k, n_games, turn, bowl_dict):
    '''
    Parameters
    ----------
    gamer_1 : Integer
        An indicator for the strategy requested for player 1
        
    gamer_2 : Integer
        An indicator for the strategy requested for player 2
        
    k : Integer
        The number of rocks in each bowl
        
    n_games : Integer
        The requested number of simulations
        
    bowl_dict : Dictionary
        A dictionary that simulates the board for the kalaha game.

    Returns
    -------
    Integer
        An indicator for the winner of the game.
    '''
    
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
            return 1
        elif bowl_dict[13] > 6 * k: #if player 2 has most rocks, player 2 win.
            return 2
        else: return 0 #if nobody has most rocks, both have same number. Tie.
                
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
            return 1
        elif bowl_dict[13] > 6 * k: #if player 2 has most rocks, player 2 win.
            return 2
        else: return 0 #if nobody has most rocks, both have same number. Tie.
    
    elif bowl_dict[6] > 6 * k: #if player 1 has enough rocks to win the game.
        return 1
    
    elif bowl_dict[13] > 6* k: #if player 2 has enough rocks to win the game.
        return 2
    
    else: #if no player has won yet, loop continues.
        return turns(gamer_1, gamer_2, k, n_games, turn, bowl_dict)
       
#-----------------------------------------------------------------------------

def main():
    
    kalaha_inputs() #starts asking for inputs to start simulations.

if __name__ == '__main__': #axiomatic in python.
    main()