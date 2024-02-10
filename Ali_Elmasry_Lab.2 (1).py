#!/usr/bin/env python
# coding: utf-8

# ## Lab 2- Tic Tac Toe
# 
# In this lab your will build a n x n Tic Tac Toe game. As you do the exercises, make sure your solutions work for any size Tic Tac Toe game. 

# *Exercise 1:* Write a function that creates an n by n matrix (of list of lists) which will represent the state of a Tie Tac Toe game. Let 0, 1, and 2 represent empty, "X", and "O", respectively.
# 

# In[1]:


# Write you solution here
player_1 = "X"
player_2 = "O"
empty = 0
#size =


# In[2]:


player_1 = "X"
player_2 = "O"
empty = 0


# *Exercise 2:* Write a function that takes 2 integers `n` and `m` as input and draws a `n` by `m` game board. For example the following is a 3x3 board:
# ```
#    --- --- --- 
#   |   |   |   | 
#    --- --- ---  
#   |   |   |   | 
#    --- --- ---  
#   |   |   |   | 
#    --- --- --- 
#    ```

# In[3]:


n = 3
m = 3
board = list()
for i in range(n):
    row = list()
    for j in range(m):
        row.append(empty)
    
    board.append(row)

def create_game_board():
    for i in range(n):
        print("\n", end="")
        print(" ---" * m)
        print("|", end="")
        for j in range(m):
            print("",board[i][j], end= " |" )
    print("\n", end="")
    print(" ---" * m)


# In[4]:


board_0 = create_game_board()


# *Exercise 3:* Modify exercise 2, so that it takes a matrix of the form from exercise 1 and draws a tic-tac-tie board with "X"s and "O"s.  

# In[5]:


n = 3
m = 3
board = list()
for i in range(n):
    row = list()
    for j in range(m):
        row.append(empty)
    
    board.append(row)

pieces = 0

for a in range(n):
    for b in range(m):
        if pieces:
            board[a][b]="X"
            pieces-= 1
        else:
            board[a][b]="O"
            pieces+= 1
            
            
def create_game_board():
    for i in range(n):
        print("\n", end="")
        print(" ---" * m)
        print("|", end="")
        for j in range(m):
            print("",board[i][j], end= " |" )
    print("\n", end="")
    print(" ---" * m)


# In[6]:


board_0 = create_game_board()


# In[ ]:





# *Exercise 4:* Write a function that takes a `n` by `n` matrix representing a tic-tac-toe game, and returns -1, 0, 1, or 2 indicating the game is incomplete, the game is a draw, player 1 has won, or player 2 has one, respectively. Here are some example inputs you can use to test your code:

# In[7]:


n = 3
board = list()
for i in range(n):
    row = list()
    for j in range(n):
        row.append(empty)
    
    board.append(row)

winner_is_2 = [["O", "O", " "],
	["O", "X", " "],
	["O", "X", "X"]]

winner_is_1 = [["X", "O", "O"],
	["O", "X", "O"],
	["O", " ", "X"]]

winner_is_also_1 = [["X", "X", " "],
	["O", "X", " "],
	["O", "X", "O"]]

no_winner = [["X", "O", " "],
	["O", "X", " "],
	["O", "X", "O"]]

also_no_winner = [["X", "O", " "],
	["O", "X", " "],
	["O", "X", " "]]
            
            
def create_game_board(myBoard):
    for i in range(n):
        print("\n", end="")
        print(" ---" * n)
        print("|", end="")
        for j in range(n):
            print("",myBoard[i][j], end= " |" )
    print("\n", end="")
    print(" ---" * n)


# In[8]:


board_0 = create_game_board(also_no_winner)


# In[9]:


winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]


# *Exercise 5:* Write a function that takes a game board, player number, and `(x,y)` coordinates and places "X" or "O" in the correct location of the game board. Make sure that you only allow filling previously empty locations. Return `True` or `False` to indicate successful placement of "X" or "O".

# In[10]:


n = 3
board = list()
for i in range(n):
    row = list()
    for j in range(n):
        row.append(empty)
    
    board.append(row)

board = [[" ", "O", " "],
	["O", "X", " "],
	["O", "X", "X"]]    

player = 1

def create_game_board(myBoard,next_player,x,y):
    x -= 1
    y -= 1
    print("Player", next_player, "turn:")
    if board[x][y]==" ":
        my_turn = True
        board[x][y] = "O"
    else:
        my_turn = False
    for i in range(n):
        print("\n", end="")
        print(" ---" * n)
        print("|", end="")
        for j in range(n):   
            print("",myBoard[i][j], end= " |" )
    print("\n", end="")
    print(" ---" * n)
    if my_turn:
        print("Successful turn")
    else:
        print("Invalid move")
    return(my_turn)


# In[11]:


