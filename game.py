from cmath import sqrt
import time
import src.input_file as input_file
import src.troops as troops
import src.buildings as buildings
from colorama import Back
import json

input_arr = []

# creating base
th = buildings.TownHall(9, 9)

Huts = []

#definining size of grid
rows, cols = (20, 20)

# define spawning position
r1,c1 = (1,1)
r2,c2 = (cols-2,cols-2)
r3,c3 = (1,10)
#defining barbarian object array
barb = []

Huts.append(buildings.hut(1, 15, 7))
Huts.append(buildings.hut(2, 15, 9))
Huts.append(buildings.hut(3, 15, 11))
Huts.append(buildings.hut(4, 15, 13))
Huts.append(buildings.hut(5, 15, 15))

Cannons  = []
Cannons.append(buildings.cannon(1, 11, 7, 6, 50))
Cannons.append(buildings.cannon(2, 11, 13, 6, 50))

walls = []
wall_num=0
for i in range(th.col-4, th.col+7):
    walls.append(buildings.wall(wall_num,th.row-4,i))
    wall_num=wall_num+1
    walls.append(buildings.wall(wall_num,th.row+8,i))
    wall_num=wall_num+1

for i in range(th.row-4, th.row+8):
    walls.append(buildings.wall(wall_num,i,th.col-4))
    wall_num=wall_num+1
    walls.append(buildings.wall(wall_num,i,th.col+7))
    wall_num=wall_num+1

k = troops.king(2, 2, 10,1)
# defining our grid

grid = [['.' for i in range(cols)] for j in range(rows)]

for i in range(th.row, th.row+4):
    for j in range(th.col, th.col+3):
        grid[i][j] = 'T'

for w in walls:
    grid[w.row][w.col] = 'W'

for h in Huts:
    grid[h.row][h.col] = 'H'

for c in Cannons:
    grid[c.row][c.col] = 'C'

grid[k.row][k.col] = 'K'
inp = 'n'



# print grid
getch = input_file.Get()

def king_movement(inp):
    if inp == 'W' and k.row > 0 and grid[k.row-1][k.col] == '.':
        grid[k.row][k.col] = '.'
        shift = 0
        while k.row > 0 and grid[k.row-1][k.col] == '.' and shift < k.speed:
            k.row = k.row-1
            shift = shift +1
        grid[k.row][k.col] = 'K'
    if inp == 'A' and k.col > 0 and grid[k.row][k.col-1] == '.':
        grid[k.row][k.col] = '.'
        shift = 0
        while k.col > 0 and grid[k.row][k.col-1] == '.' and shift < k.speed:
            k.col = k.col-1
            shift = shift +1
        grid[k.row][k.col] = 'K'
    if inp == 'S' and k.row < rows-1 and grid[k.row+1][k.col] == '.':
        grid[k.row][k.col] = '.'
        shift = 0
        while k.row < rows-1 and grid[k.row+1][k.col] == '.' and shift < k.speed:
            k.row = k.row+1
            shift = shift +1
        grid[k.row][k.col] = 'K'
    if inp == 'D' and k.col < cols-1 and grid[k.row][k.col+1] == '.':
        grid[k.row][k.col] = '.'
        shift = 0
        while k.col < cols-1 and grid[k.row][k.col+1] == '.' and shift < k.speed:
            k.col = k.col+1
            shift = shift +1
        grid[k.row][k.col] = 'K'

max_barbarian = 15
def create_barbarian(inp):
    if len(barb) < max_barbarian:
        default_damage = 10
        default_speed = 1
        if inp == '1':
            barb.append(troops.barbarians(r1,c1,default_damage,default_speed))
            grid[r1][c1] = 'B'
        elif inp == '2':
            barb.append(troops.barbarians(r2,c2,default_damage,default_speed))
            grid[r2][c2] = 'B'
        else:
            barb.append(troops.barbarians(r3,c3,default_damage,default_speed))
            grid[r3][c3] = 'B'

def area_of_effect():
    aoe = 5
    is_th = 0
    if k.health > 0:
        for i in range(rows):
            for j in range(cols):
                if ((i-k.row)*(i-k.row)) + ((j-k.col)*(j-k.col)) < (aoe*aoe):
                    if grid[i][j] == 'T' and is_th == 0:
                        th.health = th.health - k.damage
                        is_th = 1
                    for c in Cannons:
                        if i == c.row and j == c.col:
                            c.health = c.health - k.damage
                    for h in Huts:
                        if i ==  h.row and j == h.col:
                            h.health = h.health - k.damage


