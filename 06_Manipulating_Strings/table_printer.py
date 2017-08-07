#! Python

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(value) :
    col_widths = [0] * len(table_data)
    x = 0
    y = 0
    for y in range(len(table_data)):
        for x in range(len(table_data[x])):
            if col_widths[y] < len(table_data[y][x]):
                col_widths[y] =  len(table_data[y][x])
            x = x + 1
        x = 0
        y = y + 1

    x = 0
    for x in range(len(table_data[x])):
        print(table_data[0][x].rjust(col_widths[0]) + ' ' + table_data[1][x].rjust(col_widths[1]) + ' ' + table_data[2][x].rjust(col_widths[2]))
        x = x + 1
    x = 0

# import pdb; pdb.set_trace()
print_table(table_data)
