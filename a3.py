def is_valid_word(wordlist, word):
        if word in wordlist:
            return True
        return False

def make_str_from_row(board, row_index):
        string = ''
        for elem in range(0, len(board[row_index])):
                string = string + board[row_index][elem]
        return string

def make_str_from_column(board, column_index):
        string = ''
        for lst in range(0, len(board)):
                string = string + board[lst][column_index]
        return string

def board_contains_word_in_row(board, word):
        for row_index in range(len(board)):
                if word in make_str_from_row(board, row_index):
                        return True
        return False

def board_contains_word_in_column(board, word):
        for column_index in range (len(board[0])):
                if word in make_str_from_column(board, column_index):
                        return True
        return False

def board_contains_word(board, word):
        if board_contains_word_in_row(board, word) is True:
                return True
        elif board_contains_word_in_column(board, word) is True:
                return True
        else:
                return False

def word_score(word):
        if len(word) < 3:
                return 0
        elif len(word) >=3 and len(word) < 7:
                return len(word) * 1
        elif len(word) >= 7 and len(word) < 10:
                return len(word)* 2
        else:
                return len(word) * 3

def update_score(player_info, word):
        player_info[1] = player_info[1] + word_score(word)

def num_words_on_board(board, words):
        cols = 0
        rows = 0
        for word in range(0, len(words)):
                if board_contains_word_in_row(board, words[word]) is True:
                        rows = rows + 1
                if board_contains_word_in_column(board, words[word]) is True:
                        cols = cols + 1
        return rows + cols

def read_words(words_file):
        words_list = []
        words = words_file.readlines()
        for word in words:
                word = word.rstrip('\n')
                words_list.append(word)

        return words_list

def read_board(board_file):
        board = []
        board_row = []
        i = 0

        for line in board_file:
                line = line.rstrip('\n')
                board_row += line
                board.insert( i, board_row )
                i = i + 1
                board_row = []

        return board
