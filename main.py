import pygame
from pygame.locals import *
import os

pygame.init()

screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

font = "8-BIT WONDER.ttf"
bg = pygame.image.load("3R2.png")

def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="Leaderboard"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        import game
                    if selected=="Leaderboard":
                        os.system("mysq2.py")
                    if selected=="quit":
                        quit()
                if event.key==pygame.K_RIGHT:
                    selected="quit"
        screen.blit(bg, (0, 0))
        title1=text_format("Last", font, 70, yellow)
        title2=text_format("Stand", font, 70, yellow)
        if selected=="start":
            text_start=text_format("START", font, 25, red)
        else:
            text_start = text_format("START", font, 25, white)
        if selected=="Leaderboard":
            text_leaderboard=text_format("LEADERBOARD", font, 25, red)
        else:
            text_leaderboard = text_format("LEADERBOARD", font, 25, white)
        if selected=="quit":
            text_quit=text_format("EXIT GAME", font, 25, red)
        else:
            text_quit=text_format("EXIT GAME", font, 25, white)

        title1_rect=title1.get_rect()
        title2_rect=title2.get_rect()
        start_rect=text_start.get_rect()
        leaderboard_rect=text_leaderboard.get_rect()
        quit_rect=text_quit.get_rect()

        screen.blit(title1, (screen_width/2 - (title1_rect[2]/2), 110))
        screen.blit(title2, (screen_width/2 - (title2_rect[2]/2), 200))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 330))
        screen.blit(text_leaderboard, (screen_width/2 - (leaderboard_rect[2]/2), 390))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 450))
        pygame.display.update()
        pygame.display.set_caption("LAST STAND")

main_menu()