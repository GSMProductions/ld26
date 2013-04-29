
import cocos
import cocos.scenes

import pyglet

import data

from data import DIALOGS, mapKey
    
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

        self.dialog_layer = cocos.layer.Layer()
        self.dialog_box = cocos.sprite.Sprite(pyglet.image.load('img/GUI/dialog_box.png'), anchor=(0,0))
        self.dialog_layer.add(self.dialog_box,z=0)
        self.dialog_layer.visible = False
        self.add(self.dialog_layer, z = 4)
        self.dialog_line1 = cocos.text.Label(anchor_x = 'left',font_name='Statix',position=(100,90), color=(36,36,36,255), font_size=30)
        self.dialog_line2 = cocos.text.Label(anchor_x = 'left',font_name='Statix',position=(100,46), color=(36,36,36,255), font_size=30)

        self.dialog_arrow = cocos.sprite.Sprite(pyglet.image.load('img/GUI/dialog_arrow.png'), anchor=(0,0))
        self.dialog_arrow.position = (690,15)
        self.dialog_arrow.visible = False
        self.dialog_layer.add(self.dialog_arrow, z = 5)

        self.dialog_layer.add(self.dialog_line1, z = 5)
        self.dialog_layer.add(self.dialog_line2, z = 5)

        self.current_dialog = []
        self.current_dialog_speaker = []
        self.current_dialog_counter = 0
        self.speaker_boxes = {}

        cocos.director.director.window.push_handlers(self)


    def on_key_press(self, key, modifiers):

        if mapKey(key) == pyglet.window.key.ENTER and self.dialog_layer.visible:
            print len(self.current_dialog), self.current_dialog_counter
            if len(self.current_dialog) > self.current_dialog_counter + 2:
                self.current_dialog_counter += 2
                self.dialog_line1.element.text = self.current_dialog[self.current_dialog_counter]
                for box in self.speaker_boxes:
                    self.speaker_boxes[box].visible = False
                self.speaker_boxes[self.current_dialog_speaker[self.current_dialog_counter]].visible = True

                if len(self.current_dialog) > self.current_dialog_counter:
                    self.dialog_line2.element.text = self.current_dialog[self.current_dialog_counter+1]

                if len(self.current_dialog) > self.current_dialog_counter + 2 and\
                   self.current_dialog_speaker[self.current_dialog_counter] == self.current_dialog_speaker[self.current_dialog_counter+2]:
                    self.dialog_arrow.visible = True
                else:
                    self.dialog_arrow.visible = False
            else:
                self.dialog_arrow.visible = False
                self.dialog_layer.visible = False



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

    def displayDialog(self):
        self.dialog_layer.visible = True
        diag = DIALOGS['Nod_Nel_B']

        self.current_dialog = []
        self.current_dialog_speaker = []
        self.current_dialog_counter = 0

        for d in diag:
            tokens = ['- '+d[0]+' -']
            tokens.extend(d[1].split())
            
            self.current_dialog.append(tokens[0])
            self.current_dialog_speaker.append(d[0])
            counter = 1
            while counter < len(tokens):
                line = ""    
                while len(line) + len(tokens[counter]) +1 < 36:
                    line += tokens[counter] + ' '
                    counter += 1
                    if counter == len(tokens):
                        break

                self.current_dialog.append(line)
                self.current_dialog_speaker.append(d[0])

            if (len(self.current_dialog) % 2 != 0):
                self.current_dialog.append('')
                self.current_dialog_speaker.append(d[0])

        self.speaker_boxes = {}
        for s in self.current_dialog_speaker:
            if s not in self.speaker_boxes:
                self.speaker_boxes[s] = cocos.sprite.Sprite(pyglet.image.load('img/chara/'+data.SPEAKERS[s]+'-b.png'), position=(50,90))
                self.dialog_layer.add(self.speaker_boxes[s], z =5   )
                self.speaker_boxes[s].visible = False

        self.dialog_line1.element.text = self.current_dialog[0]
        self.speaker_boxes[self.current_dialog_speaker[0]].visible = True
        if len(self.current_dialog) > 1:
            self.dialog_line2.element.text = self.current_dialog[1]
        if len(self.current_dialog) > 2 and self.current_dialog_speaker[0] == self.current_dialog_speaker[2]:
            self.dialog_arrow.visible = True