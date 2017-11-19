import pygame
import random
import math

#initialize the program
pygame.init()

display_width = 950
display_height = 600

white = (255,255,255)
grey = (200,200,200)
black = (50,50,50)

gameDisplay = pygame.display.set_mode((display_width, display_height))

bgImg = pygame.image.load('background.png')
bgImg_scaled = pygame.transform.scale(bgImg, (800, 600))

mmImg = pygame.image.load('main_menu.png')
mmImg_scaled = pygame.transform.scale(bgImg, (950, 600))

manImg = pygame.image.load('instructions.png')
manImg_scaled = pygame.transform.scale(bgImg, (950, 600))

planeImg = pygame.image.load('plane.png')

pygame.display.set_caption('YOU MUST TRAIN!')

font = pygame.font.SysFont("calibri.ttf", 30)

plane_x = random.randrange(10,785)
plane_y = random.randrange(5,600)

clock = pygame.time.Clock()
def main_menu(x,y):
    gameDisplay.blit(mmImg_scaled, (x,y))

def instructions(x,y):
    gameDisplay.blit(manImg_scaled, (x,y))

def new_bg():
    bgx = random.choice([True, False])
    bgy = random.choice([True, False])

    global bgImg_scaled

    bgImg_scaled = pygame.transform.flip(bgImg_scaled, bgx, bgy)
    
def bg(x,y):
    gameDisplay.blit(bgImg_scaled, (x,y))

def plane(x,y):
    gameDisplay.blit(planeImg, (x,y))

def new_level():
    new_bg()

    global plane_x, plane_y

    plane_x = random.randrange(10,785)
    plane_y = random.randrange(5,600)

def time(sec, mints):
    font = pygame.font.SysFont("calibri.ttf", 30)
    displaytext = "%s:%s" % (mints, sec)
    text = font.render("Time : " +str(displaytext), True, black)
    gameDisplay.blit(text, (820,80))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def scoreboard(x,y,w,h,color):
    pygame.draw.rect(gameDisplay, color, [x,y,w,h])

def score(count):
    font = pygame.font.SysFont("calibri.ttf", 30)
    text = font.render("Score : " +str(count), True, black)
    gameDisplay.blit(text, (820,20))

def misses(count):
    font = pygame.font.SysFont("calibri.ttf", 30)
    text = font.render("Misses : " +str(count), True, black)
    gameDisplay.blit(text, (820,50))
    
def game_main():
    main_menu(0,0)
    
    pygame.display.update()

def game_loop():

    score_c = 0
    misses_c =0
    timer_s = 0
    timer_m = 0
    
    plane_w = 20
    plane_h = 15
    
    gameExit = False
        
    while not gameExit:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        scoreboard(800,0,150,display_height, grey)
        score(score_c)
        misses(misses_c)

        seconds = clock.tick()/1000
        timer_s += seconds

        display_timer_s = math.trunc(timer_s)
        if display_timer_s == 60:
            timer_s = 0
            timer_m += 1
        
        bg(0,0)
        plane(plane_x, plane_y)
        time(display_timer_s, timer_m)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if plane_x < mouse[0] < plane_x+plane_w and plane_y < mouse[1] < plane_y+plane_h:
                #print("HERE")
                if click[0] == 1:
                    #print("Allahua Akbar!")
                    score_c += 1
                    new_level()
            elif 0 < mouse[0] < 800 and 0 < mouse[1] < 600:
                if click[0] == 1:
                    misses_c += 1

game_loop()
pygame.quit()
quit()
