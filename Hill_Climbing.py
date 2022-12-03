#Hill climbing algorithm

import random
import copy
import globals as gl

# State class
class state:
    def __init__ (self,queens,n):
        self.queens = queens
        self.n = n
        self.matrix = self.matrix_generation()      # Calls the function that generates the matrix
        self.columns = self.columns()               # Calls the functions that keep track of the amount of 
        self.diagonals = self.diagonals()           # queens in each column and diagonal
        
    def matrix_generation(self):                    # Generating the state matrix
        matrix = []
        for x in range(0,n):
            matrix.append([0]*n)
        for q in queens:
            matrix[q[0]][q[1]] = 1
        return matrix
    
    def columns(self):                          # Function that stores the amount of queens in each column
        columns = [0]*n
        for q in queens:
            columns[q[1]] += 1
        return columns
            
    def diagonals(self):                                        # Function that stores the amount of queens in each diagonal
        diagonals = []                                          # diagonals[0] --> down diagonals
        diagonals.append([0]*(n+1))                             # diagonals[1] --> up diagonals
        diagonals.append([0]*(n+1))
        for q in queens:
            if (q[0]-q[1])+2 <= n:
                diagonals[0][(q[0]-q[1])+2] += 1                # adds one to the down diagonal
            if (((q[0]+q[1])-1) >= 0) and (((q[0]+q[1])-1)<=n):
                diagonals[1][(q[0]+q[1])-1] += 1                # adds one to the up diagonal
            
        return diagonals                
                                
                    

def move_queen (q):                             # this function returns all the posible column positions where we can move a queen
    new_queens = []
    for x in range(0,n):
        if x != q[1]:
            new_queens.append((q[0],x))
    return new_queens

# Conflict count first version
def conflict_count_1st(queens):
    conflicts = 0
    for q in queens:
        for k in queens:                                    # checks every other queen
            if k != q:
                if q[1] == k[1]:                            # checks queen's column
                    conflicts += 1
                if abs(q[0]-k[0]) == abs(q[1]-k[1]):        # checks both queen's diagonals at the same time
                    conflicts += 1
    return conflicts


# Conflict count second version

def conflict_count_2nd(state):
    conflicts = 0;
    for q in state.queens:
        if state.columns[q[1]] > 1:                                     # checks the amount of queens in q's column
            conflicts += (state.columns[q[1]]-1)
        if ((q[0]-q[1])+2) <= n:                                        
            if state.diagonals[0][(q[0]-q[1])+2] > 1:                   # checks the amount of queens in q's down diagonal
                conflicts += (state.diagonals[0][(q[0]-q[1])+2]-1)
        if (((q[0]+q[1])-1) >= 0) and (((q[0]+q[1])-1)<=n):
            if state.diagonals[1][(q[0]+q[1])-1] > 1:                   # cheks the amount of queens in q's up diagonal
                conflicts += (state.diagonals[1][(q[0]+q[1])-1]-1)
    return conflicts

# Function that helps us find all the indices where a certain element is stored at on a list
def find_indices(list_to_check, item_to_find):
    return [idx for idx, value in enumerate(list_to_check) if value == item_to_find]

#First version

@gl.mide_tiempo
def first_version(initial_state, steps):
    current_state = initial_state
    while conflict_count_1st(current_state.queens) != 0:                        # it keeps running while the number of conflicts is different than 0
    
        new_states_queens = []                                                  # here we store all the posible new state queen's configurations
        conflicts = int(conflict_count_1st(current_state.queens)/2)
        for q in current_state.queens:                                          # we do this for each one of the n queens
            moved_q = move_queen(q)                                             # call the move_queen function
            state_queens = copy.deepcopy(current_state.queens)  
            state_queens.remove(q)                                              # Removes q's original position

            for i in moved_q:                                                   # for every queen's possible new position we create a new configuration
                state_queens.insert(q[0],i)
                new_states_queens.append(copy.deepcopy(state_queens))           # we store the n queens positions
                state_queens.remove(i)
    
        conflicts_number = []
         
        for n_queens in new_states_queens:                                      # for each queens configuration we calculate the number
            conflicts_number.append(int(conflict_count_1st(n_queens)/2))        # of conflicts and we store them in a list
        
        indexes_min = find_indices(conflicts_number, min(conflicts_number))
        random_index = random.randint(0,len(indexes_min)-1)
        index = indexes_min[random_index]                                       # we select the index randomly for not always select the same configuration
        steps.append(new_states_queens[index])
        current_state.queens = copy.deepcopy(new_states_queens[index])          # we change the queens position of the current state 
                                                                                # to the one that causes the less conflicts 
    return len(steps)
                                                                                                
