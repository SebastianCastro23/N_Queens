from sprites import *
from View import *
import csv
import sys
import time

font_name = pg.font.match_font('arial')
def draw_text(surface, text, size, x, y, color):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)


N_TILES = 5
csv_name = ''
maze = ""

class Button:
    def __init__(self, game, text, x, y, color, size, t_size):
        self.game = game
        self.image = pg.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.image.fill(color)
        self.text = text
        self.t_size = t_size
        self.color = color

    def show_text(self):
        draw_text(self.game.screen, self.text, self.t_size, self.rect.centerx, self.rect.centery, WHITE)

    def show(self):
        self.game.screen.fill(self.color, self.rect)

class Game:
    def __init__(self):
        # Inicializacion de pygame
        pg.init()
        pg.mixer.init()

        # Inicializacion de ventana
        self.screen = pg.display.set_mode(SCREEN_SIZE, pg.RESIZABLE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.buttons = []

    def start(self):
        self.show_start_screen()
        self.show_go_screen()
        self.load_data()
        while self.running:
            self.new()
            self.run()

    def load_data(self):
        self.map_data = list()
        with open(os.path.join(os.path.dirname(__file__) + '/mazes', csv_name), 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    self.map_data.append(row)

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.steps = pg.sprite.Group()

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == 'c' and row == 0:
                    self.player = Player(self, int((SCREEN_WIDTH/TILESIZE - N_TILES) / 2) + col, int((SCREEN_HEIGHT/TILESIZE - N_TILES) / 2), TILESIZE)
                    self.all_sprites.add(self.player)
                if tile == 'w':
                    wall = Wall(self, int((SCREEN_WIDTH/TILESIZE - N_TILES) / 2) + col, int((SCREEN_HEIGHT/TILESIZE - N_TILES) / 2) + row, TILESIZE, LIGHTGREY)
                    self.all_sprites.add(wall)
                    self.walls.add(wall)

    def run(self):
        # Bucle del juego
        self.playing = True
        self.searching = True
        self.solved = False
        self.search_coor = []
        self.end = (self.map_data[N_TILES-1].index("c"), N_TILES-1)

        button1 = Button(self, "BACK", SCREEN_WIDTH*0.92, SCREEN_HEIGHT*0.9, RED, (100, 50), 25)
        self.buttons.append(button1)

        depth_iter = -2
        dif = 3
        if N_TILES == 50:
            dif = 16
        elif N_TILES == 100:
            dif = 26
        elif N_TILES == 400:
            dif = 40

        if self.mode != 'iter':
            self.load_solution(self.mode)
            self.solved = True

        while self.playing:
            self.clock.tick(FPS)
            self.events()                
            self.update()
            self.draw()

            if self.search_coor:
                self.draw_search()
                if N_TILES < 50:
                    time.sleep(0.06)
                elif N_TILES == 50:
                    time.sleep(0.03)

            elif self.mode == 'iter' and not self.solved:
                for step in self.steps:
                    step.kill()
                depth_iter += dif
                self.load_solution(self.mode, depth_iter)
                if self.search_coor[-1] == self.end:
                    self.solved = True

            elif self.solved == True:
                if self.instructions:
                    self.draw_solution()
                    if N_TILES < 50:
                        time.sleep(0.06)
                    elif N_TILES == 50:
                        time.sleep(0.03)
            
            

    def quit(self):
        # Saliendo del juego
        pg.quit()

    def update(self):
        # Actualizando todos los sprites
        self.all_sprites.update()

    def draw_grid(self):
        # Lineas verticales
        for i in range(int(TILESIZE*(SCREEN_WIDTH/TILESIZE - N_TILES) / 2),  int(SCREEN_WIDTH-TILESIZE*(SCREEN_WIDTH/TILESIZE - N_TILES) / 2 + 1), TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (i, TILESIZE*(SCREEN_HEIGHT/TILESIZE - N_TILES) / 2), (i, SCREEN_HEIGHT-TILESIZE*(SCREEN_HEIGHT/TILESIZE - N_TILES) / 2))
        # Lineas horizontales
        for j in range(int(TILESIZE*(SCREEN_HEIGHT/TILESIZE - N_TILES) / 2), int(SCREEN_HEIGHT - TILESIZE*(SCREEN_HEIGHT/TILESIZE - N_TILES) / 2 + 1), TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (TILESIZE*(SCREEN_WIDTH/TILESIZE - N_TILES) / 2, j), (SCREEN_WIDTH-TILESIZE*(SCREEN_WIDTH/TILESIZE - N_TILES) / 2, j))


    def drawing(self):
        # Dando color a la pantalla y dibujando todos los sprites
        self.screen.fill(GREY)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_buttons()
        draw_text(self.screen, maze, 50, SCREEN_WIDTH / 2, 80, WHITE)
        # Actualizamos los cambios
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1,dy=0)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1,dy=0)
                if event.key == pg.K_UP:
                    self.player.move(dx=0,dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dx=0,dy=1)
            
            if event.type == pg.MOUSEBUTTONDOWN:
                mpos = pg.mouse.get_pos()
                if self.buttons[0].rect.collidepoint(mpos):
                    self.all_sprites.remove()
                    self.buttons = []
                    self.start()

    def draw_buttons(self):
        for button in self.buttons:
            button.show()
            button.show_text()

    def show_start_screen(self):
        global TILESIZE, csv_name, maze, N_TILES
        self.showing_menu = True
        button1 = Button(self, "Bactracking", SCREEN_WIDTH / 2, SCREEN_HEIGHT*0.45, BLUE, (400, 60), 25)
        self.buttons.append(button1)
        button2 = Button(self, "Hill climbing", SCREEN_WIDTH / 2, SCREEN_HEIGHT*0.55, BLUE, (400, 60), 25)
        self.buttons.append(button2)
        button3 = Button(self, "Algorithm Sosic JungGu", SCREEN_WIDTH / 2, SCREEN_HEIGHT*0.65, BLUE, (400, 60), 25)
        self.buttons.append(button3)
  
        button6 = Button(self, "EXIT", SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.95, RED, (100, 50), 25)
        self.buttons.append(button6)
        while self.showing_menu:
            self.clock.tick(FPS)
            self.screen.fill(BLACK)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mpos = pg.mouse.get_pos()
                    if button1.rect.collidepoint(mpos):
                        N_TILES = 5
                        TILESIZE = 100
                        csv_name = 'Backtracking'
                        self.showing_menu = False

                    elif button2.rect.collidepoint(mpos):
                        TILESIZE = 50
                        N_TILES = 10
                        csv_name = 'Hill climbing'
                        v = 0.08
                        self.showing_menu = False

                    elif button3.rect.collidepoint(mpos):
                        TILESIZE = 10
                        N_TILES = 50
                        csv_name = 'Algorithm Sosic JungGu'
                        v = 0.05
                        pg.quit()
                        sys.exit()

                    
                    elif button6.rect.collidepoint(mpos):
                        self.showing_menu = False
                        pg.quit()
                        sys.exit()


            self.draw_buttons()
            draw_text(self.screen, "N-Queens Problem", 100, SCREEN_WIDTH / 2, 120, YELLOW)
            draw_text(self.screen, "Select Algorithn", 50, SCREEN_WIDTH / 2, 300, WHITE)

            pg.display.flip()
        self.buttons = []


    def draw_solution(self):        
        c = YELLOW
        if len(self.instructions) == 1:
            c = RED
        # Agregar un nuevo bloque a all_sprites
        sol = self.instructions.pop(0)
        
        if sol == 'D':
            wall = Wall(self, self.xnow, self.ynow + 1, TILESIZE, c)
            self.all_sprites.add(wall)
            self.walls.add(wall)
            self.ynow += 1
        
        if sol == 'U':
            wall = Wall(self, self.xnow, self.ynow - 1, TILESIZE, c)
            self.all_sprites.add(wall)
            self.walls.add(wall)
            self.ynow -= 1
        
        if sol == 'R':
            wall = Wall(self, self.xnow + 1, self.ynow, TILESIZE, c)
            self.all_sprites.add(wall)
            self.walls.add(wall)
            self.xnow += 1
        
        if sol == 'L':
            wall = Wall(self, self.xnow - 1, self.ynow, TILESIZE, c)
            self.all_sprites.add(wall)
            self.walls.add(wall)
            self.xnow -= 1

    def show_go_screen(self):
        global TILESIZE, csv_name, maze, N_TILES
        self.showing_menu = True
        if csv_name == 'Backtracking':
            button1 = Button(self, "Standard", SCREEN_WIDTH / 2, SCREEN_HEIGHT*0.43, BLUE, (400, 60), 25)
            self.buttons.append(button1)
            button2 = Button(self, "Variant Branch/Bound", SCREEN_WIDTH / 2, SCREEN_HEIGHT*0.53, BLUE, (400, 60), 25)
            self.buttons.append(button2)
        if csv_name == 'Hill climbing':
            button3 = Button(self, "Standard", SCREEN_WIDTH / 2, SCREEN_HEIGHT*0.43, BLUE, (400, 60), 25)
            self.buttons.append(button3)
            button4 = Button(self, "Variant #1", SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.53, BLUE, (400, 60), 25)
            self.buttons.append(button4)
            button5 = Button(self, "Variant #2", SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.63, BLUE, (400, 60), 25)
            self.buttons.append(button5)
        while self.showing_menu:
            self.clock.tick(FPS)
            self.screen.fill(BLACK)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    main()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mpos = pg.mouse.get_pos()
                    self.mode = 'Standard'
                    self.showing_menu = False

                    if button2.rect.collidepoint(mpos):
                        self.mode = 'bfs'
                        self.showing_menu = False

                    elif button3.rect.collidepoint(mpos):
                        self.mode = 'iter'
                        self.showing_menu = False

                    elif button4.rect.collidepoint(mpos):
                        self.mode = 'ucs'
                        self.showing_menu = False

                    elif button5.rect.collidepoint(mpos):
                        self.mode = 'greedy'
                        self.showing_menu = False
                    
    


            self.draw_buttons()
            draw_text(self.screen, "N-Queens Problem", 100, SCREEN_WIDTH / 2, 120, YELLOW)
            draw_text(self.screen, "Select Algorithm", 50, SCREEN_WIDTH / 2, 300, WHITE)

            pg.display.flip()
        self.buttons = []