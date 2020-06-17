import os 
import random
import game_config as gc

from pygame import image,transform

animal_count = dict((a,0) for a in gc.ASSET_FILES) #created a dictionary to store the animals 

def available_animals():
    return [a for a,c in animal_count.items() if c < 2]         #returns the count of animals still not used 

class Animal:
    def __init__(self, index):
        self.index = index                      #index of the animal
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.name = random.choice(available_animals())      #would give animal random name      
        animal_count[self.name] += 1

        self.image_path = os.path.join(gc.ASSET_DIR, self.name)         #set the image to the variable
        self.image = image.load(self.image_path)                #load the image into the variable
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE- 2*gc.MARGIN , gc.IMAGE_SIZE- 2*gc.MARGIN))     #-2 is uesd bcoz of margin size
        self.box = self.image.copy()        #copy of the image        
        self.box.fill((200,200,200))        #if image not matched return grey box
        
        self.skip = False       #initalise it to false , flag will skip printing image or box if already matched



        