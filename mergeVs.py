
from tkinter import*

import random 
from merge import merge_sort
import time

tk = Tk()
canvas = Canvas(tk , height = 700 , width = 1280 , bg = "lightblue" )
tk.title("System is Hacked!!!")
canvas.pack()

class Bar:
    b_h = 0
    def __init__(self ,x,y,a,b,col):
        self.bar = canvas.create_rectangle(x,y,a,b, fill = col)
        self.write  = canvas.create_text(x + 2 , y, anchor = SW , text = str(600-y) , fill = "red")
        self.b_h = y
    def move(self , take):
        canvas.move(self.bar, take , 0 )

n = 50
heightList = (list(random.sample(range(100,500), n)))

def draw(data , L , R):
    for k in range(n):
        col = "lightgreen"
        if k >= L and k <= R:
            col = "green"
        x = k * 20
        Bar(x   , data[k] , x + 15, 700 , col)
    tk.update()
def merge_sort(a , L , R , draw):
    if(L >= R):
        return
    m = (L + R) >> 1
    merge_sort(a , L , m , draw)
    merge_sort(a , m + 1, R , draw)
    merge(a , L , R , draw)
def merge(a , L , R , draw):
    canvas.delete("all")
    draw(a , L , R)
    time.sleep(0.1)
    M = (L + R) >> 1
    i = L 
    j = M + 1
    k = L
    temp = [0 for _ in range(100)]
    while i <= M and j <= R:
        if a[i] < a[j]:
            temp[k] = a[i]
            k += 1
            i += 1
        else:
            temp[k] = a[j]
            k += 1
            j += 1
    while i <= M:
        temp[k] = a[i]
        k += 1
        i += 1
    while j <= R:
        temp[k] = a[j]
        k += 1
        j += 1
    for i in range(L , R + 1):
        a[i] = temp[i]
    canvas.delete("all")
    draw(a , L , R)
    time.sleep(0.1)

merge_sort(heightList , 0 , len(heightList) - 1 , draw)
