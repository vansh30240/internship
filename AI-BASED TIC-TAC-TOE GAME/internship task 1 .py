import math

player = "X"      
ai = "O"          
scores = {"player":0, "ai":0, "draws":0}


board = [" " for _ in range(9)]


def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(b, turn):
    winning_positions = [
        [0,1,2],[3,4,5],[6,7,8],  
        [0,3,6],[1,4,7],[2,5,8],  
        [0,4,8],[2,4,6]           
    ]
    for line in winning_positions:
        if b[line[0]] == turn and b[line[1]] == turn and b[line[2]] == turn:
            return True
    return False


def draw(b):
    return " " not in b


def minimax(b, depth, isMaximizing):
    
    if winner(b, ai):
        return 1
    if winner(b, player):
        return -1
    if draw(b):
        return 0

    if isMaximizing:
        bestScore = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = ai
                score = minimax(b, depth + 1, False)
                b[i] = " "
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = player
                score = minimax(b, depth + 1, True)
                b[i] = " "
                bestScore = min(score, bestScore)
        return bestScore


def ai_move():
    bestScore = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            score = minimax(board, 0, False)
            board[i] = " "
            if score > bestScore:
                bestScore = score
                move = i
    board[move] = ai


def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = player
                break
        print("Invalid move, try again.")


while True:
    board = [" " for _ in range(9)]
    print("\n--- TIC TAC TOE (You = X, AI = O) ---")
    
    while True:
        print_board()
        player_move()

        if winner(board, player):
            print_board()
            print("🎉 You Win!")
            scores["player"] += 1
            break

        if draw(board):
            print_board()
            print("🤝 It's a Draw!")
            scores["draws"] += 1
            break

        ai_move()

        if winner(board, ai):
            print_board()
            print("🤖 AI Wins!")
            scores["ai"] += 1
            break

        if draw(board):
            print_board()
            print("🤝 It's a Draw!")
            scores["draws"] += 1
            break

    print("\nSCOREBOARD:")
    print("You:", scores["player"])
    print("AI:", scores["ai"])
    print("Draws:", scores["draws"])

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
