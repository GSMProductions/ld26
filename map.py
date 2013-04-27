
import cocos

import data

class Map(cocos.scene.Scene):

    def __init__(self, name):

        self.name = name

        self.scroller = cocos.layer.ScrollingManager()
        self.char_layer = cocos.layer.ScrollableLayer()
        self.map_layer = cocos.tiles.load('maps/'+self.name+'.tmx')["Tile Layer 1"]

        self.scroller.add(self.map_layer)
        self.scroller.add(self.char_layer)

        cocos.scene.Scene.__init__(self, self.scroller)


    def spawnPlayer(self, player, position):

        self.scroller.set_focus(position[0]*data.TILE_SIZE, position[1]*data.TILE_SIZE)

