#Skapat av Lamin Barrow
# Datum: 12/9-2021
player1=input('What is the name of contestant number one?: ')
player2=input('What is the name of contestant number two?: ')
results_p1=[]
results_p2=[]
total_p1=0
total_p2=0

for i in range(5):
    score1=input('How many points did '+player1.capitalize()+" score in round number "+str(i+1)+'?:')
    results_p1.append(score1)
    total_p1+=int(score1)

for i in range(5):
    score2=input('How many points did '+player2.capitalize()+" score in round number "+str(i+1)+'?:')
    results_p2.append(score2)
    total_p2+=int(score2)

#if total_p1==total_p2:
#        print("There was no winner since "+ player1+' and '+ player2+' scored the exact same points which results in a draw')
#if total_p1<total_p2:
#    print(" The winner of the darts game is "+ player2+ ', Congratulations!')
#if total_p1>total_p2:
#    print(" The winner of the darts game is "+ player1+ ', Congratulations!')

