#Hill climbing algorithm

import random

n = 4

# State class
class state:
    def __init__ (self,queens,n):
        self.queens = queens
        self.n = n
        self.matrix = self.matrix_generation()
        
    def matrix_generation(self):                # Generating the state matrix
        matrix = []
        for x in range(0,n):
            matrix.append([0]*n)
        for q in queens:
            matrix[q[0]][q[1]] = 1
        return matrix
                    

def move_queen (q):
    new_queens = []
    for x in range(0,n):
        if x != q[1]:
            new_queens.append((q[0],x))
    return new_queens
    
def conflict_count(queens):
    conflicts = 0
    for q in queens:
        for k in queens:                    # checks every other queen
            if k != q:
                if q[1] == k[1]:            # checks queen's column
                    conflicts += 1
                if abs(q[0]-k[0]) == abs(q[1]-k[1]):
                    conflicts += 1
    return conflicts
                        

#Genariting randomly the initial state      
queens = []
for x in range (0,n):
    xth_queen = (x,random.randint(0,n-1))
    queens.append(xth_queen)

    
initial_state = state(queens,n)                     # Declaring the initial state


# First algorithm

current_state = initial_state

print(queens)

steps = [queens]

while conflict_count(current_state.queens) != 0:
    
    new_states_queens = []
        
    for q in current_state.queens:
        moved_q = move_queen(q)
    
        for i in moved_q:
            state_queens = []
            for p in range(0,n):
                if p != q[0]:
                    state_queens.append(current_state.queens[p])
            state_queens.insert(q[0],i)
            new_states_queens.append(state_queens)
    
    conflicts_number = []
         
    for n_queens in new_states_queens:
        conflicts_number.append(int(conflict_count(n_queens)/2))
    
    steps.append(new_states_queens[conflicts_number.index(min(conflicts_number))])
    current_state.queens = new_states_queens[conflicts_number.index(min(conflicts_number))]

print(len(steps))