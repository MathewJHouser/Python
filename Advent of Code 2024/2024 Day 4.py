class WordSearch():
    def __init__(self):
        self.word_search = []
        with open("Input Day 4", "r") as f:
            for line in f.readlines():
                self.word_search.append([element for element in line if element != '\n'])
                self.n = len(self.word_search) #row
                self.m = len(self.word_search[0]) #column
                self.word_goal = ["XMAS", "SAMX"]
                self.x_goal = ["MAS", "SAM"]
                self.part1 = 0
                self.part2 = 0

    def xmas_search(self):
        self.row_search()
        self.column_search()
        self.diagonal_search()
        self.x_mas_search()

    def row_search(self):
        for row in self.word_search:
            for i in range(self.m - 3):
                self.part1 += ''.join(row[i:i+4]) in self.word_goal

    def column_search(self):
        for column in zip(*self.word_search):
            for i in range(self.m - 3):
                self.part1 += ''.join(column[i:i+4]) in self.word_goal

    def diagonal_search(self):
        for row in range(self.n-3):
            for col in range(self.m-3):
                diag_1 = ''.join([self.word_search[row][col],
                                  self.word_search[row+1][col+1],
                                  self.word_search[row+2][col+2],
                                  self.word_search[row+3][col+3]])
                diag_2 = ''.join([self.word_search[row+3][col],
                                  self.word_search[row+2][col+1],
                                  self.word_search[row+1][col+2],
                                  self.word_search[row][col+3]])
                self.part1 += diag_1 in self.word_goal
                self.part1 += diag_2 in self.word_goal

    def x_mas_search(self):
        for row in range(self.n-2):
            for col in range(self.m-2):
                diag_1 = ''.join([self.word_search[row][col],
                                  self.word_search[row+1][col+1],
                                  self.word_search[row+2][col+2]])
                diag_2 = ''.join([self.word_search[row+2][col],
                                  self.word_search[row+1][col+1],
                                  self.word_search[row][col+2]])
                self.part2 += diag_1 in self.x_goal and diag_2 in self.x_goal


day4 = WordSearch()
day4.xmas_search()
print("Part One:", day4.part1, "\nPart Two:", day4.part2)