import numpy as np


stuff = ['c',5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F"]

if type(stuff[0]) is str:   #type(stuff[0]) geeft het datatype van het eerste item in de list 
    print("string found")

pizza = [i for i in range(10)]

if list(range(10)):
    print("pizza")

ijs = [i for i in np.arange(2,8,0.5)]

if list(np.arange(2,8,0.5)):
    print("haha gevint")

guhbean =  [True for i in range(6)]

if list(str(guhbean)):
    print("boing!")
