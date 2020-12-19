import pygame
import time
pygame.init()

white = [255, 255, 255]
red = [255, 0, 0]
dark_red=[132,0,0]
black = [0, 0, 0]
green = [0,255,0]
dark_green=[0,83,2]
game_border = [58, 58, 58]
dark_button = [31, 31, 75]
light_button = [62, 62, 151]
window_width = 600
window_height = 500
border_width = 15

rect_x = window_width // 2
rect_y = window_height - border_width - 20
rect_width = 100
rect_height = 20

change_x = 0
change_y = 0

ball_x = 100
ball_y = 20
ball_change_x = 2
ball_change_y = 7

score = 0

intro=True
main_game=False
over=False
pause=False

window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

resumeImage = pygame.image.load('resume.png')

def slab(window, color, rect_x, rect_y, w, h):
    pygame.draw.rect(window, color, (rect_x, rect_y, w, h))


def text_object(text, font):
    textSusrface = font.render(text, True, black)
    return textSusrface, textSusrface.get_rect()


def text_object1(text, font):
    textSusrface = font.render(text, True, white)
    return textSusrface, textSusrface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    global intro,over,main_game,pause
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, ac, (x, y, w, h), 0, 20)
        if click[0] and action != None:
            if action == "start":
                #print("start")
                intro=False
                main_game=True
                over=False

                game_loop()
            elif action == "exit":
                quit()

    else:
        pygame.draw.rect(window, ic, (x, y, w, h), 0, 20)

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_object1(msg, small_text)
    textRect.center = ((x + (w // 2)), (y + (h // 2)))
    window.blit(textSurf, textRect)


def round_button(msg, x,y,r,ic, ac, action=None):
    global over,intro,main_game,pause,score
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x-r<mouse[0]<x+r and y-r <mouse[1] <y+r:
        pygame.draw.circle(window,ac,(x,y),r)
        if click[0] and action!=None:
            if action== "start":
                over=False
                intro=True
                game_loop()
            if action=="yes":
                score=0
                intro=True
                game_intro()
            elif action=="resume":
                pause=False
            elif action=="exit" or action=="no" or action=="exitGame-yes":
                pygame.quit()
                quit()
            elif action=="game_exit":
                exitGame()
            elif action=="exitGame-no":
                game_loop()


    else:
        pygame.draw.circle(window, ic, (x, y), r)

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_object1(msg, small_text)
    textRect.center = ((x ,y))
    window.blit(textSurf, textRect)

def exitGame():

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            else:
                pass
        window.fill(white)

        pygame.draw.rect(window, dark_button, (20, 80, 450, 200), 0, 10)

        smallText = pygame.font.Font('freesansbold.ttf', 25)


        # message---------------------->
        TextSurf, TextRect = text_object1("Are you sure ?", smallText)
        TextRect.center = ((250, 120))
        window.blit(TextSurf, TextRect)

        # yes and no button-------------->
        round_button("YES", 160, 190, 30, green, dark_green, "exitGame-yes")
        round_button("NO", 330, 190, 30, red, dark_red, "exitGame-no")

        pygame.display.update()




def crash(text,score):
    global over,main_game,pause,intro

    while over:
        #print(f"game--over--{intro},{main_game},{over},{pause}")
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            else:
                pass

        window.fill(white)
        #game over text--------------->
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_object(text, largeText)
        TextRect.center = ((250, 50))
        window.blit(TextSurf, TextRect)

        #your score------------------>
        smallText = pygame.font.Font('freesansbold.ttf', 25)
        TextSurf, TextRect = text_object("Your score:"+str(score), smallText)
        TextRect.center = ((250, 100))
        window.blit(TextSurf, TextRect)

        pygame.draw.rect(window,dark_button,(20,150,450,200),0,10)

        #message---------------------->
        TextSurf, TextRect = text_object1("Do you want to play again ?", smallText)
        TextRect.center = ((250, 200))
        window.blit(TextSurf, TextRect)

        #yes and no button-------------->
        round_button("YES", 150,260 ,30,green, dark_green, "yes")
        round_button("NO", 330,260,30 , red, dark_red, "no")

        pygame.display.update()


def paused():
    global pause

    while pause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            else:
                pass

        window.fill(white)
        # game over text--------------->
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_object("Pause", largeText)
        TextRect.center = ((250, 50))
        window.blit(TextSurf, TextRect)

        pygame.draw.rect(window, dark_button, (20, 150, 450, 200), 0, 10)

        # yes and no button-------------->
        round_button("resume", 150, 260, 50, green, dark_green, "resume")
        round_button("exit", 330, 260, 50, red, dark_red, "game_exit")

        pygame.display.update()

def things_dodged(score):
    font=pygame.font.Font(None,25)
    text=font.render("Score:"+str(score),True,white)
    window.blit(text,(0,0))

def game_intro():
    global intro,over,main_game,pause

    while intro:
        #print(f"game--intro--{intro},{main_game},{over},{pause}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_object("PONG GAME", largeText)
        TextRect.center = ((250, 50))
        window.blit(TextSurf, TextRect)


        button("START", 190, 120, 120,40, light_button, dark_button, "start")
        button("HIGHT SCORE", 170, 180, 160, 40, light_button, dark_button, "score")
        button("DEFICULTY", 180, 240, 140, 40, light_button, dark_button, "deficulty")
        button("Exit", 190, 300, 120, 40, light_button, dark_button, "exit")

        pygame.display.update()
    pygame.quit()
    quit()



def game_loop():
    global ball_x, ball_y, ball_change_x, ball_change_y
    global rect_x, rect_y, rect_height, rect_width, change_x, change_y
    global score,pause
    global main_game,intro,over,pause


    while main_game:

        #print(f"game--loop--{intro},{main_game},{over},{pause}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                        # print("LEFT-CLICK")
                        change_x -= 5
                    if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                        # print("RIGHT-CLICK")
                        change_x += 5
                    if event.key == pygame.K_p:
                        pause = True
                        paused()
                if event.type == pygame.KEYUP:
                    change_x = 0
                    change_y = 0

        ball_x += ball_change_x
        ball_y += ball_change_y


        # right wall------------>
        if ball_x > window_width - border_width:
            ball_x = window_width - border_width
            ball_change_x = ball_change_x * -1
        # left wall------------->
        if ball_x < border_width:
            ball_x = border_width
            ball_change_x = ball_change_x * -1

        # up wall------------->
        if ball_y < border_width+35:
            ball_y = border_width+35
            ball_change_y = ball_change_y * -1
            score += 1
            print(f"score={score}")

        # down wall------------>
        # if ball_y > window_height - border_width:
        #    ball_y = window_height - border_width
        #   ball_change_y = ball_change_y * -1

        if ball_y > window_height - border_width - 25:
            if rect_x < ball_x < rect_x + rect_width:
                ball_y = window_height - border_width - 25
                ball_change_y = ball_change_y * -1

            if ball_y > window_height - border_width:
                #main_game=False
                ball_x = 100
                ball_y = 50
                over=True
                intro=False
                crash("GAME OVER", score)

        rect_x += change_x
        rect_y += change_y

        if rect_x < border_width:
            rect_x = border_width
        if rect_x + rect_width > window_width - border_width:
            rect_x = window_width - border_width - rect_width

        #pause button click logic----------------->
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
       # print(mouse)

            #print("YES")


        window.fill(black)


        #pygame.draw.rect(window, (0, 255, 0), (450, 0, 30, 30), 3)
        #score update------------------>
        things_dodged(score)
       #resume button------------------>
        window.blit(resumeImage, (450, 0))
        if 450 < mouse[0] < 500 and 0 < mouse[1] < 30:
            #pygame.draw.circle(window,(191,168,6),(460,10),10)
            #pygame.draw.rect(window,(0,255,0),(450,0,40,30))
            if click[0] :
                pause=True
                paused()

        # game border------------------------------------>
        pygame.draw.rect(window, game_border, (0, 35, window_width, window_height-35),border_width)

        # slab----------------------------------------------->
        pygame.draw.rect(window, red, (rect_x, rect_y, 100, 20), 0, 10)

        # ball---------------------------------------------->
        pygame.draw.circle(window, white, (ball_x, ball_y), 10)



        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()



game_intro()
game_loop()
pygame.quit()
quit()