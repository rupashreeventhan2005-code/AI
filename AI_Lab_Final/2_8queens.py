def solve(row, n, board):
    if row == n:
        print(board)
        return True
    for col in range(n):
        if all(board[i] != col and abs(board[i]-col) != row-i for i in range(row)):
            board.append(col)
            if solve(row+1, n, board):
                return True
            board.pop()
    return False

n = int(input("Enter number of queens: "))
if not solve(0, n, []):
    print("No solution")
