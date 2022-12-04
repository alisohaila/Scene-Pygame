import pygame, sys
from pygame.locals import QUIT

pygame.init()

#Set up the Drawing Screen /Window
screen = pygame.display.set_mode((400,300)) #defining the display, which is the "surface" that we will draw things to (pygame.Surface object)
pygame.display.set_caption('The beautiful scene!') #window title

BACKGROUND = (135, 206, 235) #setting the background color to the colour of sky blue
RED = (255, 0, 0) #setting the RGB code of the color red in this variable known as RED
GREEN = (0, 100, 0) #setting the RGB code of the color green in this variable known as GREEN
BLUE = (0, 0, 255) #setting the RGB code of the color blue in this variable known as BLUE
YELLOW = (252, 229, 112) #setting the RGB code of the color yellow in this variable known as YELLOW
BROWN = (150, 75, 0) #setting the RGB code of the color brown in this variable known as BROWN
SKIN_COLOR = (214, 161, 94) #setting the RGB code of the skin color in this variable known as SKIN_COLOR, so it could be used multiple times for the stickman

#Fill the Screen
screen.fill(BACKGROUND) #setting the background color to be sky blue
pygame.display.flip()

#SUN

pygame.draw.circle(screen, YELLOW, (350, 50), 30) #drawing the sun using a circle in the color yellow. The first value after the color placeholder means the x-coordinate, then the y-coordinate, and the last value means the width of the circle.

#GRASS

pygame.draw.rect(screen, (70, 171, 44), (0, 250, 500, 100)) #drawing the grass using a rectangle in the color green. For the color placeholder, we add the color by using its RGB code. The first value after that means the x-coordinate, then the y-coordinate, the width, and finally the height of the rectangle. 

#DOORS

pygame.draw.rect(screen, BROWN, (250, 150, 100, 100), 3) #drawing the doors using rectangle with just an outline in the color brown. 
pygame.draw.line(screen, BROWN, (300, 150), (300, 250)) #drawing the doors' divider using a line 
pygame.draw.circle(screen, BROWN, (285, 200), 5) #drawing the left door's knob using a line
pygame.draw.circle(screen, BROWN, (315, 200), 5) #drawing the right door's knob using a line

#STICKMAN

pygame.draw.circle(screen, (SKIN_COLOR), (100, 200), 17) #drawing the stickman's face using a circle in the skin color. The first value after the color placeholder means the x-coordinate, then the y-coordinate, and the width.
pygame.draw.line(screen, (SKIN_COLOR), (100, 215), (100, 250), 3) #drawing the stickman's body using a line. The first value after the color placeholder means a pair of x-coordinates, then a pair of y-coordinates, and then the width of the line. 
pygame.draw.line(screen, (SKIN_COLOR), (100, 215), (80, 230), 3) #drawing the stickman's left arm using a line
pygame.draw.line(screen, (SKIN_COLOR), (100, 215), (120, 230), 3) #drawing the stickman's right arm using a line
pygame.draw.line(screen, (SKIN_COLOR), (75, 270), (100, 250), 3) #drawing the stickman's left leg using a line
pygame.draw.line(screen, (SKIN_COLOR), (125, 270), (100, 250), 3)  #drawing the stickman's right leg using a line

#BANGLADESH'S FLAG

pygame.draw.rect(screen, GREEN, (10, 10, 130, 90)) #drawing the flag's background using a rectangle in color green
pygame.draw.circle(screen, RED, (75, 55), 22) #drawing the flag's circle in the middle using a circle in the color red. The first value after the color placeholder means the x-coordinate, then the y-coordinate, and the width.

while True:
    
    pygame.display.update()
