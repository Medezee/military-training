import pygame
import random
import math

#initialize the program
pygame.init()

display_width = 890
display_height = 740

white = (255,255,255)
grey = (100,100,100)
light_grey = (230,230,230)
black = (50,50,50)
dark = (0,0,0)
red = (229,57,90)
dark_red = (202,51,80)
green = (188,213,128)
dark_green = (150,172,98)
yellow = (255,199,48)
dark_yellow = (232,187,66)
blue = (38,207,255)
dark_blue = (37,170,226)
purple = (168,1,202)

gameDisplay = pygame.display.set_mode((display_width, display_height))

bgImg = pygame.image.load('background_1.png')
bgImg_scaled = pygame.transform.scale(bgImg, (720, 720))

mmImg = pygame.image.load('main_menu.png')
mmImg_scaled = pygame.transform.scale(mmImg, (890, 740))

manImg = pygame.image.load('instructions.png')
manImg_scaled = pygame.transform.scale(manImg, (890, 740))

planeImg = pygame.image.load('plane.png')

pygame.display.set_caption('YOU MUST TRAIN!')

font = pygame.font.SysFont("calibri.ttf", 30)
font_small = pygame.font.SysFont("calibri.ttf", 20)
font_little = pygame.font.SysFont("calibri.ttf", 5)


plane_x = random.randrange(30,725)
plane_y = random.randrange(25,730)

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

    plane_x = random.randrange(30,725)
    plane_y = random.randrange(25,730)

def time(sec, mints):
    font = pygame.font.SysFont("calibri.ttf", 30)
    displaytext = "%s:%s" % (mints, sec)
    text = font.render("Time : " +str(displaytext), True, black)
    gameDisplay.blit(text, (760,80))

def time_seg(sec, mints):
    font = pygame.font.SysFont("calibri.ttf", 30)
    displaytext = "%s:%s" % (mints, sec)
    text = font.render("Segm : " +str(displaytext), True, black)
    gameDisplay.blit(text, (760,110))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def scoreboard(x,y,w,h,color):
    pygame.draw.rect(gameDisplay, color, [x,y,w,h])

def colums(index):
    text = font_small.render(chr(65+index), True, black)
    gameDisplay.blit(text, (5, 40 + 60 * index))

def rows(index):
    text = font_small.render(str(index+1), True, black)
    gameDisplay.blit(text, (40 + 60 * index, 5))

def location(x,y):
    for i in range (12):
        for j in range (12):
            rect_x_start = 20 + j*60
            rect_x_end = 20 + (j + 1)*60
            rect_y_start = 20 + i*60
            rect_y_end = 20 + (i + 1)*60
            if rect_x_start < x < rect_x_end and rect_y_start < y < rect_y_end:
                text = font_small.render("Location: " + chr(65+i) + str(j+1), True, black)
                gameDisplay.blit(text, (760,150))
                break

def score(count):
    font = pygame.font.SysFont("calibri.ttf", 30)
    text = font.render("Score : " +str(count), True, black)
    gameDisplay.blit(text, (760,20))

def misses(count):
    font = pygame.font.SysFont("calibri.ttf", 30)
    text = font.render("Misses : " +str(count), True, black)
    gameDisplay.blit(text, (760,50))

def start_button(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, dark_green, [x,y,w,h])
    if x+w > mouse[0] > x and y+h > mouse[1] > y:    
        pygame.draw.rect(gameDisplay, green, [x,y,w,h])
        if click[0] == 1:
            game_loop()

    textSurf, textRect = text_objects("Start", font, black)
    textRect.center = (x+(w/2), y+(h/2))
    gameDisplay.blit(textSurf, textRect)

def back_button(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, dark_blue, [x,y,w,h])
    if x+w > mouse[0] > x and y+h > mouse[1] > y:    
        pygame.draw.rect(gameDisplay, blue, [x,y,w,h])
        if click[0] == 1:
            game_main()

    textSurf, textRect = text_objects("Back", font, black)
    textRect.center = (x+(w/2), y+(h/2))
    gameDisplay.blit(textSurf, textRect)
    
def instruction():
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        instructions(0,0)
        back_button(270,400,80,60)

        pygame.display.update()

def instruction_button(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, dark_yellow, [x,y,w,h])
    if x+w > mouse[0] > x and y+h > mouse[1] > y:    
        pygame.draw.rect(gameDisplay, yellow, [x,y,w,h])
        if click[0] == 1:
            instruction()

    textSurf, textRect = text_objects("Instructions", font_small, black)
    textRect.center = (x+(w/2), y+(h/2))
    gameDisplay.blit(textSurf, textRect)

def quit_button(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, dark_red, [x,y,w,h])
    if x+w > mouse[0] > x and y+h > mouse[1] > y:    
        pygame.draw.rect(gameDisplay, red, [x,y,w,h])
        if click[0] == 1:
            pygame.quit()
            quit()

    textSurf, textRect = text_objects("Quit", font, black)
    textRect.center = (x+(w/2), y+(h/2))
    gameDisplay.blit(textSurf, textRect)

def game_main():

    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        main_menu(0,0)
        start_button(170,640,80,60)
        instruction_button(395,650,80,60)
        quit_button(620,640,80,60)

        pygame.display.update()
        
def game_loop():
    clock = pygame.time.Clock()

    score_c = 0
    misses_c = -1
    timer_s = 0
    timer_m = 0
    timer_seg = 0
    timer_m_seg = 0
    
    plane_w = 20
    plane_h = 15

    gameExit = False
        
    while not gameExit:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        plane_center_x = plane_x + (plane_w / 2)
        plane_center_y = plane_y + (plane_h / 2)

        scoreboard(740,0,150,display_height, grey)
        score(score_c)
        misses(misses_c)

        seconds = clock.tick()/1000
        timer_s += seconds
        timer_seg += seconds

        display_timer_s = math.trunc(timer_s)
        if display_timer_s == 60:
            timer_s = 0
            timer_m += 1

        display_timer_seg = math.trunc(timer_seg)
        if display_timer_seg == 60:
            timer_seg = 0
            timer_m_seg += 1
        
        bg(20,20)
        plane(plane_x, plane_y)
        time(display_timer_s, timer_m)
        time_seg(display_timer_seg,timer_m_seg)
        location(plane_center_x, plane_center_y)

        pygame.draw.rect(gameDisplay, grey, [0,0,20,display_height])
        pygame.draw.rect(gameDisplay, grey, [0,0,display_width,20])

        for i in range (12):
            colums(i)
            rows(i)

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
                    timer_m_seg = 0
                    timer_seg = 0
            elif 20 < mouse[0] < 740 and 20 < mouse[1] < 740:
                if event.type == pygame.MOUSEBUTTONUP:
                    misses_c += 1
                    
game_main()
pygame.quit()
quit()