board_0 = create_game_board(board,player, 1,1)


# *Exercise 6:* Modify Exercise 4 to show column and row labels so that players can specify location using "A2" or "C1".

# In[12]:


n = 3
board = list()
for i in range(n):
    row = list()
    for j in range(n):
        row.append(empty)
    
    board.append(row)

winner_is_2 = [["O", "O", " "],
	["O", "X", " "],
	["O", "X", "X"]]

winner_is_1 = [["X", "O", "O"],
	["O", "X", "O"],
	["O", " ", "X"]]

winner_is_also_1 = [["X", "X", " "],
	["O", "X", " "],
	["O", "X", "O"]]

no_winner = [["X", "O", " "],
	["O", "X", " "],
	["O", "X", "O"]]

also_no_winner = [["X", "O", " "],
	["O", "X", " "],
	["O", "X", " "]]

row_names=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
row_map=dict(zip(row_names,range(n)))
column_names = list(map(str, range(1, n+1)))
column_map = dict(zip(column_names, range(n)))


def create_game_board(myBoard):
    print("  ",end=" ")
    for j in range(n):
        print(column_names[j],"  ", end=" ")

    for i in range(n):
        print("\n", end="")
        print("  ---" * n)
        print(row_names[i],end="")
        
        for j in range(n):
            print(" |", end="")
            print(myBoard[i][j], end= "| " )
    print("\n", end="")
    print("  ---" * n)


# In[13]:


board_0 = create_game_board(winner_is_also_1)


# *Exercise 7:* Write a function that takes a board, player number, and location specified as in exercise 6 and then calls exercise 5 to correctly modify the board.  

# In[32]:


n = 3
board = list()
for i in range(n):
    row = list()
    for j in range(n):
        row.append(empty)
    
    board.append(row)

