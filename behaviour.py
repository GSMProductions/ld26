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
        # handle input and move the character
        self.target.velocity = ((KEYBOARD[key.RIGHT] - KEYBOARD[key.LEFT]) * 150,(KEYBOARD[key.UP] - KEYBOARD[key.DOWN]) * 150 )
        if self.target.current_map is not None:

            x = self.target.position[0] + self.target.velocity[0]*dt
            y = self.target.position[1] + self.target.velocity[1]*dt

            if self.target.velocity[0] < 0:
                x -= 12
            elif self.target.velocity[0] > 0:
                x += 12

            if self.target.velocity[1] < 0:
                y -= 0
            elif self.target.velocity[1] > 0:
                y += 16

            cell = self.target.current_map.map_layer.get_at_pixel(x,y)
            next_cell = None

            if cell is not None:
                if 'passable' in cell and cell['passable'] == 'True':
                    next_cell = cell

            cell = self.target.current_map.map_layer2.get_at_pixel(x,y)

            if cell is not None and cell.tile is not None:
                if not ('passable' in cell and cell['passable'] == 'True'):
                    next_cell = None            


            if next_cell is not None and 'passable' in next_cell and next_cell['passable'] == 'True':
                if 'door' in next_cell:
                    self.target.current_map = MAPS[next_cell['door_map']]
                    dest = next_cell['door_destination'].split()
                    dest = [int(dest[0]), int(dest[1])]
                    self.target.current_map.spawnPlayer(self.target, dest)
                self.target.map_position = [int(self.target.position[0]) / TILE_SIZE, int(self.target.position[1]) / TILE_SIZE]
                self.target.current_map.scroller.set_focus(self.target.position[0], self.target.position[1])
                self.target.battle_timer += dt
            else:
                # Nice to have : slider le long des murs
                self.target.velocity = (0,0)

        super(MoveCharacter, self).step(dt)
