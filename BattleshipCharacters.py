class Ship():
    size = None
    char = None

    def __init__(self):
        self.row = 0
        self.col = 0
        self.direction = None

class Carrier(Ship):
    size = 5
    char = 'C'

class Battleship(Ship):
    size = 4
    char = 'B'

class Destroyer(Ship):
    size = 3
    char = 'D'

class Submarine(Ship):
    size = 3
    char = 'S'

class PatrolBoat(Ship):
    size = 2
    char = 'P'

class Player():
    def __init__(self):
        self.carrier = Carrier()
        self.battleship = Battleship()
        self.destroyer = Destroyer()
        self.submarine = Submarine()
        self.patrolboat = PatrolBoat()
        self.ships = [
            self.carrier,
            self.battleship,
            self.destroyer,
            self.submarine,
            self.patrolboat
        ]
        self.ships_grid = Grid()
        self.shots_grid = Grid()





class Grid():
   
    
    row_num = {'a' :1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9, 'j':10}
    def __init__(self):
        
            w = '~'
            self.rows =[
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
    

class Controller():

    def __init__(self):
        self.player = Player()
        self.computer = Player()
    
    def greet(self):
        print('Prepare for battle!')

    def ask_coord(self):
   
        row = input("row? >").strip().lower()
        col = input("column? >").strip()
        row = Grid.row_num[row]
        col = int(col) + 1
        return (row, col)

    def shoot(self):
        warn = '\u26A0'
        (row, col) = self.ask_coord()
        self.computer.ships_grid.rows[row][col] = warn
        self.player.shots_grid.rows[row][col] = warn

    def play(self):
        while True:
            self.print_player_grids(self.player)
            self.shoot()

    def print_player_grids(self, player):
        
        ul = '\u250F'
        ur = '\u2513'
        ll = '\u2517'
        lr = '\u251B'
        h = '\u2501'
        v = '\u2503'
        uhv = '\u253B'
        lhv = '\u253B'
        star = '\u269D'
        pent = '\u26E4'
        com = '\u262D'
        app = '\u2776'
        
        
        
        
        
            
        print(pent + h * 5 + com + h * 6 + pent + h * 6 + com + h * 5 + pent)
        print('      -~-SHIPS-~-',
              '            -~-SHOTS-~-           ')
        for row_num in range(10):
            for col in player.ships_grid.rows[row_num]:
                print(col, end =' ')
            print(' ', end=' ')
            for col in player.shots_grid.rows[row_num]:
                print(col, end =' ')
            print()

        print(pent + h * 5 + com + h * 6 + pent + h * 6 + com + h * 6 + pent)
        
        
         

    
Controller().play()


##
##for ship in [my_carrier,my_battleship,my_destroyer,my_submarine,my_patrolboat]:
##    print("{} start coord:".format(ship. __class__.__name__)) 
##    (ship.row,ship.col) = ask_coord()
##    print("Direction? [h|v] ")
##    ship.direction = input('> ').lower().strip()
##
##    if ship.direction  == 'h':
##        for col in range(ship.size):
##            grid[ship.row] [ship.col + col] = ship.char
##
##    show_grid()




<<<<<<< HEAD
if ship.direction  == 'h':
    for col in range(ship.size):
        grid[ship.row] [ship.col + col] = ship.char
            
if ship.direction == 'v':
    for row in range(ship.size):
        grid[ship.row] [ship.col + col] = ship.char
=======
    if ship.direction  == 'h':
        for col in range(ship.size):
            grid[ship.row] [ship.col + col] = ship.char
            
    if ship.direction == 'v':
        for row in range(ship.size):
            grid[ship.row] [ship.col + col] = ship.char
>>>>>>> origin/master


