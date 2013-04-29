import cocos
from pyglet.window import key
from data import KEYBOARD, TILE_SIZE, MAPS
import random

class CheckForBattle(cocos.actions.Action):
    def step(self, dt):

        if self.target.battle_timer >= self.target.battle_threshold:
            self.target.battle_timer = 0.0
            self.battle_threshold = random.randint(10,15)
            print "BATTLE !"
            pass
            # START THE BATTLE


class MoveCharacter(cocos.actions.Move):
    def step(self, dt):

        if self.target.current_map.timer < 2.0:
            self.target.visible = False
            self.target.current_map.timer += dt
            return
        else:
            self.target.visible = True

        # handle input and move the character
        if self.target.current_map.dialog_layer.visible == True:
            return
        self.target.velocity = ((KEYBOARD[key.RIGHT] - KEYBOARD[key.LEFT]) * 150,(KEYBOARD[key.UP] - KEYBOARD[key.DOWN]) * 150 )
        if self.target.current_map is not None:

            x0 = self.target.position[0]
            y0 = self.target.position[1]

            x = self.target.position[0] + self.target.velocity[0]*dt
            y = self.target.position[1] + self.target.velocity[1]*dt

            #rect = cocos.rect.Rect(x-12, y, 24, 16)
            rect_x = cocos.rect.Rect(x-12, y0, 24,16)
            rect_y = cocos.rect.Rect(x0-12, y, 24,16)

            for i in range(int(x/TILE_SIZE)-1,int(x/TILE_SIZE)+2):
                for j in range(int(y/TILE_SIZE)-1, int(y/TILE_SIZE)+2):
                    cell = self.target.current_map.map_layer.get_cell(i,j)
                    cell2 = self.target.current_map.map_layer2.get_cell(i,j)

                    if cell is not None:
                        if cell.intersects(rect_x):
                            if cell is not None and 'passable' in cell and cell['passable'] == 'True':
                                if cell2 is not None and 'passable' in cell2 and cell2['passable'] == 'True':
                                    pass
                                else:
                                    self.target.velocity = (0,self.target.velocity[1])
                            else:
                                self.target.velocity = (0,self.target.velocity[1])
                        
                        if cell.intersects(rect_y):
                            if cell is not None and 'passable' in cell and cell['passable'] == 'True':
                                if cell2 is not None and 'passable' in cell2 and cell2['passable'] == 'True':
                                    pass
                                else:
                                    self.target.velocity = (self.target.velocity[0],0)
                            else:
                                self.target.velocity = (self.target.velocity[0],0)

            if self.target.velocity != (0,0):
                self.target.map_position = [int(self.target.position[0]) / TILE_SIZE, int(self.target.position[1]) / TILE_SIZE]
                self.target.current_map.scroller.set_focus(self.target.position[0], self.target.position[1])
                self.target.battle_timer += dt

                cell = self.target.current_map.map_layer2.get_cell(self.target.map_position[0],self.target.map_position[1])
                if 'door' in cell:
                    self.target.current_map = MAPS[cell['door_map']]
                    dest = cell['door_destination'].split()
                    dest = [int(dest[0]), int(dest[1])]
                    self.target.current_map.spawnPlayer(self.target, dest)
            #    
            # if next_cell is not None and 'passable' in next_cell and next_cell['passable'] == 'True':
            #     if 'door' in next_cell:
            #         self.target.current_map = MAPS[next_cell['door_map']]
            #         dest = next_cell['door_destination'].split()
            #         dest = [int(dest[0]), int(dest[1])]
            #         self.target.current_map.spawnPlayer(self.target, dest)
            #     self.target.map_position = [int(self.target.position[0]) / TILE_SIZE, int(self.target.position[1]) / TILE_SIZE]
            #     self.target.current_map.scroller.set_focus(self.target.position[0], self.target.position[1])
            #     self.target.battle_timer += dt
            # else:
            #     # Nice to have : slider le long des murs
            #     self.target.velocity = (0,0)


            player_rect = self.target.get_rect()
            player_rect.x += self.target.velocity[0]*dt
            player_rect.y += self.target.velocity[1]*dt

            for npc in self.target.current_map.npcs:
                if player_rect.intersects(self.target.current_map.npcs[npc].get_rect()):
                    self.target.velocity = (0,0)
                    self.target.in_dialog = True
                    #self.target.current_map.displayDialog()

            for item in self.target.current_map.items:
                if player_rect.intersects(self.target.current_map.items[item].get_rect()):
                    print "ITEMY!"

        super(MoveCharacter, self).step(dt)
