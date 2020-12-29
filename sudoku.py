board =[
    [0,9,0,0,5,8,6,0,4],
    [0,0,5,7,6,3,0,0,9],
    [6,3,8,0,2,0,0,7,1],
    [0,0,0,4,1,0,7,8,0],
    [0,6,0,0,0,9,0,1,2],
    [0,0,1,3,0,2,9,6,0],
    [0,8,0,0,9,1,0,4,7],
    [3,1,0,6,4,7,2,5,8],
    [7,2,0,0,0,5,1,9,6]

]

def solve_sudoku(board):
    find = find_empty_cell(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid_sudoku(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def valid_sudoku(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True



def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ", end="")


def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

print_sudoku(board)
solve_sudoku(board)
print("      ")
print("      ")
print("The solution of the sudoku is")
print("      ")
print_sudoku(board)





