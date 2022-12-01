import numpy as np
import random as rd
import globals as gl
from memory_profiler import profile
import copy

N = 50 # N will be the number of queens that also represents the size of the board 
queens = list(np.arange(1,N+1)) # arrange with the columns of the N queens, the index represents the row in wich each queen is 
attack = [] # columns of the queens that will be attacked

# checks collisions or conflict between the queens already on the chest board
# returns the number of conflicts generated by the configuration pass as an argument
def conflict_count(queens):
    conflicts = 0
    for q in queens: # q an k represents the columns
        for k in queens:                              # checks every other queen
            if q != k:
                if q == k:                            # checks queen's column
                    conflicts += 1
                if abs(q-k) == abs(queens.index(q)-queens.index(k)):        # checks both queen's diagonals at the same time
                    conflicts += 1
            
    return int(conflicts/2)

# returns number of queens attacked and modify the attack arrange, inserting the queens that are being attacked 
def attacked_queens(queens):
    num_queens_attacked = 0
    for q in queens: # q an k represents the columns
        for k in queens:                
            if q != k:
                if q == k or abs(q-k) == abs(queens.index(q)-queens.index(k)):    # checks queen's column and both queen's diagonals at the same time
                    if q not in attack:
                        attack.append(q) # row x column
    num_queens_attacked = len(attack)
    return num_queens_attacked

# returns true if the value of collisions is less with the swap of queen_i and queen_j, each swap is a column swap
def swap_ok(queen_i,queen_j,queens):
    swap = False
    num_conflicts = conflict_count(queens)
    queens_copy = copy.deepcopy(queens)
    temp = queen_j                              # queen position swap in que queen array copy 
    index = queens.index(queen_i) 
    queens_copy[queens.index(queen_j)] = queen_i
    queens_copy[index] = temp
    if conflict_count(queens_copy) < num_conflicts:
        swap = True
    return swap
    
# this function actually swap the two queens positions, update the collision variable and also the queens array
def perform_swap(queen_i,queen_j,collisions,queens):
    temp = queen_j                               # queen position swap
    index = queens.index(queen_i) 
    queens[queens.index(queen_j)] = queen_i
    queens[index] = temp
    collisions = conflict_count(queens)         # update the number of conflicts 
    return [collisions,queens]



@gl.mide_tiempo
#@profile
# given N be the size of the board lets let each row have exactly one queen
def queen_search(queen):

    # initialization 
    while conflict_count(queen) != 0:
        queen = list(np.random.permutation(np.array(queen)))    # generate a random permunation of queen[1] to queen[n]
        collisions = conflict_count(queen)
        limit = 0.45*collisions                     #  variable limit is initialized to a certain percentage of the number of collisions, this adjustmente reduced computing cost and increased algorithm efficiency
        number_of_attacks = attacked_queens(queen)
        loopCount = 0

        #searching ways of arranging the N queens
        while loopCount < 32*N:      # bound the iterations, it doesn't affect at all the solution for large n
            for k in range(0,number_of_attacks):
                i = attack[k]           # idea: find a arrangement so this queen has no conflict
                j = rd.randint(1,N)     # use a random queen for exchange
                if swap_ok(i,j,queen):          
                    rta = perform_swap(i,j,collisions,queen) # update the queens array in case the swap is perform
                    collisions = rta[0]
                    queen = rta[1]
                    if collisions == 0:     # END!
                        break
                    if collisions < limit:      # update the variables that change with the swap
                        limit = 0.45*collisions 
                        number_of_attacks = attacked_queens(queen)
            loopCount = loopCount + number_of_attacks 

queen_search(queens)