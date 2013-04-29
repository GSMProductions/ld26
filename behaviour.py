import cocos
from pyglet.window import key
from data import KEYBOARD, TILE_SIZE, MAPS, TRIGGERS
import random
from sprite import Character
import time
from fightScene import FightScene
from battle_data import HOOK




class CheckForBattle(cocos.actions.Action):

    zone = 'prairie'

    def step(self, dt):

        if self.target.battle_timer >= self.target.battle_threshold:
            self.target.battle_timer = 0.0
            self.battle_threshold = random.randint(10,15)
            
            # START THE BATTLE
            heros = [self.target, HOOK['NED']]
            sf = FightScene(self.zone,heros)
            sf = cocos.scenes.transitions.ZoomTransition(sf)
            cocos.director.director.push(sf)

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

            if TRIGGERS['found_nel'] and TRIGGERS['village_state'] == 1:
                TRIGGERS['village_state'] = 2
                self.target.current_map.char_layer.remove(self.target.current_map.npcs['nel11'])
                self.target.current_map.npcs.pop('nel11')
                self.target.current_map.npcs['villagera4'].do(cocos.actions.interval_actions.MoveBy((-1000,0),5))

            if TRIGGERS['village_state'] == 3 and self.target.current_map.name == 'inside_ceremony_hall':
                thewise = Character('n_the_wise',(0,0))
                self.target.current_map.placeCharacter(thewise, (13,2))
                thewise.do(cocos.actions.interval_actions.MoveBy((0,256),3))
                self.target.current_map.displayDialog('N_friends_Wise_A')
                TRIGGERS['village_state'] = 4


            if TRIGGERS['village_state'] == 10:
                self.target.current_map.displayDialog('Nod_Nel_D')
                TRIGGERS['village_state'] = 11


            if TRIGGERS['village_state'] == 9:
                self.target.current_map = MAPS['village3']
                self.target.current_map.spawnPlayer(self.target, (6,9))
                TRIGGERS['village_state'] = 10                


            if TRIGGERS['village_state'] == 8:
                self.target.current_map.displayDialog('Ellipse')
                TRIGGERS['village_state'] = 9


            if TRIGGERS['village_state'] == 7:
                self.target.current_map = MAPS['inside_house_nod']
                self.target.current_map.spawnPlayer(self.target, (5,8))
                TRIGGERS['village_state'] = 8


            if TRIGGERS['village_state'] == 6:
                self.target.current_map.displayDialog('Nod_Nel_C')
                TRIGGERS['village_state'] = 7

            if TRIGGERS['village_state'] == 5:
                self.target.current_map = MAPS['village2']
                self.target.current_map.spawnPlayer(self.target, (24,16))
                TRIGGERS['village_state'] = 6

            if TRIGGERS['village_state'] == 4 and self.target.current_map.name == 'village':
                self.target.current_map.displayDialog('Nod_Nel_B')
                TRIGGERS['village_state'] = 5

            for npc in self.target.current_map.npcs:
                if player_rect.intersects(self.target.current_map.npcs[npc].get_rect()):
                    self.target.velocity = (0,0)
                    self.target.in_dialog = True

                    if TRIGGERS['village_state'] == 1 and not TRIGGERS['found_nel']:
                        print 'Name', self.target.current_map.npcs[npc].name
                        if self.target.current_map.npcs[npc].name == 'nel11':
                            self.target.current_map.displayDialog('Nod_Nel_A')
                            TRIGGERS['found_nel'] = True
                        else:
                            self.target.current_map.displayDialog('Villageois_A')
                    elif TRIGGERS['village_state'] == 2:
                        if self.target.current_map.name == 'inside_ceremony_hall':
                            self.target.current_map.displayDialog('N_friends_A')
                            TRIGGERS['village_state'] = 3
                        else:
                            self.target.current_map.displayDialog('Villageois_B')


            for item in self.target.current_map.items:
                if player_rect.intersects(self.target.current_map.items[item].get_rect()):
                    print "ITEMY!"

        super(MoveCharacter, self).step(dt)
