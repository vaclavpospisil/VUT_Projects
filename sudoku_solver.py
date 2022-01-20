
A = [[0,0,0,2,7,3,9,0,5],
    [5,0,0,0,0,9,0,3,7],
    [7,9,0,4,0,0,0,0,2],
    [0,8,0,5,2,6,4,0,0],
    [1,6,5,8,0,0,0,0,0],
    [0,0,2,0,9,0,5,0,6],
    [0,0,1,0,0,5,3,6,0],
    [9,3,8,0,6,2,0,0,0],
    [0,0,0,9,3,0,0,2,8]]

def solve_sudoku(A):

    empty_spot = find_empty_field(A)
    if not empty_spot:
        return True
    else:
        R, S = empty_spot
    for cislo in range(1,10):
        if checking_spot(A, cislo, R, S):
            A[R][S] = cislo

            if solve_sudoku(A):
                return True

            A[R][S] = 0
    return False

def checking_spot(A, cislo, R, S):

    # Checking if our selected number is suitable for our combination
    
    for i in range(9):
        if A[R][i] == cislo:
            return False
    
    for j in range(9):
        if A[j][S] == cislo:
            return False
    
    R_x = (R//3)*3
    S_y = (S//3)*3

    for k in range(3):
        for l in range(3):
            if A[R_x+k][S_y+l] == cislo:
                return False

    return True

def print_board(A):

    # Creating borders and filling the playing board
    # First print with our unsolved playing board and second one with solved board

    for i in range(len(A)):

        if i % 3 == 0:
            print("-------------------------")

        for j in range(len(A[0])):

            if  j % 3 == 0:
                print("| ", end="")
            
            if j == 8:
                print(str(A[i][j]) + " |")
            else:
                print(str(A[i][j]) + " ", end="")
    print("-------------------------")

def find_empty_field(A):

    # Finding the empty field in our playing board

    for i in range(9):
        for j in range(9):
            if A[i][j] == 0:
                return (i, j)
    return None

if __name__ == '__main__':
    print("This is your unsolved example!")
    print_board(A)
    solve_sudoku(A)
    print("SUDOKU SOLVED!")
    print("Your solution is below.")
    print_board(A)