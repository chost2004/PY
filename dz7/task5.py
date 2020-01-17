'''
Check Sudoku
'''

def done_or_not(text):
    for i in range(9):
        for p in range (1,10):
            column = []
            for s in range (9):
                column.append(text[s][i])            
            if column.count(p) != 1:
                return False
            if text[i].count(p) != 1:
                return False
    cub1 = []
    cub2 = []
    cub3 = []
    cub4 = []
    cub5 = []
    cub6 = []
    cub7 = []
    cub8 = []
    cub9 = []
    for i in range(3):
        for p in range (3):
            cub1.append (text[i][p])
        for p in range (3,6):
            cub2.append (text[i][p])
        for p in range (6,9):
            cub3.append (text[i][p])
    for i in range(3,6):
        for p in range (3):
            cub4.append (text[i][p])
        for p in range (3,6):
            cub5.append (text[i][p])
        for p in range (6,9):
            cub6.append (text[i][p])
    for i in range(6,9):
        for p in range (3):
            cub7.append (text[i][p])
        for p in range (3,6):
            cub8.append (text[i][p])
        for p in range (6,9):
            cub9.append (text[i][p])
    cubs = [cub1,cub2,cub3,cub4,cub5,cub6,cub7,cub8,cub9]
    for i in cubs:
        for p in range(1,10):
            if i.count(p) != 1:
                return False
    return True

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],[4, 9, 8, 2, 6, 1, 3, 7, 5],[7, 5, 6, 3, 8, 4, 2, 1, 9],[6, 4, 3, 1, 5, 8, 7, 9, 2],[5, 2, 1, 7, 9, 3, 8, 4, 6],[9, 8, 7, 4, 2, 6, 5, 3, 1],[2, 1, 4, 9, 3, 5, 6, 8, 7],[3, 6, 5, 8, 1, 7, 9, 2, 4],[8, 7, 9, 6, 4, 2, 1, 3, 5]]))
print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],[4, 9, 8, 2, 6, 1, 3, 7, 5],[7, 5, 6, 3, 8, 4, 2, 1, 9],[6, 4, 3, 1, 5, 8, 7, 9, 2],[5, 2, 1, 7, 9, 3, 8, 4, 6],[9, 8, 7, 4, 2, 6, 5, 3, 1],[2, 1, 4, 9, 3, 5, 6, 8, 7],[3, 6, 5, 8, 1, 7, 9, 2, 4],[8, 7, 9, 6, 4, 2, 1, 5, 3]]))

    
            
            
    
