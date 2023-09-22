def createBoard():
    print(" __ __ __ __ __ __ ")
    print("|__%c__|__%c__|__%c__|" % (board[0], board[1], board[2]))
    print("|__%c__|__%c__|__%c__|" % (board[3], board[4], board[5]))
    print("|__%c__|__%c__|__%c__|" % (board[6], board[7], board[8]))

def CheckPos(i):
    if board[i] == ' ':
        return True
    else:
        return False

def changePlayers():
    global player, Sign
    if (player%2 != 0):
        Sign = 'X'
    else:
        Sign = 'O'
    player += 1

def CheckWin():
    global Game, moves
    if ((board[0]==board[1] and board[1]==board[2] and board[0]=='X')or
        (board[3]==board[4] and board[4]==board[5] and board[3]=='X')or
        (board[6]==board[7] and board[7]==board[8] and board[6]=='X')or
        (board[0]==board[3] and board[3]==board[6] and board[0]=='X')or
        (board[1]==board[4] and board[4]==board[7] and board[1]=='X')or
        (board[2]==board[5] and board[5]==board[8] and board[2]=='X')or
        (board[0]==board[4] and board[4]==board[8] and board[0]=='X')or
        (board[2]==board[4] and board[4]==board[6] and board[2]=='X')):
        print("Player 1 wins")
        Game = "Over"
    elif ((board[0]==board[1] and board[1]==board[2] and board[0]=='O')or
        (board[3]==board[4] and board[4]==board[5] and board[3]=='O')or
        (board[6]==board[7] and board[7]==board[8] and board[6]=='O')or
        (board[0]==board[3] and board[3]==board[6] and board[0]=='O')or
        (board[1]==board[4] and board[4]==board[7] and board[1]=='O')or
        (board[2]==board[5] and board[5]==board[8] and board[2]=='O')or
        (board[0]==board[4] and board[4]==board[8] and board[0]=='O')or
        (board[2]==board[4] and board[4]==board[6] and board[2]=='O')):
        print("Player 2 wins")
        Game = "Over"
    elif moves == 9:
        print("It's a draw")
        Game = "Over"

def GoalBasedAgent():
    global Game, player, moves
    Game = "Running"
    moves = 0
    while (Game == "Running"):
        createBoard()
        changePlayers()
        pos = int(input("Enter position:"))
        if (CheckPos(pos)):
            board[pos] = Sign
            moves += 1
            CheckWin()

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1
Sign = 'X'
Game = "Running"
moves = 0

print("This is a 3x3 Simple Tic-Tac-Toe game, a problem scenario for Goal-Based agent.")
print("Player1-X\nPlayer2-O")
GoalBasedAgent()
print("Agent has completed its task")