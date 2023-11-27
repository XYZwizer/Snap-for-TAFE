import pygame
import math
from GUI.math2D import *
pygame.init()
pygame.font.init()
#font = pygame.font.SysFont("segoeuisymbol", 100)
font = pygame.font.SysFont("dejavusans", 100)
font = pygame.font.Font("GUI/seguisym.ttf",100)

class display_card:
    def __init__(self,init_canvas,init_pos,init_angel):
        self.canvas = init_canvas
        self.pos = init_pos
        self.angel = init_angel
        self.rot = 1
        self.card = '🂠'
        
    def set_all(self,new_data):
        self.pos = pos(new_data.x,new_data.y)
        self.angel = new_data.points[2]
        self.rot = new_data.points[3]
        
    def render(self):
        imgT = font.render('🂠', True, (255,255,255))
        if self.rot < 0:
            rot = -self.rot
            img = font.render('🂠', True, (255,255,255))
        else:
            rot = self.rot
            img = font.render(self.card, True, (255,255,255))
        
        
        pygame.draw.rect(imgT, (0,0,222), pygame.Rect(4, 28, 58, 90))
        
        #img = font.render(self.card, True, (255,255,255)) #,(0,0,0,0)
        imgT.blit(img,(0,0))
        
        new_size = pos(imgT.get_size())
        new_size.x *= rot
        
        imgT = pygame.transform.scale(imgT, new_size.AsTuple())
        
        imgT = pygame.transform.rotate(imgT, self.angel)
        
        
        loc_center = (pos(imgT.get_size() )/2)
        loc = self.pos - loc_center
        
        self.canvas.blit(imgT, loc.AsTuple())
        #pygame.draw.circle(self.canvas,(0,255,0),self.pos.AsTuple(),10)
def generate_round_table(canvas,center,num_players,size,turn):
    players = []
    step = (math.pi*2)/(num_players)
    for a in range(1,num_players+1):
        cer = pos.OnCircle((step*a)+turn)
        card_pos = center + (cer*size)
        card_angel = math.degrees(math.atan(cer.x/cer.y))
        players.append(display_card(canvas,card_pos,card_angel))
    return players
    

