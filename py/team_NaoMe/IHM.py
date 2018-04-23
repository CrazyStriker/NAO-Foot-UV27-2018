#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 02:56:41 2018

@author: sadomablow
"""

import time
import pygame
from pygame.locals import *
import sys
#import NaoMe

taille_touches = 50


pygame.init()
screen = pygame.display.set_mode((320*3, 240*3))


font=pygame.font.Font(None, 20)


pygame.display.flip()

continuer = 1
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = (RED, GREEN, BLUE)
color_index = 0
 
#Création des touches

clickable_area_StrafeL = pygame.Rect((1*taille_touches, 3*taille_touches), (1*taille_touches, 1*taille_touches))
rect_StrafeL = pygame.Surface(clickable_area_StrafeL.size)

clickable_area_Go = pygame.Rect((2*taille_touches, 2*taille_touches), (1*taille_touches, 1*taille_touches))
rect_Go = pygame.Surface(clickable_area_StrafeL.size)

clickable_area_StrafeR = pygame.Rect((3*taille_touches, 3*taille_touches), (1*taille_touches, 1*taille_touches))
rect_StrafeR = pygame.Surface(clickable_area_StrafeR.size)

clickable_area_MovingBackward = pygame.Rect((2*taille_touches, 4*taille_touches), (1*taille_touches, 1*taille_touches))
rect_MovingBackward = pygame.Surface(clickable_area_MovingBackward.size)

clickable_area_Wait = pygame.Rect((2*taille_touches, 3*taille_touches), (1*taille_touches, 1*taille_touches))
rect_Wait = pygame.Surface(clickable_area_Wait.size)

clickable_area_GoFast = pygame.Rect((2*taille_touches,1*taille_touches), (1*taille_touches, 1*taille_touches))
rect_GoFast = pygame.Surface(clickable_area_GoFast.size)

clickable_area_rotate_right = pygame.Rect((3*taille_touches,2*taille_touches), (1*taille_touches, 1*taille_touches))
rect_rotate_right = pygame.Surface(clickable_area_rotate_right.size)

clickable_area_rotate_left = pygame.Rect((1*taille_touches,2*taille_touches), (1*taille_touches, 1*taille_touches))
rect_rotate_left = pygame.Surface(clickable_area_rotate_left.size)

clickable_area_shoot_right = pygame.Rect((3*taille_touches,4*taille_touches), (1*taille_touches, 1*taille_touches))
rect_shoot_right = pygame.Surface(clickable_area_shoot_right.size)

clickable_area_shoot_left = pygame.Rect((1*taille_touches,4*taille_touches), (1*taille_touches, 1*taille_touches))
rect_shoot_left = pygame.Surface(clickable_area_shoot_left.size)

clickable_area_angle_rotation = pygame.Rect((120,630), (720, 50))
rect_angle_rotation = pygame.Surface(clickable_area_angle_rotation.size)

#Boucle infinie

action_en_cours = "Wait"

while continuer:
    
    #NaoMe.getImage()
    
    rect_StrafeL.fill(COLORS[2])
    rect_MovingBackward.fill(COLORS[2])
    rect_Go.fill(COLORS[2])
    rect_StrafeR.fill(COLORS[2])
    rect_Wait.fill(COLORS[2])
    rect_GoFast.fill(COLORS[2])
    rect_rotate_right.fill(COLORS[2])
    rect_rotate_left.fill(COLORS[2])
    rect_shoot_right.fill(COLORS[2])
    rect_shoot_left.fill(COLORS[2])
    rect_angle_rotation.fill(COLORS[0])
    
    
        if event.type == QUIT:     #Si un de ces événements est de type QUIT

            continuer = 0      #On arrête la boucle
        
        if event.type == MOUSEBUTTONDOWN: # quand je relache le bouton
            if clickable_area_StrafeL.collidepoint(event.pos):
                action_en_cours = "StrafeL"
                print("LEFT")
            if clickable_area_Go.collidepoint(event.pos):
                action_en_cours = "Go"
                print("UP")
            if clickable_area_MovingBackward.collidepoint(event.pos):
                action_en_cours = "MovingBackward"
                print("DOWN")
            if clickable_area_StrafeR.collidepoint(event.pos):
                action_en_cours = "StrafeR"
                print("RIGHT")
            if clickable_area_Wait.collidepoint(event.pos):
                action_en_cours = "Wait"
                print("Wait")
            if clickable_area_GoFast.collidepoint(event.pos):
                action_en_cours = "GoFast"
                print("RUN")
            if clickable_area_rotate_left.collidepoint(event.pos):
                action_en_cours = "TurnL"
                print("ROTATE LEFT")
            if clickable_area_rotate_right.collidepoint(event.pos):
                action_en_cours = "TurnR"
                print("ROTATE RIGHT")
            if clickable_area_shoot_left.collidepoint(event.pos):
                action_en_cours = "KickL"
                print("SHOOT LEFT")
            if clickable_area_shoot_right.collidepoint(event.pos):
                action_en_cours = "KickR"
                print("SHOOT RIGHT")
            if clickable_area_angle_rotation.collidepoint(event.pos):
                action_en_cours = "TOURNE"
                angle = 0.5*event.pos[0]-240
                print("TOURNE"+str(angle))
            
    if action_en_cours == "Go":
        rect_Go.fill(COLORS[1])
    if action_en_cours == "StrafeL":
        rect_StrafeL.fill(COLORS[1])
    if action_en_cours == "StrafeR":
        rect_StrafeR.fill(COLORS[1])
    if action_en_cours == "MovingBackward":
        rect_MovingBackward.fill(COLORS[1])
    if action_en_cours == "Wait":
        rect_Wait.fill(COLORS[1])
    if action_en_cours == "GoFast":
        rect_GoFast.fill(COLORS[1])
    if action_en_cours == "TurnL":
        rect_rotate_left.fill(COLORS[1])
    if action_en_cours == "TurnR":
        rect_rotate_right.fill(COLORS[1])
    if action_en_cours == "KickL":
        rect_shoot_left.fill(COLORS[1])
    if action_en_cours == "KickR":
        rect_shoot_right.fill(COLORS[1])
    
    screen.fill(0) # On efface tout l'écran
    screen.blit(rect_Go, clickable_area_Go)
    screen.blit(rect_MovingBackward, clickable_area_MovingBackward)
    screen.blit(rect_StrafeR, clickable_area_StrafeR)
    screen.blit(rect_StrafeL, clickable_area_StrafeL)
    screen.blit(rect_Wait, clickable_area_Wait)
    screen.blit(rect_GoFast, clickable_area_GoFast)
    screen.blit(rect_rotate_right, clickable_area_rotate_right)
    screen.blit(rect_rotate_left, clickable_area_rotate_left)
    screen.blit(rect_shoot_right, clickable_area_shoot_right)
    screen.blit(rect_shoot_left, clickable_area_shoot_left)
    screen.blit(rect_angle_rotation,clickable_area_angle_rotation)
    
    text = font.render("FW",1,(255,255,255))
    screen.blit(text, (2*taille_touches+taille_touches/8, 2*taille_touches+taille_touches/4))
    text = font.render("BW",1,(255,255,255))
    screen.blit(text, (2*taille_touches+taille_touches/8, 4*taille_touches+taille_touches/4))
    text = font.render("RS",1,(255,255,255))
    screen.blit(text, (3*taille_touches+taille_touches/8, 3*taille_touches+taille_touches/4))
    text = font.render("LS",1,(255,255,255))
    screen.blit(text, (1*taille_touches+taille_touches/8, 3*taille_touches+taille_touches/4))
    text = font.render("WT",1,(255,255,255))
    screen.blit(text, (2*taille_touches+taille_touches/8, 3*taille_touches+taille_touches/4))
    text = font.render("FFW",1,(255,255,255))
    screen.blit(text, (2*taille_touches+taille_touches/8, 1*taille_touches+taille_touches/4))
    text = font.render("RL",1,(255,255,255))
    screen.blit(text, (1*taille_touches+taille_touches/8, 2*taille_touches+taille_touches/4))
    text = font.render("RR",1,(255,255,255))
    screen.blit(text, (3*taille_touches+taille_touches/8, 2*taille_touches+taille_touches/4))
    
    
    pygame.display.flip()
 

pygame.quit()