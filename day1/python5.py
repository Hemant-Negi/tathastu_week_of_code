player1=int(input("enter the no. of run scored by player 1 in 60 balls"))
player2=int(input("enter the no. of run scored by player 2 in 60 balls"))
player3=int(input("enter the no. of run scored by player 3 in 60 balls"))
#strike rate
strike_rate1=(player1/60)*100
strike_rate2=(player2/60)*100
strike_rate3=(player3/60)*100
print("strike rate of player 1 : ",strike_rate1)
print("strike rate of player 2 : ",strike_rate2)
print("strike rate of player 3 : ",strike_rate3)
#if 60 more balls
run_player1=player1*2
run_player2=player2*2
run_player3=player3*2
print(run_player1)
print(run_player2)
print(run_player3)
#maximum no of 6's
six_player1=player1//6
six_player2=player2//6
six_player3=player3//6
print("no. of most six by player 1 :",six_player1)
print("no. of most six by player 2 :",six_player2)
print("no. of most six by player 3 :",six_player3)
