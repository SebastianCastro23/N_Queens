#Hill climbing algorithm

import random

n = 4

# State class
class state:
    def __init__ (self,queens,n):
        self.queens = queens
        self.n = n
        self.matrix = self.matrix_generation()
        self.conflicts = 0                                           # Conflict's number always start at 0
        self.conflict_count()
        self.conflicts = int(self.conflicts/2)                       # The real number of conflicts because every conflict is counted twice
        
    def matrix_generation(self):                # Generating the state matrix
        matrix = []
        for x in range(0,n):
            matrix.append([0]*n)
        for q in queens:
            matrix[q[0]][q[1]] = 1
        return matrix
    
    def conflict_count(self):
        for q in queens:
            for x in range(0,n):                                                # checks only the rows that are different from the queen's row
                if x!= q[0]:
                    if self.matrix[x][q[1]] == 1:                               # checks the queen's column
                        self.conflicts+=1
                    topleft_diag_index = q[1]-(q[0]-x)                          # top-left diagonal index in row x
                    bottomleft_diag_index = q[1]+(q[0]-x)                       # bottom-left diagonal index in row x
                    if topleft_diag_index >= 0 and topleft_diag_index<n:
                        if self.matrix[x][topleft_diag_index] == 1:             # checks the top-left diagonal
                            self.conflicts+=1
                    if bottomleft_diag_index >= 0 and bottomleft_diag_index < n:
                        if self.matrix[x][bottomleft_diag_index] == 1:          # checks the bottom-left diagonal
                            self.conflicts+=1
                    

def subsequential_states(c_state, n):
    subsequential_states = []
    
    for x in range(0,n):
        current_column = c_state.queens[x][1]
        new_q1 = (x,(current_column+1)%n)
        new_q2 = (x,(current_column+2)%n)
        new_q3 = (x,(current_column+3)%n)

        news1_queens = [0]*n
        news2_queens = [0]*n
        news3_queens = [0]*n
        
        for y in range(0,n):
            if y == x:
                news1_queens[y] = new_q1
                news2_queens[y] = new_q2
                news3_queens[y] = new_q3
            else:
                news1_queens[y] = c_state.queens[y]
                news2_queens[y] = c_state.queens[y]
                news3_queens[y] = c_state.queens[y]
        
        
        new_s1 = state(news1_queens, n)
        new_s2 = state(news2_queens, n)
        new_s3 = state(news3_queens, n)
        
        subsequential_states.append(new_s1)
        subsequential_states.append(new_s2)
        subsequential_states.append(new_s3)
    
    return subsequential_states
    

#Genariting randomly the initial state      
queens = []
for x in range (0,n):
    xth_queen = (x,random.randint(0,n-1))
    queens.append(xth_queen)

    
initial_state = state(queens,n)                     # Declaring the initial state


# First algorithm

current_state = initial_state

j = 0

while j <= 1:
        
    subsequential = subsequential_states(current_state, n)
    conflict_values = []
    
    for s in subsequential:
        conflict_values.append(s.conflicts)
    
    current_state = subsequential[conflict_values.index(min(conflict_values))]
    
    j += 1

