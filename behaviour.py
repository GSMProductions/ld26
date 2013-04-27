import cocos
from pyglet.window import key
from data import KEYBOARD, TILE_SIZE


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

            next_cell = self.target.current_map.map_layer.get_at_pixel(x,y)
            if next_cell is not None and next_cell['passable'] == 'True':
                self.target.map_position = [int(self.target.position[0]) / TILE_SIZE, int(self.target.position[1]) / TILE_SIZE]
                self.target.current_map.scroller.set_focus(self.target.position[0], self.target.position[1])
            else:
                # Nice to have : slider le long des murs
                self.target.velocity = (0,0)

        super(MoveCharacter, self).step(dt)
