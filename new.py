import numpy as np
from math import inf as infinity

HUMAN = -1
COMP = 1

def check3num(num):
    if(len(str(num))==1):
        return "00"+str(num)
    elif(len(str(num))==2):
        return "0"+str(num)
    return str(num) 


#Tao ban co thanh mot array
def board(size):
    state = np.zeros(size*size)
    state = state.reshape(size,size)
    return state

#Ve ban co
def draw_board(board):

    line = '-------'*(len(board))
    temp = 0
    for row in range(len(board)):
        print(line, end="\n|| ")
        for col in range(len(board[row])):
            temp+=1
            if(board[row][col] == 0.0):
                print(check3num(temp),end=' || ')
            elif(board[row][col] == 1):
                print(' X ', end=' || ')
            elif(board[row][col] == -1):
                print(' O ', end=' || ')
            
        print()

#Kiem tra nuoc di co hop le hay khong?
def valid_move(board, x, y):
    if(board[x][y] == 0.0 and x != len(board) -1 and x!=0 and  y != len(board)-1 and y!=0):
        return True
    return False
    
#thiet lap lai nuoc di
def set_move(board, x, y, player):
    if(valid_move(board, x, y)):
        board[x][y] = player
        return True
    else:
        return False

def score_row(board, x, y, choice):
    score = 0

    if(
        board[x][y] == choice and 
        board[x][y+1] == choice and 
        board[x][y+2] == choice and 
        board[x][y+3] == choice and
        board[x][y+4] == choice
    ):
        score = 5
        return score
    if(
        board[x][y] == choice and 
        board[x][y+1] == choice and 
        board[x][y+2] == choice and 
        board[x][y+3] == choice
    ):
        score = 4
        return score
    if(
        board[x][y] == choice and 
        board[x][y+1] == choice and 
        board[x][y+2] == choice
    ):
        score = 3
        return score
    if(
        board[x][y] == choice and 
        board[x][y+1] == choice 
    ):
        score = 2
        return score
    if(
        board[x][y] == choice
    ):
        score = 1
        return score

    return score
        
def score_col(board, x, y, choice):
    score = 0
    if(
        board[x][y] == choice and 
        board[x+1][y] == choice and 
        board[x+2][y] == choice and 
        board[x+3][y] == choice and
        board[x+4][y] == choice
    ):
        score = 5
        return score
    if(
        board[x][y] == choice and 
        board[x+1][y] == choice and 
        board[x+2][y] == choice and 
        board[x+3][y] == choice
    ):
        score = 4
        return score
    if(
        board[x][y] == choice and 
        board[x+1][y] == choice and 
        board[x+2][y] == choice
    ):
        score = 3
        return score
    if(
        board[x][y] == choice and 
        board[x+1][y] == choice
    ):
        score = 2
        return score

    if(board[x][y] == choice): 
        score = 1
        return score

    return score

def score_left2right_up(board, x, y, choice):
    score = 0
    if(
        board[x][y] == choice and 
        board[x-1][y+1] == choice and 
        board[x-2][y+2] == choice and 
        board[x-3][y+3] == choice and
        board[x-4][y+4] == choice   
    ):
        score = 5
        return score
    if(
        board[x][y] == choice and 
        board[x-1][y+1] == choice and 
        board[x-2][y+2] == choice and 
        board[x-3][y+3] == choice
    ):
        score = 4
        return score
    if(
        board[x][y] == choice and 
        board[x-1][y+1] == choice and 
        board[x-2][y+2] == choice
    ):
        score = 3
        return score
    if(
        board[x][y] == choice and 
        board[x-1][y+1] == choice
    ):
        score = 2
        return score
    if(
        board[x][y] == choice
    ):
        score = 1
        return score

    return score

def score_left2right_down(board, x, y, choice):
    score = 0
        
    if(
        board[x][y] == choice and 
        board[x+1][y+1] == choice and 
        board[x+2][y+2] == choice and 
        board[x+3][y+3] == choice and
        board[x+4][y+4] == choice
    ):
        score = 5
        return score
    if(
        board[x][y] == choice and 
        board[x+1][y+1] == choice and 
        board[x+2][y+2] == choice and 
        board[x+3][y+3] == choice
    ):
        score = 4
        return score
    if(
        board[x][y] == choice and 
        board[x+1][y+1] == choice and 
        board[x+2][y+2] == choice
    ):
        score = 3
        return score
    if(
        board[x][y] == choice and 
        board[x+1][y+1] == choice
    ):
        score = 2
        return score
    if(board[x][y] == choice): 
        score = 1    
        return score

    return score

