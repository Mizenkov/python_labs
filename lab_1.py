board_size = 3

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_board():
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)
    pass

def input_validation(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and 0 <= int(user_input) <= 9:
            return int(user_input)
        else:
            print("Invalid input! Enter a number from 1 to 9 or 0 to exit.")


def game_step(index, char):

    if (index > 9 or index < 1 or board[index - 1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True


def check_win():
    # Ініціалізуємо переможну змінну як False
    win = False

    # Визначаємо всі можливі комбінації для перемоги у вигляді кортежів по трійках позицій
    win_combinations = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    # Проходимося по кожній комбінації у циклі
    for pos in win_combinations:
        # Перевіряємо, чи символи на трьох позиціях поточної комбінації однакові ('X' або 'O')
        if board[pos[0]] == board[pos[1]] == board[pos[2]] and board[pos[0]] in ('X', 'O'):
            # Якщо умова виконується, встановлюємо переможну змінну як символ, що утворює переможну комбінацію
            win = board[pos[0]]
            # Завершуємо цикл, бо вже знайшли переможця
            break

    # Повертаємо символ переможця або False, якщо переможця немає
    return win

def start_game():

    current_player: str = 'X'

    step = 1
    draw_board()

    while (step < 10) and (check_win() == False):
        index = input_validation('player ' + current_player + '. Enter the field number (0 - Output):')

        if (int(index) == 0):
            exit()
        if (game_step(int(index), current_player)):
            print('Success!')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            
            step += 1
        else:
            print('Wrong! Retry!')
    if (step == 10):
        print('Game over. Draw!')
    else:
        print('Winner ' + str(check_win()))


print('Welcome to the game!')

start_game()