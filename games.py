class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.symbol1 = "X"
        self.symbol2 = "O"
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.game_on = True
        self.t = 1
        self.name = ""
        self.score = {self.player1: 0, self.player2: 0}

    def play_game(self):
        while self.game_on == True:
            if self.t % 2 == 0:
                self.name = self.player2
                mark = self.symbol2
            else:
                self.name = self.player1
                mark = self.symbol1
            player_input = input(f"Hey {self.name},please enter the column,row of your choice: ")
            try:
                position = player_input.split(",")
                col = int(position[0]) - 1
                row = int(position[1]) - 1
                if col < 3 and row < 3:
                    if self.board[col][row] == " ":
                        self.board[col][row] = mark
                        self.t += 1
                        print(f'''
                        {self.board[0][0]}|{self.board[1][0]}|{self.board[2][0]}
                        ------  
                        {self.board[0][1]}|{self.board[1][1]}|{self.board[2][1]}
                        ------  
                        {self.board[0][2]}|{self.board[1][2]}|{self.board[2][2]}
                        ''')
                        self.check_board_status()
                    else:
                        print("Hey,it's already marked!Please try again!")
                else:
                    print("Wrong Input! Please try again!")
            except ValueError:
                print("Wrong input! Please try again!")
            except TypeError:
                print("Wrong input! Please try again!")

    # Check for all winning patterns:
    def check_board_status(self):
        for i in range(0, 3):
            column = self.board[i]
            if column[0] == column[1] == column[2] != " ":
                self.game_on = False
                print(f"{self.name} wins the game!")
                self.score[self.player1] += 1
                return self.score
        for i in range(0, 3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                self.game_on = False
                print(f"{self.name} wins the game!")
                self.score[self.player1] += 1
                return
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != " ") or (
                self.board[2][0] == self.board[1][1] == self.board[0][2] != " "):
            self.game_on = False
            print(f"{self.name} wins the game!")
            self.score[self.player1] += 1
            return

        elif self.t == 9:
            self.game_on = False
            print("GAME OVER!")
            return
