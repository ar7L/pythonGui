from  tkinter import *
import random
import time

tk = Tk()
canvas = Canvas(tk , width = 400 , height = 500, bg = "lightblue")
tk.title("Drawing")
canvas.pack()

class Bar:
    b_h = 0
    def __init__(self ,x,y,a,b):
        self.bar = canvas.create_rectangle(x,y,a,b, fill = "green")
        self.b_h = y
    def move(self , take):
        canvas.move(self.bar, take , 0 )
n = 30
heightList = (list(random.sample(range(100,400), n)))

def swap(i , j , a = []):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    

bars = []
def draw(data):
    for k in range(n):
        x = k * 10
        Bar(x , data[k] , x + 12, 500)
    tk.update()
draw(heightList)

for i in range(n - 1):
    for j in range(n - 1):
        if heightList[j] > heightList[j + 1]:
           heightList[j] , heightList[j + 1] = heightList[j + 1] , heightList[j]
           canvas.delete("all")
           draw(heightList)
           time.sleep(00.1)
print(heightList)            


tk.mainloop()

