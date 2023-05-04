import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    
    def draw_snake(self):
        for block in self.body:
            #creating snake
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen,pygame.Color("red"), block_rect)
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False 
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
        
    def add_block(self):
        self.new_block = True


class FRUIT:
    def __init__(self):
        self.randomize()
    
    def draw_fruit(self):
        #create fruit
        fruit_rect = pygame.Rect((int(self.pos.x * cell_size), int(self.pos.y * cell_size) ,cell_size, cell_size))
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0 ,cell_num- 1)
        self.y = random.randint(0 ,cell_num- 1)
        self.pos = Vector2(self.x,self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collison()
        self.check_fail()
    
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    
    def check_collison(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    
    #Loss conditions
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_num or not 0 <= self.snake.body[0].y < cell_num:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()
    
    def draw_grass(self):
        grass_color = (0, 71, 171)
        for row in range(cell_num):
            if row % 2 == 0:
                for col in range(cell_num):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_num):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True, pygame.Color("white"))
        score_x = int(cell_size * cell_num - 60)
        score_y = int(cell_size * cell_num - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface, score_rect)

#initliazing pygame
pygame.init()
cell_size = 40
cell_num = 20
screen = pygame.display.set_mode((cell_num * cell_size, cell_num * cell_size))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
test_surface.fill(pygame.Color("green"))
test_rect = test_surface.get_rect(center = (200,250))
game_font = pygame.font.Font(None, 25)



SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()
    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)

            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,1)
            
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(1,0)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)

    screen.fill(pygame.Color("blue"))
    main_game.draw_elements()


    #creating the elements
    pygame.display.update()

    #Making FPS
    clock.tick(60)
