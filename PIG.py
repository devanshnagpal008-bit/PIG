#number of players
#define roll function
#ask roll or pass
#store score of each player
#make a loop fo rall players


import random
import sys

numbers=[0,1,2,3,4,5,6,7,8,9]
players=int(input("enter the number of players(2-5): "))
if players>5 or players<2:
    print("enter valid number of players!!!")
    sys.exit()



def roll():
    num =random.choice(numbers)
    print("you got ",num)
    return num


def play():
    ask=input("do you want to play??(y/n) : ").lower()
    if ask=='y':
        return True
    else:
        sys.exit()

def winner():
    top_score=max(player_score)
    winner=[i+1 for i in range(int(players)) if player_score[i]==top_score]
    print("\n\nThe winner is player ",winner," with score of ",top_score)

play()

max_score=50
player_score=[0 for _ in range(int(players))]
if player_score>=max_score:
    winner()
    sys.exit()


while max_score>max(player_score):
    for player_idx in range(int(players)):
        print("\n The for player ",player_idx+1," has started.\n")
        
        while True:
            a=input("do you want to roll / pass / quit ").lower().strip()
            if a=='roll':
                value=roll()
                value=int(value)
                if value==1:
                    player_score[player_idx]=0
                    print("You rolled 1 . turn over!!!")
                    print("total score = ",player_score[player_idx])
                    break
                else:
                    player_score[player_idx]+=value
                    print('total score = ',player_score[player_idx])
                    continue
            elif a=='pass':
                break
            elif a=='quit':
                for player_idx in range(int(players)):
                    print("\n the score for player ",player_idx+1,"is :",player_score[player_idx])
                winner()
                sys.exit()
                
            else:
                sys.exit()
        


        


