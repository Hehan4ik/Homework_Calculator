class TicTacToe:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        print("  0  1  2")
        for i in range(3):
            print(f"{i} {' '.join(self.board[i])}")

    def make_move(self, row, col):
        if 0 <= row < len(self.board) and 0 <= col < len(self.board[0]) and self.board[row][col] == '-':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            return False

    def check_winner(self):
        for i in range(3):
            # Проверка горизонталей и вертикалей
            if self.board[i][0] != '-' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] != '-' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        # Проверка диагоналей
        if self.board[0][0] != '-' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != '-' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        return None

# Создаем новую игру
game = TicTacToe()

# Основной игровой цикл
while True:
    # Печатаем игровое поле
    game.print_board()

    # Ход игрока
    row = int(input("Выберите строку для вашего хода (0, 1, 2): "))
    col = int(input("Выберите столбец для вашего хода (0, 1, 2): "))

    # Выполняем ход и проверяем его корректность
    if game.make_move(row, col):
        winner = game.check_winner()
        if winner:
            game.print_board()
            print(f"Игрок {winner} победил!")
            break
        elif all(all(cell != '-' for cell in row) for row in game.board):
            game.print_board()
            print("Ничья!")
            break
    else:
        print("Некорректный ход. Попробуйте еще раз.")
