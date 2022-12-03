from interface import *
from View import *
g=Game()
g.start
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