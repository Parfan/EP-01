# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:12:56 2019

@author: kenzo
"""
class Item:
    
class ChaveMestra(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Chave Mestra",
                         description="Uma chave mestra que dá acesso a todas as salas da insper.".format(str(self.amt)),
                         value=self.amt)
class Weapon:
    def __str__(self):
        return self.name
    
class Atestado(Weapon):
    def __init__(self):
        super().__init__(name="Atestado",
                         description="Atestado médico para os professors ficarem com pena de voce",
                         value=10, 
                         damage=10)

class Gripe(Weapon):
      def __init__(self):
        super().__init__(name="Gripe"
                         description="Dá uma desculpa que voce está doente",
                         value=10, 
                         damage=4)a