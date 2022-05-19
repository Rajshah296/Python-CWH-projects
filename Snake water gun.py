import random
from pip import __main__

player_history,comp_history = [],[] 
result = ['S','W','G']
i,comp_score,player_score = 0,0,0
def update_score(player_choice,comp_choice) :  
    global comp_score,player_score,i
    if(player_choice == comp_choice) : 
        print("Noone won this round.")
    elif(player_choice == 'S' and comp_choice == 'W') : 
        player_score += 1
        print("\nPlayer won this round.\nComp score : ",comp_score,"\nPlayer score : ",player_score)
    elif(player_choice == 'S' and comp_choice == 'G') :
        comp_score += 1
        print("\nComputer won this round.\nComp score : ",comp_score,"\nPlayer score : ",player_score)
    elif(player_choice == 'G' and comp_choice == 'S') :
        player_score += 1   
        print("\nPlayer won this round.\nComp score : ",comp_score,"\nPlayer score : ",player_score)
    elif(player_choice == 'G' and comp_choice == 'W') :
        comp_score  += 1 
        print("\nComputer won this round.\nComp score : ",comp_score,"\nPlayer score : ",player_score)
    elif(player_choice == 'W' and comp_choice == 'G') :
        player_score += 1
        print("\nPlayer won this round.\nComp score : ",comp_score,"\nPlayer score : ",player_score)
    elif(player_choice == 'W' and comp_choice == 'S') :
        comp_score += 1
        print("\nComputer won this round.\nComp score : ",comp_score,"\nPlayer score : ",player_score)  
    i+=1
def main() :
    name = input("Enter your name : ")
    while(1) : 
        while i in range(10) :
            print(f"\nRound {i + 1}\n")
            comp_choice = random.choice(result) 
            player_choice = input("\nEnter your choice : ").capitalize()
            if (player_choice not in result) : print("Invalid input.Pleasetry again.")

            else : 
                update_score(player_choice,comp_choice)
                player_history.append(player_choice),comp_history.append(comp_choice)
        print("Noone wins.") if player_score == comp_score else print(f"{name} wins.\n{name} won for {player_score} rounds.") if player_score > comp_score else print(f"\nComputer wins.\nComputer won for {comp_score} rounds.") 
        print(f"\nGame summary : \n\n{name}'s Summary : \n\n{name}'s choices are: {player_history}\nComputer Summary : \n\nComputer's choices are : {comp_history}")
        resume = input("\nPress any key for continuing to play\nEnter -1 to close the game.")
        if(resume == "-1") : 
            print("\nThanks for Playing")
            break
if __name__ == "__main__" :      
    main()