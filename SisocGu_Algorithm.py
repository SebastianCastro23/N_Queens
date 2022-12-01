import numpy as np
import random as rd
import copy

N = 5 # N will be the number of queens that also represents the size of the board 
queens = list(np.arange(1,N+1)) # columns of the N queens
attack = []

# checks collisions or conflict between the queens already on the chest board
def conflict_count(queens):
    conflicts = 0
    for q in queens: # q an k represents the columns
        for k in queens:                                # checks every other queen
            if q != k:
                if q == k:                            # checks queen's column
                    conflicts += 1
                if abs(q-k) == abs(queens.index(q)-queens.index(k)):        # checks both queen's diagonals at the same time
                    conflicts += 1
            
    return int(conflicts/2)

# returns number of queens attacked
def attacked_queens(queens):
    num_queens_attacked = 0
    for q in queens: # q an k represents the columns
        for k in queens:                
            if q != k:
                if q == k or abs(q-k) == abs(queens.index(q)-queens.index(k)):     # checks queen's column and both queen's diagonals at the same time
                    if q not in attack:
                        attack.append(q) # row x column
    num_queens_attacked = len(attack)
    return num_queens_attacked

# returns true if the value of collisions is less with the swap propose
def swap_ok(queen_i,queen_j,queens):
    swap = False
    num_conflicts = conflict_count(queens)
    queens_copy = copy.deepcopy(queens)
    temp = queen_j # Hacemos el swapping de las reinas en las columnas
    index = queens.index(queen_i) 
    queens_copy[queens.index(queen_j)] = queen_i
    queens_copy[index] = temp
    if conflict_count(queens_copy) < num_conflicts:
        swap = True
    return swap
    
# this function actually swap 
def perform_swap(queen_i,queen_j,collisions,queens):
    temp = queen_j # Hacemos el swapping de las reinas en las columnas
    index = queens.index(queen_i) 
    queens[queens.index(queen_j)] = queen_i
    queens[index] = temp
    collisions = conflict_count(queens) # update the number of conflicts 
    return [collisions,queens]



# given N be the size of the board lets let each row have exactly one queen
def queen_search(queen):

    # initialization 
    while conflict_count(queen) != 0:
        queen = list(np.random.permutation(np.array(queen)))
        collisions = conflict_count(queen)
        limit = 0.45*collisions 
        number_of_attacks = attacked_queens(queen)
        loopCount = 0

        #searching ways of arranging the N queens
        while loopCount < 32*N:
            for k in range(0,number_of_attacks):
                i = attack[k]
                j = rd.randint(1,4)
                if swap_ok(i,j,queen):
                    rta = perform_swap(i,j,collisions,queen)
                    collisions = rta[0]
                    queen = rta[1]
                    if collisions == 0:
                        break
                    if collisions < limit:
                        limit = 0.45*collisions 
                        number_of_attacks = attacked_queens(queen)
            loopCount = loopCount + number_of_attacks
        print(queen)

queen_search(queens)