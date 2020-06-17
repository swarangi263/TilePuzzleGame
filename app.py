import pygame  #imported pygame module  
import game_config as gc

from pygame import display , event , image # imported packages
from animal import Animal
from time import sleep

pygame.init()  #initialises all modules that might be imported in pygame    

def find_index(x,y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index

display.set_caption('MyGame')

screen = display.set_mode((512,512))

matched = image.load('other_assets/matched.png')

running = True

tiles = [Animal(i) for i in range (0,gc.NUM_TILES_TOTAL)]       #all the images to tiles

current_images = []             #list of images currently being used

while running:
    current_event = event.get()
    for e in current_event:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN :
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos() #get the position of mouse
            index = find_index(mouse_x,mouse_y)       # to find on which tile mouse is
            if index not in current_images :        # to check if the same img is not clicked
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]



    screen.fill((255,255,255))

    total_skipped = 0

    for _ ,tile in enumerate(tiles):         #enumerate fn is used to get index also tile.index can be used
        image_i = tile.image if tile.index in current_images else tile.box
        
        if not tile.skip :
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else :
            total_skipped += 1
    
    display.flip()          #to change the screen

    if len(current_images) == 2:
        indx1, indx2 = current_images
        if tiles[indx1].name == tiles[indx2].name :
            tiles[indx1].skip = True
            tiles[indx2].skip = True
            sleep(0.4)
            screen.blit(matched, (0,0))
            display.flip()
            sleep(0.4)
            current_images = []
   
    #if len(current_images) == 0:
    #    screen.
    if total_skipped == len(tiles) :
        running = False

print('GoodBye!')