# Second Version

@gl.mide_tiempo
def second_version(initial_state, steps):
    current_state = initial_state
    while conflict_count_2nd(current_state) != 0:                           # it keeps running while the number of conflicts is different than 0
    
        new_states_queens = []                                              # here we store all the posible new state queen's configurations
        
        for q in current_state.queens:                                      # we do this for each one of the n queens
            moved_q = move_queen(q)                                         # call the move_queen function
    
            for i in moved_q:                                               # for every queen's possible new position we create a configuration
                state_queens = []
                for p in range(0,n):
                    if p != q[0]:
                        state_queens.append(current_state.queens[p])
                state_queens.insert(q[0],i)
                new_states_queens.append(state_queens)                      # we store the n queens position
    
        conflicts_number = []
         
        for n_queens in new_states_queens:                                  # we calculate and store the number of conflicts for every
            new_state = state(n_queens,n)                                   # different configuration with the improved version of conflict counting
            n_conflicts = copy.deepcopy(conflict_count_2nd(new_state))                                                      
            conflicts_number.append(n_conflicts/2)                            
    
        steps.append(new_states_queens[conflicts_number.index(min(conflicts_number))])
        current_state.queens = new_states_queens[conflicts_number.index(min(conflicts_number))]     # we change the queens position of the current state
                                                                                                    # to the one that causes the less conflict
    return len(steps)

# Third version

@gl.mide_tiempo
def third_version(initial_state, steps):
    current_state = initial_state
    while conflict_count_2nd(current_state) != 0:                                           # it keeps running while the number of conflicts is different than 0
    
        flag = False                                                                        # flag that indicates if it has found a lower conflicts state
        equal_states = []
        
        for q in current_state.queens:                                                      # we do this for each one of the n queens
            if flag:
                break
            moved_q = move_queen(q)                                                         # call the move_queen function
            state_queens = copy.deepcopy(current_state.queens)
            state_queens.remove(q)                                                          # removing q's original position
    
            for i in moved_q:                                                               # for every queen's possible new position we create a new configuration
                state_queens.insert(q[0],i)
                new_state = state(state_queens,n)
                n_conflicts = copy.deepcopy(conflict_count_2nd(new_state))                  # counts the conflicts for that configuration
                if n_conflicts < conflict_count_2nd(current_state):                         # if it's lower than the current conflicts number
                    steps.append(state_queens) 
                    current_state.queens = copy.deepcopy(state_queens)                      # it becomes the new current state's configuration                     
                    flag = True  
                    break
                if n_conflicts == conflict_count_2nd(current_state):                        # if it's equal to the current conflicts number
                    equal_states.append(copy.deepcopy(state_queens))                        # it saves this configuration in a list
                state_queens.remove(i)
            
        if not flag:                                                                        # if a lower conflicts configuration was not found
            random_index = random.randint(0,len(equal_states)-1)                
            steps.append(equal_states[random_index])        
            current_state.queens = copy.deepcopy(equal_states[random_index])                # it sets a random configuration selected from the equal conflicts number configuration         
              
    return(len(steps))   

n = 60
    
#Genariting randomly the initial state      
queens = []
for x in range (0,n):
    xth_queen = (x,random.randint(0,n-1))
    queens.append(xth_queen)

    
initial_state = state(queens,n)                     # Declaring the initial state
steps = [queens]

print(first_version(initial_state, steps))          # calls the algorithm               