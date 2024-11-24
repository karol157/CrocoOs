import pygame
import sys
from Config import *
import ctypes
import json
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Script'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Terminal'))
import Terminal
from Button import Button
import app


screen = pygame.display.set_mode((Weight, Height))
buttonOnOf = Button(1890, 0, "CrocoOs\\Descopt\\Image\\ON_OF") 
rec = pygame.Rect(0, 0, Weight, 70)
screen.fill(Bc_color)

pygame.draw.rect(screen, line_color, rec)
pygame.display.update()
hwnd = pygame.display.get_wm_info()['window']
#ctypes.windll.user32.SetWindowPos(hwnd, 1, 0, 0, 0, 0, 0x0001 | 0x0002)

terminal = {
    "icon" : pygame.image.load("CrocoOs\\Terminal\\icon.png"),
    "script" : Terminal.main(),
    "pc" : 1
}



while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()
    
    if buttonOnOf.tick():
        app.off_sys()
        sys.exit()
    
    
    buttonOnOf.draw(screen)
    pygame.display.update()