##check ban co
def return_score(board, choice):
    for row in range(len(board)):
        for col in range(len(board[row])):

            #check theo hang ngang
            if(score_row(board, row, col, choice) > 0):
                score = score_row(board, row, col, choice)
                # check_human_comp(choice)
                return score, row, col

            if(score_col(board, row, col, choice) > 0):
                score = score_col(board, row, col, choice)
                # check_human_comp(choice)
                return score, row, col

            if(score_left2right_down(board, row, col,choice)):
                score = score_left2right_down(board, row, col,choice)
                # check_human_comp(choice)
                return score, row, col

            if(score_left2right_up(board, row, col, choice)):
                score = score_left2right_up(board, row, col, choice)
                check_human_comp(choice)
                return score, row, col
        
    return 0, None, None

def check_status(board, choice):
    for row in range(len(board)):
        for col in range(len(board[row])):
            #check theo hang ngang
            if(score_row(board, row, col, choice) == 5):
                check_human_comp(choice)
                return True

            if(score_col(board, row, col, choice) == 5):
                check_human_comp(choice)
                return True

            if(score_left2right_down(board, row, col,choice) == 5):
                check_human_comp(choice)
                return True

            if(score_left2right_up(board, row, col, choice) == 5):
                check_human_comp(choice)
                return True
    
    return False


#check human or comp
def check_human_comp(choice):
    if(choice == 1):
        print("COMP WINS")
    elif(choice == -1):
        print("HUMAN WINS")





# #thuat toan
def alphabeta(board, depth, alpha, beta, player):

    results = return_score(board, player)
    value, x, y = results[0], results[1], results[2]

    if(depth == 0 or game_over(board)):
        return value, x, y

    if(player):
        v = -infinity
        for row in range(len(board)):
            for col in range(len(board[row])):
                if(valid_move(board, row, col)):
                    v = max(v, alphabeta(board, depth - 1, alpha, beta, HUMAN)[0])
                      
                    if(v >= alpha):
                        x = row
                        y = col

                    alpha = max(alpha, v)
                    if(beta <= alpha):
                        break
    
        return alpha, x, y
    else:
        v = +infinity
        for row in range(len(board)):
            for col in range(len(board[row])):
                if(valid_move(board, row, col)):
                    v = min(v, alphabeta(board, depth - 1, alpha, beta, COMP)[0])
                    if(v < beta):
                        x = row
                        y = col

                    beta = min(beta, v)

                    if(beta <= alpha):
                        break

        return beta, x, y




    
#check end game
def game_over(board):
    return check_status(board, HUMAN) or check_status(board, COMP)

##Human turn
def human_turn(board, player):
    index = 0
    moves = {}
    move = -1

    if(game_over(board)):
        return

    for row in range(len(board)):
        for col in range(len(board[row])):
            index += 1
            moves[index] = [row, col]
    
    while move < 1 or move > len(board)**2:
        move = int(input("Nhap move: "))
        coord = moves[move]
        if(valid_move(board, coord[0], coord[1])):
            set_move(board, coord[0], coord[1], player)
        else:
            print("Nước đi bị trùng hoặc ngoài vòng, xin thử lại")
            move = -1

    draw_board(board)


def ai_turn(board, player):
    if(game_over(board)):
        return
    
    move = alphabeta(board, 2, -infinity, +infinity, COMP)[1:]
    x, y = move[0], move[1]
    print(move)
    set_move(board, x, y, player)

    draw_board(board)

    return x, y
    


board = board(10)

# print("Update")
draw_board(board)
# print(board)
# check_status(board, 1)
while(check_status(board, COMP) == False and check_status(board, HUMAN) == False):
    # Nguoi choi 1
    human_turn(board, HUMAN)

    #Nguoi choi 2
    ai_turn(board, COMP)

    
