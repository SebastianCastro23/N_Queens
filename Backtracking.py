
def is_valid(row, col, queens):
    for r in range(row):
        #Valida columnas
        if col == queens[r]:
            return False
        #Validar diagonales
        elif abs(col - queens[r]) == abs(row - r):
            return False
        #No hay riesgo de ataque
    return True


#Verifica (recursivamente) si la reina n se puede ubicar en alguna posición
def place_queen(row, queens, n): 
    #si la última fila de la matriz guardada coincide con
    #el tamaño del tablero se ha encontrado una solución
    if row == n:
        #print(queens)
        return 1
    else:
        total_solns = 0
        
        for col in range(n):
            #is_valid: no ataca ninguna reina
            if is_valid(row, col, queens):
                queens[row] = col
                total_solns += place_queen(row+1, queens, n)
        return total_solns
def n_queens(n):
    queens = [' ']*n
    row = 0
    return place_queen(row, queens, n) 

n_queens(5)