# -*- coding: utf-8 -*-

MONSTERS =  {
             'fly':  {
                        'hp':5,
                        'xp':5,
                        'hit':5,
                        'triangles':1,
                        'circles':1,
                        'squares':0,
                        'halfsquares':0.3,
                        }
             'ogre':  {
                        'hp':35,
                        'xp':17,
                        'hit':7,
                        'triangles':1.5,
                        'circles':1,
                        'squares':0.3,
                        'halfsquares':1,
                        }
             'kraken':  {
                        'hp':50,
                        'xp':37,
                        'hit':12,
                        'triangles':1,
                        'circles':0.3,
                        'squares':1,
                        'halfsquares':1.5,
                        }
             'dragon':  {
                        'hp':100,
                        'xp':50,
                        'hit':25,
                        'triangles':0.3,
                        'circles':1.5,
                        'squares':1,
                        'halfsquares':1,
                        }
             'boss':  {
                        'hp':300,
                        'xp':150,
                        'hit':30,
                        'triangles':1,
                        'circles':1,
                        'squares':1,
                        'halfsquares':1,
                        }
            }

LEVELS = {
    
            1: {
                  'nextlevel':10,
                  'hp':15,
                  'mp':15,
                  'hit':6,
                  'heal':0,
                  'triangles':0,
                  'circles':0,
                  'squares':0,
                  'halfsquares':0,
                  'life':0,
                  }
            2: {
                  'nextlevel':20,
                  'hp':17,
                  'mp':17,
                  'hit':11,
                  'heal':6,
                  'triangles':11,
                  'circles':0,
                  'squares':0,
                  'halfsquares':0,
                  'life':0,
                  }
            3: {
                  'nextlevel':25,
                  'hp':20,
                  'mp':20,
                  'hit':17,
                  'heal':7,
                  'triangles':17,
                  'circles':0,
                  'squares':0,
                  'halfsquares':0,
                  'life':0,
                  }
            4: {
                  'nextlevel':30,
                  'hp':25,
                  'mp':25,
                  'hit':25,
                  'heal':9,
                  'triangles':25,
                  'circles':30,
                  'squares':30,
                  'halfsquares':0,
                  'life':0,
                  }
            5: {
                  'nextlevel':35,
                  'hp':32,
                  'mp':32,
                  'hit':33,
                  'heal':11,
                  'triangles':33,
                  'circles':40,
                  'squares':40,
                  'halfsquares':0,
                  'life':0,
                  }
            6: {
                  'nextlevel':40,
                  'hp':41,
                  'mp':41,
                  'hit':40,
                  'heal':14,
                  'triangles':40,
                  'circles':48,
                  'squares':48,
                  'halfsquares':60,
                  'life':0,
                  }
            7: {
                  'nextlevel':45,
                  'hp':52,
                  'mp':52,
                  'hit':47,
                  'heal':18,
                  'triangles':47,
                  'circles':56,
                  'squares':56,
                  'halfsquares':71,
                  'life':0,
                  }
            8: {
                  'nextlevel':50,
                  'hp':66,
                  'mp':66,
                  'hit':55,
                  'heal':23,
                  'triangles':55,
                  'circles':66,
                  'squares':66,
                  'halfsquares':83,
                  'life':46,
                  }
            9: {
                  'nextlevel':55,
                  'hp':81,
                  'mp':81,
                  'hit':64,
                  'heal':28,
                  'triangles':64,
                  'circles':77,
                  'squares':77,
                  'halfsquares':96,
                  'life':56,
                  }
            10: {
                  'nextlevel':None,
                  'hp':99,
                  'mp':99,
                  'hit':73,
                  'heal':35,
                  'triangles':73,
                  'circles':88,
                  'squares':88,
                  'halfsquares':110,
                  'life':70,
                  }
}