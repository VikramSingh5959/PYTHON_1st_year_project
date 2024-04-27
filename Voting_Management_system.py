election_status=1
votes_BJP=0
votes_CONGRESS=0
votes_AAP=0
votes_OTHERS=0
while(election_status==1):
      name=(input("enter candidate name : "))
      age=int(input("enter candidate age : "))
      choice1=int(input(" to vote 'BJP' press 1 : \n to vote 'Congress' press 2 : \n to vote 'AAP' press 3 : \n to vote 'Others' press 4 : \n"))
      choice2=int(input("to 'continue' press 1 \nto 'exit' press 2 \n"))
      if(age>=18):
            if(choice1==1):
                  print("You have successfully voted BJP\n 'THANKS FOR VOTING':) ")
                  votes_BJP+=1
            elif(choice1==2):
                  print("You have successfully voted Congress\n 'THANKS FOR VOTING':) ")
                  votes_CONGRESS+=1
            elif(choice1==3):
                  print("You have successfully voted AAP\n 'THANKS FOR VOTING':) ")
                  votes_AAP+=1
            elif(choice1==4):
                  print("You have successfully voted Others\n 'THANKS FOR VOTING':) ")
                  votes_OTHERS+=1
            elif(choice1 !=(1 or 2 or 3 or 4)):
                  print("enter valid choice for voting the party")
                  print("2 attempts left")
                  choice1=int(input("to vote 'BJP' press 1 : \n to vote 'Congress' press 2 : \n to vote 'AAP' press 3 : \n to vote 'Others' press 4 : \n"))
                  if(choice1==1):
                        print("You have successfully voted BJP\n 'THANKS FOR VOTING':) ")
                        votes_BJP+=1
                  elif(choice1==2):
                        print("You have successfully voted Congress\n 'THANKS FOR VOTING':) ")
                        votes_CONGRESS+=1
                  elif(choice1==3):
                        print("You have successfully voted AAP\n 'THANKS FOR VOTING':) ")
                        votes_AAP+=1
                  elif(choice1==4):
                        print("You have successfully voted Others\n 'THANKS FOR VOTING':) ")
                        votes_OTHERS+=1
                  elif(choice1 !=(1 or 2 or 3 or 4)):
                        print("enter valid choice for voting the party")
                        print("1 attempts left")
                        choice1=int(input("to vote 'BJP' press 1 : \n to vote 'Congress' press 2 : \n to vote 'AAP' press 3 : \n to vote 'Others' press 4 : \n"))
                        if(choice1==1):
                              print("You have successfully voted BJP\n 'THANKS FOR VOTING':) ")
                              votes_BJP+=1
                        elif(choice1==2):
                              print("You have successfully voted Congress\n 'THANKS FOR VOTING':) ")
                              votes_CONGRESS+=1
                        elif(choice1==3):
                              print("You have successfully voted AAP\n 'THANKS FOR VOTING':) ")
                              votes_AAP+=1
                        elif(choice1==4):
                              print("You have successfully voted Others\n 'THANKS FOR VOTING':) ")
                              votes_OTHERS+=1
            if(choice2==2):
                  if(votes_BJP>votes_CONGRESS and votes_BJP>votes_AAP and votes_BJP>votes_CONGRESS and votes_BJP>votes_OTHERS):
                        print("BJP IS THE WINNER")
                  elif(votes_CONGRESS>votes_BJP and votes_CONGRESS>votes_AAP and votes_CONGRESS>votes_OTHERS):
                        print("CONGRESS IS THE WINNER")
                  elif(votes_AAP>votes_BJP and votes_AAP>votes_CONGRESS and votes_AAP>votes_OTHERS):
                        print("AAP IS THE WINNER ")
                  elif(votes_OTHERS>votes_BJP and votes_OTHERS>votes_CONGRESS and votes_OTHERS>votes_AAP):
                        print("OTHERS IS A WINNER ")
                  elif(votes_BJP==votes_CONGRESS==votes_AAP==votes_OTHERS):
                        print("All election parties got equal votes so elections is tied.")
                  elif(votes_BJP==votes_CONGRESS==votes_AAP):
                        print("The election is tied between BJP,CONGRESS and AAP and OTHERS has lost the match ")
                  elif(votes_BJP==votes_CONGRESS==votes_OTHERS):
                        print("The election is tied between BJP,CONGRESS and OTHERS and AAP has lost the match ")
                  elif(votes_OTHERS==votes_CONGRESS==votes_AAP):
                        print("The election is tied between OTHERS,CONGRESS and AAP and BJP has lost the match ")
                  elif(votes_BJP==votes_CONGRESS):
                        if(votes_BJP!=0 and votes_CONGRESS!=0):
                              print("The elections has been tied between BJP and CONGRESS ")
                        elif(votes_AAP==votes_OTHERS):
                              print("The elections has been tied between AAP and OTHERS ")
                  elif(votes_BJP==votes_AAP):
                        if(votes_BJP!=0 and votes_AAP!=0):
                              print("The elections has been tied between BJP and AAP ")
                        elif(votes_CONGRESS==votes_OTHERS):
                              print("The elections has been tied between CONGRESS and OTHERS ")
                  elif(votes_BJP==votes_OTHERS):
                        if(votes_BJP!=0 and votes_OTHERS!=0):
                              print("The elections has been tied between BJP and OTHERS ")
                        elif(votes_CONGRESS==votes_AAP):
                              print("The elections has been tied between CONGRESS and AAP ")
                  elif(votes_CONGRESS==votes_AAP):
                        print("The elections has been tied between CONGRESS and AAP ")
                  elif(votes_CONGRESS==votes_OTHERS):
                        print("The elections has been tied between CONGRESS and OTHERS ")
                  elif(votes_AAP==votes_OTHERS):
                        print("The elections has been tied between AAP and OTHERS ")
                  n=2
            elif(choice2==1):
                  n=1
            else:
                  print("enter valid choice to continue or exit")
                  print("2 attempt left")
                  choice2=int(input("to 'continue' press 1 \nto 'exit' press 2 \n"))
                  if(choice2==2):
                        if(votes_BJP>votes_CONGRESS and votes_BJP>votes_AAP and votes_BJP>votes_CONGRESS and votes_BJP>votes_OTHERS):
                              print("BJP IS THE WINNER")
                        elif(votes_CONGRESS>votes_BJP and votes_CONGRESS>votes_AAP and votes_CONGRESS>votes_OTHERS):
                              print("CONGRESS IS THE WINNER")
                        elif(votes_AAP>votes_BJP and votes_AAP>votes_CONGRESS and votes_AAP>votes_OTHERS):
                              print("AAP IS THE WINNER ")
                        elif(votes_OTHERS>votes_BJP and votes_OTHERS>votes_CONGRESS and votes_OTHERS>votes_AAP):
                              print("OTHERS IS A WINNER ")
                        elif(votes_BJP==votes_CONGRESS==votes_AAP==votes_OTHERS):
                              print("All election parties got equal votes so elections is tied.")
                        elif(votes_BJP==votes_CONGRESS==votes_AAP):
                              print("The election is tied between BJP,CONGRESS and AAP and OTHERS has lost the match ")
                        elif(votes_BJP==votes_CONGRESS):
                              if(votes_BJP!=0 and votes_CONGRESS!=0):
                                    print("The elections has been tied between BJP and CONGRESS ")
                              elif(votes_AAP==votes_OTHERS):
                                    print("The elections has been tied between AAP and OTHERS ")
                        elif(votes_BJP==votes_AAP):
                              if(votes_BJP!=0 and votes_AAP!=0):
                                    print("The elections has been tied between BJP and AAP ")
                        elif(votes_CONGRESS==votes_OTHERS):
                              print("The elections has been tied between CONGRESS and OTHERS ")
                        elif(votes_BJP==votes_OTHERS):
                              if(votes_BJP!=0 and votes_OTHERS!=0):
                                    print("The elections has been tied between BJP and OTHERS ")
                              elif(votes_CONGRESS==votes_AAP):
                                    print("The elections has been tied between CONGRESS and AAP ")
                        elif(votes_CONGRESS==votes_AAP):
                              print("The elections has been tied between CONGRESS and AAP ")
                        elif(votes_CONGRESS==votes_OTHERS):
                              print("The elections has been tied between CONGRESS and OTHERS ")
                        elif(votes_AAP==votes_OTHERS):
                              print("The elections has been tied between AAP and OTHERS ")
                        n=2
                        break
                  elif(choice2==1):
                        n=1
                        
                  else:
                        print("enter valid choice to continue or exit")
                        print("1 attempt left")
                        choice2=int(input("to 'continue' press 1 \nto 'exit' press 2 \n"))
                        if(choice2==2):
                              if(votes_BJP>votes_CONGRESS and votes_BJP>votes_AAP and votes_BJP>votes_CONGRESS and votes_BJP>votes_OTHERS):
                                    print("BJP IS THE WINNER")
                              elif(votes_CONGRESS>votes_BJP and votes_CONGRESS>votes_AAP and votes_CONGRESS>votes_OTHERS):
                                    print("CONGRESS IS THE WINNER")
                              elif(votes_AAP>votes_BJP and votes_AAP>votes_CONGRESS and votes_AAP>votes_OTHERS):
                                    print("AAP IS THE WINNER ")
                              elif(votes_OTHERS>votes_BJP and votes_OTHERS>votes_CONGRESS and votes_OTHERS>votes_AAP):
                                    print("OTHERS IS A WINNER ")
                              elif(votes_BJP==votes_CONGRESS==votes_AAP==votes_OTHERS):
                                    print("All election parties got equal votes so elections is tied.")
                              elif(votes_BJP==votes_CONGRESS==votes_AAP):
                                    print("The election is tied between BJP,CONGRESS and AAP and OTHERS has lost the election ")
                              elif(votes_BJP==votes_CONGRESS):
                                    if(votes_BJP!=0 and votes_CONGRESS!=0):
                                          print("The elections has been tied between BJP and CONGRESS ")
                                    elif(votes_AAP==votes_OTHERS):
                                          print("The elections has been tied between AAP and OTHERS ")
                              elif(votes_BJP==votes_AAP):
                                    if(votes_BJP!=0 and votes_AAP!=0):
                                          print("The elections has been tied between BJP and AAP ")
                              elif(votes_CONGRESS==votes_OTHERS):
                                    print("The elections has been tied between CONGRESS and OTHERS ")
                              elif(votes_BJP==votes_OTHERS):
                                    if(votes_BJP!=0 and votes_OTHERS!=0):
                                          print("The elections has been tied between BJP and OTHERS ")
                              elif(votes_CONGRESS==votes_AAP):
                                    print("The elections has been tied between CONGRESS and AAP ")
                              elif(votes_CONGRESS==votes_AAP):
                                    print("The elections has been tied between CONGRESS and AAP ")
                              elif(votes_CONGRESS==votes_OTHERS):
                                    print("The elections has been tied between CONGRESS and OTHERS ")
                              elif(votes_AAP==votes_OTHERS):
                                    print("The elections has been tied between AAP and OTHERS ")
                              n=2
                              break
                        elif(choice2==1):
                              n=1     
      else:
            print("Age can't be smaller than 18 please enter valid age")


