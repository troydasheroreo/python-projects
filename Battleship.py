print('Welcome to Battleship!')

w = '~'
hit = '*'

grid = [
[' ',0,1,2,3,4,5,6,7,8,9],
['A',w,w,w,w,w,w,w,w,w,w],
['B',w,w,w,w,w,w,w,w,w,w],
['C',w,w,w,w,w,w,w,w,w,w],
['D',w,w,w,w,w,w,w,w,w,w],
['E',w,w,w,w,w,w,w,w,w,w],
['F',w,w,w,w,w,w,w,w,w,w],
['G',w,w,w,w,w,w,w,w,w,w],
['H',w,w,w,w,w,w,w,w,w,w],
['I',w,w,w,w,w,w,w,w,w,w],
['J',w,w,w,w,w,w,w,w,w,w],
    ]





def show_grid():
    for row in grid:
        for col in row:
            print(col, end=' ')
        print()
        




def shoot():
    
    target_row = input("What row do you wish to attack? > ").strip().lower()
    target_col = input("What column do you wish to attack? > ").strip()

    row_num = {'a' :1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}


    row = row_num[target_row]
    col= int(target_col) + 1
    grid [row] [col] = hit

while True:
    
    show_grid()
    shoot()


