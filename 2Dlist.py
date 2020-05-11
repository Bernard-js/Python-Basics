number_matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
	[0]
]

print(number_matrix[2][0])

for row in number_matrix:
    for col in row:
        print(col)


row = 0
while row < len(number_matrix):
    col = 0
    while col <  len(number_matrix[row]):
        print(number_matrix[row][col])
        col += 1
    row += 1