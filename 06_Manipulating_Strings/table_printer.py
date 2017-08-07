#! Python

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(value) :
    col_widths = [0] * len(table_data)
    x = 0
    y = 0

    for x in range(len(table_data[x])):
        for y in range(len(table_data)):
            print('===', y,x, '===')
            if col_widths[y] < len(table_data[y][x]):
                col_widths[y] = len(table_data[y][x])
            print(col_widths[y])
            y = y + 1
#            col_widths[y] = len(table_data[y][x])
        x = x + 1

print_table(table_data)