# storing kings last input for attack
king_last_move = ''

def manipulate_input(king_last_move):
    inp = input_file.input_to(getch)
    input_arr.append(inp)
    if (inp == 'W' or inp == 'A' or inp == 'S' or inp == 'D') and k.health>0:
        king_last_move = inp
        king_movement(inp)

    if (inp == '1' or inp=='2' or inp == '3'):
        create_barbarian(inp)

    if inp == ' ':  # attack
        new_row = k.row
        new_col = k.col
        if king_last_move == 'W':
            new_row = k.row-1
        if king_last_move == 'A':
            new_col = k.col-1
        if king_last_move == 'S':
            new_row = k.row+1
        if king_last_move == 'D':
            new_col = k.col+1
        if new_col >= 0 and new_col < cols and new_row >= 0 and new_row < rows and k.health>0:
            if grid[new_row][new_col] == 'T':
                th.health = th.health - k.damage
            for c in Cannons:
                if new_row == c.row and new_col == c.col:
                    c.health = c.health - k.damage
            for h in Huts:
                if new_row ==  h.row and new_col == h.col:
                    h.health = h.health - k.damage
            for w in walls:
                if new_row == w.row and new_col == w.col:
                    w.health = w.health - k.damage

    if inp == 'R': # Rage spell
        if k.health>0:
            k.rage_spell()
        for b in barb:
            if b.health>0:
                b.rage_spell()
    if inp == 'H': # Heal spell
        k.heal_spell()
        for b in barb:
            if b.health>0:
                b.heal_spell()
    if inp == 'N':
        for w in walls:
            grid[w.row][w.col] = '.'
    if inp == 'P':
        area_of_effect()  

    if inp == 'E':
        exit()
    return king_last_move


def print_grid(i, j):
    h = buildings.structure_max_health

    if grid[i][j] == 'K':
        if k.health>0:
            print(Back.CYAN+grid[i][j], end=" ")
        else:
            print(Back.RED+grid[i][j], end=" ")
    elif grid[i][j] == '.':
        print(Back.BLACK+grid[i][j], end=" ")
    else:
        is_a = 0
        if grid[i][j] == 'T':
            h = th.health
        if grid[i][j] == 'C':
            for c in Cannons:
                if i==c.row and j==c.col:
                    h = c.health
                    if c.is_attack == 1:
                        is_a = 1
        if grid[i][j] == 'H':
            for c_h in Huts:
                if i==c_h.row and j==c_h.col:
                    h = c_h.health
        if grid[i][j] == 'W':
            for w in walls:
                if i==w.row and j==w.col:
                    h=w.health
        if grid[i][j] == 'B':
            for b in barb:
                if b.row == i and b.col == j:
                    h = b.health
        if grid[i][j] == 'C' and is_a == 1:
            print(Back.WHITE+grid[i][j],end=" ")
        elif h > (buildings.structure_max_health/2):
            print(Back.GREEN+grid[i][j],end=" ")
        elif h<=(buildings.structure_max_health/2) and h>(buildings.structure_max_health/4):
            print(Back.YELLOW+grid[i][j],end=" ")
        elif h>0 and h<=(buildings.structure_max_health/4):
            print(Back.RED+grid[i][j],end=" ")
        else:
            grid[i][j] = '.'
            print(Back.BLACK+grid[i][j], end=" ")

def defense():
    for c in Cannons:
        c.is_attack = 0
    for i in range(rows):
        for j in range(cols):
            for c in Cannons:
                if (((c.row - i)*(c.row - i)) + ((c.col - j)*(c.col-j))) < (c.c_range*c.c_range) and c.health>0:
                    if grid[i][j] == 'K':
                        k.health = k.health - c.damage
                        c.is_attack = 1
                    if grid[i][j] == 'B':
                        for b in barb:
                            if b.col == j and b.row == i:
                                b.health = b.health - c.damage
                                c.is_attack = 1
                                break


def print_health():
    total_bars = 10
    current_bars = round((float(k.health)/float(troops.max_king_health))*total_bars)
    print("King Health : ",end="")
    if current_bars>(total_bars/2):
        for bar in range(current_bars):
            print(Back.GREEN+"|", end=" ")
    elif current_bars>(total_bars/4):
        for bar in range(current_bars):
            print(Back.YELLOW+"|", end=" ")
    else:
        for bar in range(current_bars):
            print(Back.RED+"|", end=" ")


