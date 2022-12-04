from interface import *

global N
N = 8
import pygame
import time

try:
    l=Game()
    l.start()
except:
    pygame.init()
    Win = pygame.display.set_mode((800, 800))
    queen = pygame.transform.scale(pygame.image.load('quee.png'),(100,100))
def draw(board):
     win = pygame.display.set_mode((800,800))
     win. fill((255, 255, 255))
     A=[]
     for i in range (N):
          for j in range (N):
              if board[j][i]==0:
                  pygame.draw.rect(win, (255,255,255), [i*100,j*100,100,100])
              if board[j][i]==1:
                A.append((i*100,j*100))
                for i in range(len(A)):
                    win.blit(queen,(A[i][0],A[i][1]))
              if board [j][i]==2:
                  pygame.draw. rect (win,(255,0,0), [i*100,j*100,100,100])
                  
     pygame.display.update()

def printSolution (board):
     for i in range (N):
         for j in range (N):
             print (board[i] [j], end=" ")
         print( )
     for i in range (N):
        for j in range(N):
            if board[i][j]==2:
                board[i][j]=0
     draw(board)

def isSafe(board, row,col):
    clock=pygame.time.Clock()
    for i in range (col):
        if board[row] [i]==1:
            for j in range(col):        
                if board[row][j]==2:
                    board[row][j]=0
            return False
        board[row][i]=2
        draw(board)
        #clock.tick(5)
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            for x,y in zip(range(row,-1,-1),range(col,-1,-1)):
                if board[x][y]==2:
                    board[x][y]=0
            return False
        board[i][j]=2
        draw(board)
        #clock.tick(5)
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j]==1:
            for x,y in zip(range(row,-1,-1),range(col,-1,-1)):
                if board[x][y]==2:
                    board[x][y]=0
            return False
        board[i][j]=2
        draw(board)
        #clock.tick(5)
    return True

def solveNQUtil(board,col):
#check

    if col>=N:
        return True
    for i in range(N):
        if isSafe(board ,i ,col):
            board[i][col]=1
            draw(board)
            clock=pygame.time.Clock()
            clock.tick(5)
            if solveNQUtil (board, col+1)==True:
                return True
            board[i][col]=0
            draw(board)
            clock.tick(5)
    return False

def solveNQ(board):
    if solveNQUtil(board,0 )==False:
        print("Solution does not exist")
        return False

    printSolution(board)

def main():
    run = True
    board=[
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
    ]
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            if event. type==pygame. KEYDOWN:
                if event. key==pygame.K_SPACE:
                    solveNQ(board)
        draw(board)
main()


