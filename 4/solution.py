# Advent of Code Day
# Science Lab Linkki, Virpi Sumu

def read_file(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append((line.strip()))

    return contents

#tarkistaa löytyykö numero kyseisestä pelilaudasta, palauttaa indeksin tuplena jos löytyi
def find_index(item: int, board: list):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if item == board[i][j]:
                return (i,j)
    return None

# laskee voittaneen pelilaudan tuloksen eli
# niiden laudalla olevien numeroiden summa, joita ei ole vielä huudettu
# kerrottuna sillä numerolla, minkä huutaminen sai aikaan voittavan rivin/sarakkeen
def calculate_result(winboard, checkboard, number):
    result = 0
    for i in range(5):
        for j in range(5):
            if checkboard[i][j] == 0:
                result += winboard[i][j]
    result *= number
    return result

file_contents = read_file("input.txt")

result1 = 0
result2 = 0

#käsittele eka rivi syötettä
numbers = [int(number) for number in file_contents[0].split(',')]

#käsittele muut rivit syötteestä listaksi matriiseja
#luo myös tarkistusmatriisit
boards = []
checkboards = []
board = []
for line in file_contents[2:]:
    if line != '':
        board.append([int(number) for number in line.split()])
    else:
        checkboards.append([ [0 for i in range(5)] for j in range(5) ])
        boards.append(board)
        board = []

#viimeistä matriisia ei lisätä listaan yllä joten tehdään se tässä
checkboards.append([ [0 for i in range(5)] for j in range(5) ])
boards.append(board)

won_boards = []

#käy läpi arvottujen numeroiden lista
for number in numbers:
    for i in range(len(boards)):
        #pelilauta eli matriisi tarkistetaan vain jos se ei jo voittanut
        if i not in won_boards:
            found_index = find_index(number, boards[i])
            if found_index != None:
                x, y = found_index
                checkboards[i][x][y] = 1
                # tarkista tuliko voittava rivi tai sarake täyteen
                if (sum(checkboards[i][x]) == 5) or (sum([row[y] for row in checkboards[i]]) == 5) : # won!
                    # ensimmäinen voittava pelilauta
                    if result1 == 0:
                        result1 = calculate_result(boards[i], checkboards[i], number)
                    won_boards.append(i)
                    # viimeinen voittava pelilauta
                    if len(won_boards) == len(boards):
                        result2 = calculate_result(boards[i], checkboards[i], number)
            
# Task 1: 74320
print("Task 1:", result1)

# Task 2: 17884
print("Task 2:", result2)
