tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

longest_length = max(len(word) for row in tableData for word in row)
for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print(tableData[j][i].rjust(longest_length), end=" ")
        if j == 2:
            print()