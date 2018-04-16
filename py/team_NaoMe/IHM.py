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

clickable_area_left_strafe = pygame.Rect((1*taille_touches, 3*taille_touches), (1*taille_touches, 1*taille_touches))
rect_left_strafe = pygame.Surface(clickable_area_left_strafe.size)

clickable_area_forward = pygame.Rect((2*taille_touches, 2*taille_touches), (1*taille_touches, 1*taille_touches))
rect_forward = pygame.Surface(clickable_area_left_strafe.size)

clickable_area_right_strafe = pygame.Rect((3*taille_touches, 3*taille_touches), (1*taille_touches, 1*taille_touches))
rect_right_strafe = pygame.Surface(clickable_area_right_strafe.size)

clickable_area_backward = pygame.Rect((2*taille_touches, 4*taille_touches), (1*taille_touches, 1*taille_touches))
rect_backward = pygame.Surface(clickable_area_backward.size)

clickable_area_pause = pygame.Rect((2*taille_touches, 3*taille_touches), (1*taille_touches, 1*taille_touches))
rect_pause = pygame.Surface(clickable_area_pause.size)

clickable_area_fast_forward = pygame.Rect((2*taille_touches,1*taille_touches), (1*taille_touches, 1*taille_touches))
rect_fast_forward = pygame.Surface(clickable_area_fast_forward.size)

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

action_en_cours = "PAUSE"

while continuer:
    
    #NaoMe.getImage()
    
    rect_left_strafe.fill(COLORS[2])
    rect_backward.fill(COLORS[2])
    rect_forward.fill(COLORS[2])
    rect_right_strafe.fill(COLORS[2])
    rect_pause.fill(COLORS[2])
    rect_fast_forward.fill(COLORS[2])
    rect_rotate_right.fill(COLORS[2])
    rect_rotate_left.fill(COLORS[2])
    rect_shoot_right.fill(COLORS[2])
    rect_shoot_left.fill(COLORS[2])
    rect_angle_rotation.fill(COLORS[0])
    
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                action_en_cours = "RIGHT_STRAFE"
                print("RIGHT")
            
            if event.key == K_LEFT:
                action_en_cours = "LEFT_STRAFE"
                print("LEFT")
            
            if  event.key == K_UP:
                if action_en_cours == "FORWARD":
                    action_en_cours = "FAST_FORWARD"
                    print("RUN")
                elif action_en_cours != "FAST_FORWARD":
                    action_en_cours = "FORWARD"
                    print("UP")
            
            if event.key == K_DOWN:
                if action_en_cours == "FAST_FORWARD":
                    action_en_cours = "FORWARD"
                    print("UP")
                elif action_en_cours == "FORWARD":
                    action_en_cours = "PAUSE"
                    print("PAUSE")
                else:
                    action_en_cours = "BACKWARD"
                    print("RECULE")
    
        if event.type == QUIT:     #Si un de ces événements est de type QUIT

            continuer = 0      #On arrête la boucle
        
        if event.type == MOUSEBUTTONDOWN: # quand je relache le bouton
            if clickable_area_left_strafe.collidepoint(event.pos):
                action_en_cours = "LEFT_STRAFE"
                print("LEFT")
            if clickable_area_forward.collidepoint(event.pos):
                action_en_cours = "FORWARD"
                print("UP")
            if clickable_area_backward.collidepoint(event.pos):
                action_en_cours = "BACKWARD"
                print("DOWN")
            if clickable_area_right_strafe.collidepoint(event.pos):
                action_en_cours = "RIGHT_STRAFE"
                print("RIGHT")
            if clickable_area_pause.collidepoint(event.pos):
                action_en_cours = "PAUSE"
                print("PAUSE")
            if clickable_area_fast_forward.collidepoint(event.pos):
                action_en_cours = "FAST_FORWARD"
                print("RUN")
            if clickable_area_rotate_left.collidepoint(event.pos):
                action_en_cours = "ROTATE_LEFT"
                print("ROTATE LEFT")
            if clickable_area_rotate_right.collidepoint(event.pos):
                action_en_cours = "ROTATE_RIGHT"
                print("ROTATE RIGHT")
            if clickable_area_shoot_left.collidepoint(event.pos):
                action_en_cours = "SHOOT_LEFT"
                print("SHOOT LEFT")
            if clickable_area_shoot_right.collidepoint(event.pos):
                action_en_cours = "SHOOT_RIGHT"
                print("SHOOT RIGHT")
            if clickable_area_angle_rotation.collidepoint(event.pos):
                action_en_cours = "TOURNE"
                angle = 0.5*event.pos[0]-240
                print("TOURNE"+str(angle))
            
    if action_en_cours == "FORWARD":
        rect_forward.fill(COLORS[1])
    if action_en_cours == "LEFT_STRAFE":
        rect_left_strafe.fill(COLORS[1])
    if action_en_cours == "RIGHT_STRAFE":
        rect_right_strafe.fill(COLORS[1])
    if action_en_cours == "BACKWARD":
        rect_backward.fill(COLORS[1])
    if action_en_cours == "PAUSE":
        rect_pause.fill(COLORS[1])
    if action_en_cours == "FAST_FORWARD":
        rect_fast_forward.fill(COLORS[1])
    if action_en_cours == "ROTATE_LEFT":
        rect_rotate_left.fill(COLORS[1])
    if action_en_cours == "ROTATE_RIGHT":
        rect_rotate_right.fill(COLORS[1])
    if action_en_cours == "SHOOT_LEFT":
        rect_shoot_left.fill(COLORS[1])
    if action_en_cours == "SHOOT_RIGHT":
        rect_shoot_right.fill(COLORS[1])
    
    screen.fill(0) # On efface tout l'écran
    screen.blit(rect_forward, clickable_area_forward)
    screen.blit(rect_backward, clickable_area_backward)
    screen.blit(rect_right_strafe, clickable_area_right_strafe)
    screen.blit(rect_left_strafe, clickable_area_left_strafe)
    screen.blit(rect_pause, clickable_area_pause)
    screen.blit(rect_fast_forward, clickable_area_fast_forward)
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