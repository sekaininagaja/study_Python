grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

tate = len(grid)
yoko = len(grid[0])
tate_count = 0
yoko_count = 0

while tate_count < tate:
  for yoko_count in range(yoko):
    if yoko_count != yoko - 1:
      print(grid[tate_count][yoko_count], end='')
      yoko_count += 1
    else:
      print(grid[tate_count][yoko_count])
      break
  tate_count += 1
