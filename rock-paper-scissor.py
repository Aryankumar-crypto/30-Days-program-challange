import random
l=["rock","paper","scissor"]
'''
rock vs paper = paper wins
paper vs scissor = scissor wins
rock vs scissor = rock wins

'''
while True:
    ucount=0
    ccount=0
    uc=int(input('''
Game start......
1 Yes
2 No | Exit
         '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock
2 Scissor
3 Paper                                                                
                '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(l) 
            if Cchoice==uchoice:
                print("Computer value",Cchoice)
                print("user value",uchoice)
                print("Game draw") 
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer value",Cchoice)
                print("user value",uchoice)
                print("you win") 
                ucount=ucount+1  
            else:
                print("Computer value",Cchoice)
                print("user value",uchoice)
                print("computer win")
                ccount=ccount+1
            if ccount==ucount:
                print("final game......")
                print("user score ", ucount)
                print("computer score",ccount)
            elif ucount>ccount:
                print("final you win......")
                print("user score ", ucount)
                print("computer score",ccount)  
            else: 
                print("final computer win the game......")
                print("user score ", ucount)
                print("computer score",ccount)     

    else:  
        break                    