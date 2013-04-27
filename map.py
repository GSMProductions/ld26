
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

        self.scroller.add(self.map_layer)
        self.scroller.add(self.map_layer2)

        self.scroller.add(self.char_layer)

        self.scroller.add(self.map_layer3, z = 2)


        #self.player = None


        cocos.scene.Scene.__init__(self, self.scroller)


    def spawnPlayer(self, player, position, transition=True):

        if transition:
            cocos.director.director.replace(cocos.scenes.FadeTransition( self, duration=2 ) )

        self.char_layer.add(player)

        player.current_map = self

        player.map_position = [position[0], position[1]]
        player.position = (position[0]*data.TILE_SIZE + data.TILE_SIZE/2, position[1]*data.TILE_SIZE+2)
        self.scroller.set_focus(position[0]*data.TILE_SIZE, position[1]*data.TILE_SIZE)

