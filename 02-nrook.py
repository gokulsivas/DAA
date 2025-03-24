N = int(input("Enter the value of N: "))

solution_count = 0

def print_solution(board):
    global solution_count
    solution_count += 1
    print(f"Solution {solution_count}:\n")
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 'R':
            return False

    for i in range(row):
        if board[i][col] == 'R':
            return False

    return True  

def solve_n_rooks(board, col):
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 'R'  
            res = solve_n_rooks(board, col + 1) or res  
            board[i][col] = '.'  

    return res

def solve():
    board = [['.' for _ in range(N)] for _ in range(N)]

    if not solve_n_rooks(board, 0):
        print("No solution exists.")

solve()