def game_status(board_size, board):
    test = []
    for i in range(board_size):
        character = board[i]
        if character not in test:
            test.append(character)
        else:
            test = []
            return "impossible"
    for i in range(board_size):
        character = board[i]
        if "." not in character:
            for j in character:
                if j != character[i]:
                    return "impossible"
            for j in character:
                if j == "B":
                    return "Blue Wins."
                elif j == "R":
                    return "Red Wins."
                else:
                    return "Nobody Wins."
    return "Nobody Wins."


def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        board_size = int(input())
        board = []
        for _ in range(board_size):
            board.append(list(input().strip()))

        ans = game_status(board_size, board)

        print("Case #{}: {}".format(test_case, ans))


if __name__ == "__main__":
    main()
