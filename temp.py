import pygame

pygame.init()

# Window
WIDTH = 1200
HEIGHT = 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nine men morris")

# Colors
BACKGROUND = (65, 65, 65)
BUTTON = (100,100,100)
LINE = (30, 30, 30)
X_COLOR = (200, 50, 50)
O_COLOR = (50, 80, 200)

# Board
temp = [[0,"_","_",1,"_", "_",2],
        ["_",8,"_",9,"_",10,"_"],
        ["_","_",16,17,18,"_","_"],
        [7,15,23,"_",19,11,3], 
        ["_","_",22,21,20,"_","_"],
        ["_",14,"_",13,"_",12,"_"],
        [6,"_","_",5,"_","_",4]]


current_player = "X"
game_over = False

font = pygame.font.Font(None, 150)
small_font = pygame.font.Font(None, 50)

clock = pygame.time.Clock()


def draw_board():
    screen.fill(BACKGROUND)

    # Draw grid
    pygame.draw.rect(screen, LINE, (100, 100, 1000, 1000),5)
    pygame.draw.rect(screen, LINE, (250, 250, 700, 700),5)
    pygame.draw.rect(screen, LINE, (400, 400, 400, 400),5)

    pygame.draw.line(screen, LINE, (600,100), (600,400),5)
    pygame.draw.line(screen, LINE, (600,800), (600,1100),5)

    pygame.draw.line(screen, LINE, (100,600), (400,600),5)
    pygame.draw.line(screen, LINE, (800,600), (1100,600),5)
    

    buttons = []

    temp = [[1,0],[0,1], [-1,0],[0,-1],[0,0]]
    temp_r = [500, 350, 200]
    temp_last = [0,0]
    temp_start_r = [60,210,360]

    for ring in range(3):
        temp_last = [temp_start_r[ring], temp_start_r[ring]]
        for t in range(8):
            temp_last = [temp_last[0] + temp[t//2][0]*temp_r[ring],  temp_last[1] + temp[t//2][1]*temp_r[ring]]
            button = pygame.Rect(temp_last[0], temp_last[1], 80,80)
            buttons.append(button)
            pygame.draw.rect(screen, BUTTON, button)

    for button in buttons:
        pygame.draw.rect(screen, BUTTON, button)




running = True
draw_board()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, button in enumerate(buttons):
                if button.collidepoint(event.pos):
                    print("You clicked button", i)

                

    draw_board()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()