is_move_barb=0
def barbarian_move(is_move_barb):
    if is_move_barb%5 == 0:
        for b in barb:
            target_i=0
            target_j=0
            if b.health>0:
                min_dist = 1000
                for i in range(rows):
                    for j in range(cols):
                        if grid[i][j] == 'C' or grid[i][j] == 'H' or grid[i][j] == 'T':
                            if min_dist > abs(i-b.row) + abs(j-b.col):
                                min_dist = abs(i-b.row) + abs(j-b.col)
                                target_i = i
                                target_j = j
                
                new_row = b.row
                new_col = b.col
                if target_j!=b.col:
                    if target_j>b.col:
                        shift = 0
                        while new_col < cols-1 and (grid[b.row][new_col] == '.' or grid[b.row][new_col] == 'B') and shift < b.speed:
                            new_col= new_col+1
                            shift = shift +1
                    else:
                        shift = 0
                        while new_col > 0 and (grid[b.row][new_col] == '.' or grid[b.row][new_col] == 'B') and shift < b.speed:
                            new_col = new_col-1
                            shift = shift +1
                
                elif target_i!=b.row:
                    if target_i>b.row:
                        shift = 0
                        while new_row < rows-1 and (grid[new_row][b.col] == '.' or grid[new_row][b.col] == 'B') and shift < b.speed:
                            new_row = new_row+1
                            shift = shift +1
                    else:
                        shift = 0
                        while new_row > 0 and (grid[new_row][b.col] == '.' or grid[new_row][b.col] == 'B') and shift < b.speed:
                            new_row = new_row-1
                            shift = shift +1
                
                if grid[new_row][new_col] == '.' or grid[new_row][new_col] == 'B':
                    grid[b.row][b.col] = '.'
                    b.row = new_row
                    b.col = new_col
                    grid[b.row][b.col] = 'B'

                else:
                    if grid[new_row][new_col] == 'T':
                        th.health = th.health - b.damage
                    for c in Cannons:
                        if new_row == c.row and new_col == c.col:
                            c.health = c.health - b.damage
                    for h in Huts:
                        if new_row ==  h.row and new_col == h.col:
                            h.health = h.health - b.damage
                    for w in walls:
                        if new_row == w.row and new_col == w.col:
                            w.health = w.health - b.damage
    
    is_move_barb=is_move_barb+1
    return is_move_barb

            
def is_game_end():
    bldg = 0
    troops = 0
    all_barbs = 1
    if len(barb) < max_barbarian:
        all_barbs =0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] =='T' or grid[i][j]=='C' or grid[i][j] == 'H':
                bldg = 1
            if grid[i][j] == 'B' or (grid[i][j] == 'K' and k.health >0):
                troops = 1
    if troops == 0 and all_barbs == 1:
        return -1
    elif bldg == 0:
        return 1
    else :
        return 0

    
    


                            

        
print("\tWELCOME TO MY GAME !")
print("")
print("Instructions:")
print("1. W,A,S,D (capital only) to move King ")
print("2. R for Rage spell")
print("2. H for Heal spell")
print("3. Press P for King AOE")
print("4. Press 1 to Spawn at ("+str(r1)+","+str(c1)+")")
print("5. Press 2 to Spawn at ("+str(r2)+","+str(c2)+")")
print("6. Press 3 to Spawn at ("+str(r3)+","+str(c3)+")")
print("7. Press N for Noob Wall spell")
print("8. Press E to end game")
print("")
print("\t\tALL THE BEST !")
print("")
print("\t\tPRESS S TO START")
start = input()

e = 0
if(start == 'S' or start == 's'):
    while True:

        king_last_move = manipulate_input(king_last_move)
        defense()
        is_move_barb = barbarian_move(is_move_barb)
        e = is_game_end()
        if (e == 1 or e==-1):
            break
        for i in range(rows):
            for j in range(cols):
                print_grid(i,j)
                if i==2 and j==cols-1:
                    print("",end="     ")
                    print_health()
            print("")
        print("")

else:
    print("Pressed Incorrect Key.....exiting")
    exit()

if (e==1):
    print("\t\t VICTORY TO THE TROOPS")
else :
    print("\t\tDEFEAT TO THE TROOPS")

# input file name
save = input('Save file name: ')


# store input array in a json file in a folder
with open('replays/'+save + '.json', 'w') as outfile:
    json.dump(input_arr, outfile)

