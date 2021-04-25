from __future__ import print_function
cau_do = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
#Ham in ra sudoku
def sudoku(q):
    for d in range(len(q)):
        if d%3 == 0 and d != 0 :    #d la dong va c la cot
            print("- - - - - - - - - - -")
        for c in range(len(q[0])):
            if c%3 and c!=0:
                print("|")
            if c == 8:
                print(str(q[d][c]))
            else:
                print(str(q[d][c]) + "" )


#Ham tim loi giai cho Sudoku

def solution(q):
    tim_thay = findEmpty(q)
    if not tim_thay:
        return True
    else:
        d,c = tim_thay
    for i  in range(1,10):
        if test(q, i, d, c):
            q[d][c] = i
            if solution(q):
                return True
            else:
                q[d][c] = 0
    return False

#Ham tim o trong
def findEmpty(q):
    for d in range(len(q)):
        for c in range(len(q[0])):
            if q[d][c] == 0 :
                return d,c
    return None
#Ham kiem tra tinh hop le cua mot cau do
def test(q, value, row ,col):
    for i in range(len(q[0])):
        if q[i][col] == value and i!= row:
            return False
    for i in range(len(q)):
        if q[row][i] == value and i != col:
            return False
    
    x = col // 3
    y = row // 3

    for i in range(y*3,y*3+3):
        for j in range(x*3,x*3+3):
            if q[i][j] == value and i!= row and j!= col :
                return False
    return True
sudoku(cau_do)
solution(cau_do)
print('Loi giai cua cau do tren la: ')
sudoku(cau_do)

