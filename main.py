# This program is by Yoyo Liu 
# Completed 10/5/2021 
# Uploaded to Github 1/21/2024

theBoard = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']#make the board
win = False#make win false - later used for while loop
oneMore = True#for while loop

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def check_winner(check_element):
  global win #import global variable win for while loop
  list_player = []
  for i in range(len(theBoard)):
  #a loop to add element to list
    if theBoard[i] == check_element:
        list_player.append(i)
  #below is a nested loop to add position of Xs and Os to determine the winner
  for i in range(len(list_player)):
    for j in range(len(list_player)):
      if j == i:
        continue        
      for k in range(len(list_player)):
        if k == j or k == i:
          continue
        playerSum = list_player[i] + list_player[j] + list_player[k] #find the sum of the location
        #the if + elif statements below are to find whether the play wins or not
        if list_player[i] == 1 and list_player[j] == 4 and list_player[k] ==7:
          side_grid = True
        elif list_player[i] == 3 and list_player[j] == 6 and list_player[k] == 9:
          side_grid = True
        elif list_player[i] == 4 and list_player[j] == 5 and list_player[k] == 6:
          side_grid = True
        elif playerSum == 15 and list_player[j] - list_player[k] == list_player[k]-list_player[i]:
          side_grid = True
        else:
          side_grid = False
        if playerSum == 6 or playerSum == 24 or side_grid == True:
          win = True
        #if player wins, stop the while loop of getting inputs
  return win

def getInput(player):
  global win #get the global variable win
  confirm = 'n' #initialize variable
  win_here = False
  while confirm == 'n': #while the player doesn't confirm the input, run this over and over again
    try: #try excpet to avoid error and make iteration easier
      selection = input("Player " + str(player) + " please select a grid.")
      confirm = input("Your selection is " + selection + " . [y/n]")
      if confirm == 'y': 
        m = theBoard.index(selection)#ask for selection
      if theBoard[m] == 'O' or theBoard[m] == 'X':
        a = 1/0
        print(a) #create error to ask the user to enter again if the place is already taken
      if player == 1:
        theBoard[m] = 'O'
        total_taken = theBoard.count('O')
      if player == 2:
        theBoard[m] = 'X'
        total_taken = theBoard.count('X')#change the board and count the amount of Xs and Os
      if total_taken >=3: #if there's a possibility of someone's winning, check for the winner
        win_here = check_winner(theBoard[m])
      if win_here == True:#if someone won, then end game,  and display congrats message
        if player == 1:
          print("Congratulation! Player 1 Wins!\nThis is the final board: ")
          win = True
        elif player ==2:
          print("Congratulation! Player 2 Wins!\nThis is the final board: ")
          win = True
      if theBoard.count('X') + theBoard.count('O') == 9 and win_here == False:#if all the blocks are taken and there is no winner, display no winner message
        print("Oops, I guess this is a tie huh?")
        win = True
    except UnboundLocalError:
      confirm = 'n'
    except:
      print("Sorry, that selection is not valid. Please re-enter.")
      confirm = 'n'
      m = 0 #if there's an error, delete exsiting m value
  drawBoard(theBoard)
  return win
    
while oneMore:
  print("Welcome to 2-Player Tic Tac Toe. \nPlayer 1: O; Player 2: X")
  drawBoard(theBoard)#display board
  while win == False: #while noone win, run this again and again
    win = getInput(1)
    if win == False: #if player 1 didn't win, ask for player2's input
      win = getInput(2)
  one_more = input("Nice game! One more? [y/n]")
  if one_more == 'n':
    oneMore = False #if player doesn't want to play again, end game
  elif one_more == 'y':
    theBoard = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #if player want to play one more time, initialize the board again
    win = False

print("Thank you for playing! Bye!")