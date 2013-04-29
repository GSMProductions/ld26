
import cocos
import cocos.scenes

import data

    
class Map(cocos.scene.Scene):

    def __init__(self, name):

        self.name = name

        self.scroller = cocos.layer.ScrollingManager()
        self.char_layer = cocos.layer.ScrollableLayer()
        self.map_layer = cocos.tiles.load('maps/'+self.name+'.tmx')["ground1"]
        self.map_layer2 = cocos.tiles.load('maps/'+self.name+'.tmx')["ground2"]
        self.map_layer3 = cocos.tiles.load('maps/'+self.name+'.tmx')["foreground"]

        self.scroller.add(self.map_layer, z = 0)

        self.scroller.add(self.map_layer2, z = 1)

        self.scroller.add(self.char_layer, z = 2)

        self.scroller.add(self.map_layer3, z = 3)


        #self.player = None

        self.npcs = {}
        self.items = []

        cocos.scene.Scene.__init__(self, self.scroller)


    def placeCharacter(self, character, position):

        self.char_layer.add(character)
        character.current_map = self
        character.map_position = [position[0], position[1]]
        character.position = (position[0]*data.TILE_SIZE + data.TILE_SIZE/2, position[1]*data.TILE_SIZE+2)        

        if character.name[0:3] != "nod":
            self.npcs[character.name] = character

    def placeItem(self, item, position):

        self.char_layer.add(item)
        item.current_map = self
        item.map_position = [position[0], position[1]]
        item.position = (position[0]*data.TILE_SIZE + data.TILE_SIZE/2, position[1]*data.TILE_SIZE+2)        

        self.npcs.append(item)


    def spawnPlayer(self, player, position, transition=True):

        if transition:
            cocos.director.director.replace(cocos.scenes.FadeTransition( self, duration=2 ) )

        self.placeCharacter(player, position)

        self.scroller.set_focus(position[0]*data.TILE_SIZE, position[1]*data.TILE_SIZE)


