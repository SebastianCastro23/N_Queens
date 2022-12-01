import numpy as np
import random as rd

N = 4 # N will be the number of queens that also represents the size of the board 
queens = list(np.arange(1,N+1)) # columns of the N queens
attack = []

# checks collisions or conflict between the queens already on the chest board
def conflict_count():
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
def attacked_queens():
    num_queens_attacked = 0
    for q in queens: # q an k represents the columns
        for k in queens:                
            if q != k:
                if q == k or abs(q-k) == abs(queens.index(q)-queens.index(k)):     # checks queen's column and both queen's diagonals at the same time
                    if [queens.index(q),q] not in attack:
                        attack.append([queens.index(q),q]) # row x column
    num_queens_attacked = len(attack)
    return num_queens_attacked

# returns true if the value of collisions is less with the swap propose
def swap_ok():
    swap = False
    return swap
    
# this function actually swap 
def perform_swap():
    return



# given N be the size of the board lets let each row have exactly one queen
def queen_search(queen):
    collisions = conflict_count()                           # number of collitions with the initial arrangement
    number_of_attacks = 0
    
    # initialization 
    while conflict_count() != 0:
        queen = list(np.random.permutation(np.array(queens)))
        collisions = conflict_count()
        limit = 0.45*collisions
        number_of_attacks = attacked_queens()
        loopCount = 0

        #searching ways of arranging the N queens
        while loopCount > 32*N:
            for k in number_of_attacks:
                i = attack[k]
                j = rd.randint(0,4)
                pass
            pass

queens = list(np.random.permutation(np.array(queens)))
print(queens)
print(attacked_queens())
print(conflict_count())