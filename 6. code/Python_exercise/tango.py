def fill_array_with_sun_and_moon(matrix):
    for i in range(6):
        for j in range(6):
            matrix[i][j] = '_'

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))


def process_signs(matrix, signs):
    for sign in signs:
        (x1, y1), (x2, y2), sign_type = sign
        if sign_type == '=':
            if x1 == x2 or y1 == y2:
                if matrix[x1][y1] != '':
                    matrix[x2][y2] = matrix[x1][y1]
                elif matrix[x2][y2] != '':
                    matrix[x1][y1] = matrix[x2][y2]
        elif sign_type == 'x':
            if matrix[x1][y1] == 'S' and matrix[x2][y2] == '':
                matrix[x2][y2] = 'M'
            elif matrix[x1][y1] == 'M' and matrix[x2][y2] == '':
                matrix[x2][y2] = 'S'
            elif matrix[x2][y2] == 'S' and matrix[x1][y1] == '':
                matrix[x1][y1] = 'M'
            elif matrix[x2][y2] == 'M' and matrix[x1][y1] == '':
                matrix[x1][y1] = 'S'


matrix = [['' for _ in range(6)] for _ in range(6)]
filled_matrix = fill_array_with_sun_and_moon(matrix)

input_sun_moon = input(
    "Enter the coordinates of sun, moon and value format: x,y,value x,y,value): "
)
input_coordinates = [entry.split(',') for entry in input_sun_moon.split()]
input_signs = input("Enter the coordinates of sign and value format: x1,y1,x2,y2,sign x1,y1,x2,y2,sign): ")

for x, y, value in input_coordinates:
    filled_matrix[int(x)][int(y)] = value
print_matrix(matrix)
print('====================== After filled')
updated = True  # Flag to track changes in the matrix
rows, cols = 6, 6
while updated:  # Repeat until no changes are made
    updated = False  # Reset the flag at the start of each iteration
    for row in range(rows - 1):  # Check vertically
        for col in range(cols):
            # Check vertically for 'S' and update surrounding cells
            if matrix[row][col] == matrix[row + 1][col] == 'S':
                if row > 0 and matrix[row - 1][col] == '_':
                    matrix[row - 1][col] = 'M'
                    updated = True
                if row + 2 < rows and matrix[row + 2][col] == '_':
                    matrix[row + 2][col] = 'M'
            # Check vertically for 'M' and update surrounding cells
            elif matrix[row][col] == matrix[row + 1][col] == 'M':
                if row > 0 and matrix[row - 1][col] == '_':
                    matrix[row - 1][col] = 'S'
                    updated = True
                if row + 2 < rows and matrix[row + 2][col] == '_':
                    matrix[row + 2][col] = 'S'

    for row in range(rows):  # Check horizontally
        for col in range(cols - 1):
            # Check horizontally for 'S' and update surrounding cells
            if matrix[row][col] == matrix[row][col + 1] == 'S':
                if col > 0 and matrix[row][col - 1] == '_':
                    matrix[row][col - 1] = 'M'
                    updated = True
                if col + 2 < cols and matrix[row][col + 2] == '_':
                    matrix[row][col + 2] = 'M'
            # Check horizontally for 'M' and update surrounding cells
            elif matrix[row][col] == matrix[row][col + 1] == 'M':
                if col > 0 and matrix[row][col - 1] == '_':
                    matrix[row][col - 1] = 'S'
                    updated = True
                if col + 2 < cols and matrix[row][col + 2] == '_':
                    matrix[row][col + 2] = 'S'
print_matrix(matrix)
