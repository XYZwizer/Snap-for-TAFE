import pygame
import time
import math
import random
#mine
from snap import *
from GUI.math2D import *
from GUI.cards_GUI import *
from GUI.interpolation import *

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
center = pos(width,height)/2

num_players = 10
display_players = generate_round_table(screen,center,num_players,(height/2)-50,math.pi/2)
game = SnapGame(num_players)

display_center_pile = display_card(screen,center,0)

moveing_card = display_card(screen,center,0)


deal_animation = animation(time.time(),0.5,pos(center.x,center.y,0,-1),pos(center.x,center.y,0,1))
waitTime = time.time();

def try_snap_with_animation(player_num):
    if game.try_snap(player_num):
        player = display_players[player_num]
        print("snap")
        deal_animation = animation(time.time(),1.5,pos(center.x,center.y,0,1),pos(player.pos.x,player.pos.y,player.angel,-1))
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            try_snap_with_animation(1)

    #do turn
    if deal_animation.concluded():

        if random.randint(0,2) == 2:
            try_snap_with_animation(random.randint(0,num_players-1))

        if time.time() > waitTime:

            if game.turn() != None:
                print("win!!!!!!!!!!")
                break
            player = display_players[game.player_of_current_turn.id]
            deal_animation = animation(time.time(),0.5,pos(player.pos.x,player.pos.y,player.angel,-1),pos(center.x,center.y,0,1),)
            waitTime = time.time() + 1.5




    #render cards 
    for ply in game.players:
        if ply.number_of_cards != 0:
            if not (ply.number_of_cards < 2 and ply == game.player_of_current_turn):
                display_players[ply.id].render()

    abstract = 2 if not deal_animation.concluded() else 1
    if game.center_pile.number_of_cards >= abstract:
        display_center_pile.card = game.center_pile[-abstract].unicode_char()
        display_center_pile.render()
    if game.center_pile.number_of_cards > 0:
        moveing_card.card = game.center_pile[-1].unicode_char()
    new_moveing_card_position = deal_animation.dataAtTime()
    moveing_card.set_all(new_moveing_card_position)
    moveing_card.render()


    
    pygame.display.update()
    screen.fill((0,0,0)) #clear screen
