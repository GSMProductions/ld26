import cocos
from pyglet.window import key
from data import KEYBOARD, TILE_SIZE


class MoveCharacter(cocos.actions.Move):
    def step(self, dt):
        # handle input and move the character
        self.target.velocity = ((KEYBOARD[key.RIGHT] - KEYBOARD[key.LEFT]) * 150,(KEYBOARD[key.UP] - KEYBOARD[key.DOWN]) * 150 )
        if self.target.current_map is not None:

            self.target.map_position = [self.target.position[0] / TILE_SIZE, self.target.position[1] / TILE_SIZE]
            self.target.current_map.scroller.set_focus(self.target.map_position[0]*TILE_SIZE, self.target.map_position[1]*TILE_SIZE)


        super(MoveCharacter, self).step(dt)
