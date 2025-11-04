low# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 10:19:57 2025

@author: 260987
"""

import pygame  
import random  
  
def button(surface):  
    x, y = pygame.mouse.get_pos()  
    rect_coordinates = (50, 50, 50, 50)  
    def inside_rectangle(x, y, rect):  
        xr, yr, width, height = rect  
        return (  
            xr <= x and x <= (xr + width) and   
            yr <= y and y <= (yr + height)  
        )  
    if inside_rectangle(x, y, rect_coordinates):  
        pygame.draw.rect(  
            surface,  
            color="gray67",  
            rect=rect_coordinates,  
            width=0,  
            border_radius=10  
        )  
    else:  
        pygame.draw.rect(  
            surface,  
            color="gray",  
            rect=rect_coordinates,  
            width=0,  
            border_radius=10  
        )  
    return rect_coordinates  
  
if __name__ == "__main__":  
    pygame.init()  
    screen = pygame.display.set_mode((1280, 720))  
    clock = pygame.time.Clock()  
    running = True  
    color = "blue"  
      
    while running:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False  
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                # Check if click is inside button  
                x, y = event.pos  
                rect_coordinates = (50, 50, 50, 50)  
                xr, yr, width, height = rect_coordinates  
                if xr <= x <= (xr + width) and yr <= y <= (yr + height):  
                    # Generate random color  
                    color = (random.randint(0, 255),   
                            random.randint(0, 255),   
                            random.randint(0, 255)) 
                  
        screen.fill(color)  
        button(screen)  
        pygame.display.flip()  
        clock.tick(60)  
          
    pygame.quit()
