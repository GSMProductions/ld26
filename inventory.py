# -*- coding: utf-8 -*-
import cocos
import pyglet


class Inventory(dict):

    def add(self, obj):
        
        if self.has_key(obj):
            self[obj] += 1

        else:
            self[obj] = 1

    def remove(self,obj):

        if self.has_key(obj):
            self[obj] -= 1
            if self[obj] <= 0:
                self.pop(obj)



