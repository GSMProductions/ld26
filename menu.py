import cocos


class Menu(cocos.menu.Menu):

    def __init__(self,commands):

        cocos.menu.Menu.__init__(self)

        self.font_item['font_name'] = 'Statix'            
        self.font_item['font_size'] = 50
        self.font_item_selected['font_name'] = 'Statix' 
        self.font_item_selected['font_size'] = 50  
        self.menu_valign = cocos.menu.BOTTOM
        self.menu_halign = cocos.menu.CENTER
        self.y += 100

        l = []

        for cmd in commands:
            l.append(cocos.menu.MenuItem(cmd[0], cmd[1],*cmd[2]))

        self.create_menu(l, None, None)

    def on_quit(self):
              pass