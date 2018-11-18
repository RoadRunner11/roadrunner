# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 08:4=7:22 2018

@author: E
"""
with open('myfile.txt', "r") as flobj:
    print(flobj.read()
dict = {"name":'Olawale', 'city':'Modakeke', 'school':'Oau'}    
dict.items()

class Name():
    def __init__(self, first, last, other):
        self.first = first
        self.last = last
        self.other = other
    def __repr__(self):
        return 'i love girls'
    
detail = Name('Akorede', 'Fodilu', 'Olawale')
print(detail)