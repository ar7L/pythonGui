from tkinter import*
import random 
import time

tk = Tk()
canvas = Canvas(tk , height = 600 , width = 800 , bg = "lightblue" )
tk.title("System is Hacked! again!!")
canvas.pack()

def Draw(data , col):
    can_height = 600
    can_width = 800
    x_width = can_width / (len(data) + 1)
    offset = 20
    spacing = 10
    normalize = [i / max(data) for i in data]
    for i , height in enumerate(normalize):
        x0 = i * x_width + offset + spacing
        y0 = can_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = can_height
        canvas.create_rectangle(x0 , y0 , x1 , y1, fill =  col[i])
        canvas.create_text(x0 + 2 , y0 , anchor = SW, text=str(data[i]))
    tk.update()


n = 30
heightList = list(random.sample(range(0, 600),n))
colors = ["red" for _ in range(30)]
color= ["green" for _ in range(30)]
def merge_sort(a , L , R , Draw):
    if(L >= R):
        return
    m = (L + R) >> 1
    merge_sort(a , L , m , Draw)
    merge_sort(a , m + 1, R , Draw)
    merge(a , L , R , Draw)
def merge(a , L , R , Draw):
    #canvas.delete("all")
    Draw(a , colors)
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
    #canvas.delete("all")
    Draw(a , ["green" if x >= L and x <= R else "white" for x in range(30)])
    time.sleep(0.1)

merge_sort(heightList , 0 , len(heightList) - 1 , Draw)