winner_is_2 = [[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "]]



row_names=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
row_map=dict(zip(row_names,range(n)))
column_names = list(map(str, range(1, n+1)))
column_map = dict(zip(column_names, range(n)))

player = 1


def parse_location(l_string):
    if not isinstance(l_string,str):
        print("Bad Input. Location must be string.")
        return False
    
    if len(l_string)!=2:
        print("Bad Input. Location must be 2 characters.")
        return False
    
    row=l_string[0].upper()
    col=l_string[1].upper()
    
    if not row in row_names:
        print("Bad Row.")
        return False

    if not col in column_names:
        print("Bad Column.")
        return False

    return row_map[row],column_map[col]

def create_game_board(myBoard,next_player,location):     
    parse_location(location)
    R,C = location
    x = row_map[R]
    y = column_map[C]
    
    if next_player == 1:
            piece = "X"
    elif next_player == 2:
            piece = "O"
    else:
        print("Invalid player")

    print("Player", next_player, "turn:")
    if myBoard[x][y]==" ":
        my_turn = True
        myBoard[x][y] = piece
    else:
        my_turn = False
        
    print("  ",end=" ")
    for j in range(n):
        print(column_names[j],"  ", end=" ")

    for i in range(n):
        print("\n", end="")
        print("  ---" * n)
        print(row_names[i],end="")
        
        for j in range(n):
            print(" |", end="")
            print(myBoard[i][j], end= "| " )
    print("\n", end="")
    print("  ---" * n)
    if my_turn:
        print("Successful turn")
    else:
        print("Invalid move")
    return(my_turn)


# In[34]:


board_0 = create_game_board(winner_is_2, 2, "A3")


# *Exercise 8:* Write a function is called with a board and player number, takes input from the player using python's `input`, and modifies the board using your function from exercise 7. Note that you should keep asking for input until you have gotten a valid input that results in a valid move.

# In[35]:


n = 3
board = list()
for i in range(n):
    row = list()
    for j in range(n):
        row.append(empty)
    
    board.append(row)

new_board = [[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "]]



row_names=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
row_map=dict(zip(row_names,range(n)))
column_names = list(map(str, range(1, n+1)))
column_map = dict(zip(column_names, range(n)))

player = 1


def parse_location(l_string):
    if not isinstance(l_string,str):
        print("Bad Input. Location must be string.")
        return False
    
    if len(l_string)!=2:
        print("Bad Input. Location must be 2 characters.")
        return False
    
    row=l_string[0].upper()
    col=l_string[1].upper()
    
    if not row in row_names:
        print("Bad Row.")
        return False

    if not col in column_names:
        print("Bad Column.")
        return False

    return row_map[row],column_map[col]

def create_game_board(myBoard,location):
    print("Please enter a valid player number of 1 or 2.")
    playerflag = False
    while playerflag == False:
        next_player = input(str)
        if next_player == "1":
            piece = "X"
            playerflag = True
        elif next_player == "2":
            piece = "O"
            playerflag = True
        else:
            print("Invalid player. Re-enter a valid player number.")
       
    parse_location(location)
    R,C = location
    x = row_map[R]
    y = column_map[C]
    

    print("Player", next_player, "turn:")
    if myBoard[x][y]==" ":
        my_turn = True
        myBoard[x][y] = piece
    else:
        my_turn = False
        
    print("  ",end=" ")
    for j in range(n):
        print(column_names[j],"  ", end=" ")

    for i in range(n):
        print("\n", end="")
        print("  ---" * n)
        print(row_names[i],end="")
        
        for j in range(n):
            print(" |", end="")
            print(myBoard[i][j], end= "| " )
    print("\n", end="")
    print("  ---" * n)
    if my_turn:
        print("Successful turn")
    else:
        print("Invalid move")
    return(my_turn)


# In[36]:


board_0 = create_game_board(winner_is_2, "A1")


# *Exercise 9:* Use all of the previous exercises to implement a full tic-tac-toe game, where an appropriate board is drawn, 2 players are repeatedly asked for a location coordinates of where they wish to place a mark, and the game status is checked until a player wins or a draw occurs.

# In[1]:


n = 3
board = [[" " for _ in range(n)] for _ in range(n)]

row_names = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
row_map = dict(zip(row_names, range(n)))
column_names = list(map(str, range(1, n + 1)))
column_map = dict(zip(column_names, range(n)))

def parse_location(l_string):
    if not isinstance(l_string, str):
        print("Bad Input. Location must be string.")
        return False
    
    if len(l_string) != 2:
        print("Bad Input. Location must be 2 characters.")
        return False
    
    row = l_string[0].upper()
    col = l_string[1].upper()
    
    if row not in row_names:
        print("Bad Row.")
        return False

    if col not in column_names:
        print("Bad Column.")
        return False

    return row_map[row], column_map[col]

def print_board(my_board):
    print("  ",end=" ")
    for j in range(n):
        print(column_names[j],"  ", end=" ")

    for i in range(n):
        print("\n", end="")
        print("  ---" * n)
        print(row_names[i],end="")
        
        for j in range(n):
            print(" |", end="")
            print(my_board[i][j], end= "| " )
    print("\n", end="")
    print("  ---" * n)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(n):
        if all(board[row][col] == player for row in range(n)):
            return True

    if all(board[i][i] == player for i in range(n)) or \
       all(board[i][n - 1 - i] == player for i in range(n)):
        return True

    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def create_game_board():
    player = "X"
    while True:
        print_board(board)
        print(f"Player {player}'s turn:")
        location = input("Enter your move: ")
        if parse_location(location):
            row, col = parse_location(location)
        else:
            continue
        if row is None or col is None or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = player
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"


# In[51]:


create_game_board()


# *Exercise 10:* Test that your game works for 5x5 Tic Tac Toe.  

# In[2]:


n = 5
board = [[" " for _ in range(n)] for _ in range(n)]

row_names = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
row_map = dict(zip(row_names, range(n)))
column_names = list(map(str, range(1, n + 1)))
column_map = dict(zip(column_names, range(n)))

def parse_location(l_string):
    if not isinstance(l_string, str):
        print("Bad Input. Location must be string.")
        return False
    
    if len(l_string) != 2:
        print("Bad Input. Location must be 2 characters.")
        return False
    
    row = l_string[0].upper()
    col = l_string[1].upper()
    
    if row not in row_names:
        print("Bad Row.")
        return False

    if col not in column_names:
        print("Bad Column.")
        return False

    return row_map[row], column_map[col]

def print_board(my_board):
    print("  ",end=" ")
    for j in range(n):
        print(column_names[j],"  ", end=" ")

    for i in range(n):
        print("\n", end="")
        print("  ---" * n)
        print(row_names[i],end="")
        
        for j in range(n):
            print(" |", end="")
            print(my_board[i][j], end= "| " )
    print("\n", end="")
    print("  ---" * n)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(n):
        if all(board[row][col] == player for row in range(n)):
            return True

    if all(board[i][i] == player for i in range(n)) or \
       all(board[i][n - 1 - i] == player for i in range(n)):
        return True

    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def create_game_board():
    player = "X"
    while True:
        print_board(board)
        print(f"Player {player}'s turn:")
        location = input("Enter your move: ")
        if parse_location(location):
            row, col = parse_location(location)
        else:
            continue
        if row is None or col is None or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = player
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"


# In[53]:


create_game_board()


# *Exercise 11:* (Advanced / Challenge) Develop a version of the game where one player is the computer. Note that you don't need to do an extensive seach for the best move. You can have the computer simply protect against loosing and otherwise try to win with straight or diagonal patterns.

# In[ ]:


# Write you solution here


# In[ ]:


# Test your solution here


# In[ ]:




