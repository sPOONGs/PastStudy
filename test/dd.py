# import tkinter
# import tkinter.messagebox

# key = ""
# def key_down(e):
#     global key
#     key = e.keysym
# def key_up(e):
#     global key
#     key = ""
    
# mx = 1
# my = 1
# yuka = 0
# def main_proc():
#     global mx, my , yuka
#     if key == "Shift_L" and yuka > 1:
#         canvas.delete("PAINT")
#         mx = 1
#         my = 1
#         yuka = 0
#         for y in range(7):
#             for x in range(10):
#                 if maze[y][x] == 2:
#                     maze[y][x] = 0
#     if key == "Up" and maze[my - 1][mx] == 0:
#         my = my - 1
#     if key == "Down" and maze[my + 1][mx] == 0:
#         my = my + 1
#     if key == "Left" and maze[my][mx - 1] == 0:
#         mx = mx - 1
#     if key == "Right" and maze[my][mx + 1] == 0:
#         mx = mx + 1
#     if maze[my][mx] == 0:
#         maze[my][mx] = 2
#         yuka = yuka + 1
#         canvas.create_rectangle(mx * 80, my * 80, mx * 80 + 79, my * 80 + 79, fill="pink", width=0, tag="PAINT")
#         canvas.delete("MYCHR")
#         canvas.create_image(mx * 80 + 40, my * 80 + 40, image = img, tag="MYCHR")
#     if yuka == 30:
#         canvas.update()
#         tkinter.messagebox.showinfo("Good", "You Win!")
#     else:
#         root.after(300, main_proc)
    
# root = tkinter.Tk()
# root.title("coloring maze")
# root.bind("<KeyPress>", key_down)
# root.bind("<KeyRelease>", key_up)
# canvas = tkinter.Canvas(width=800, height=560, bg="white")
# canvas.pack()

# maze = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#     ]
# for y in range(7):
#     for x in range(10):
#         if maze[y][x] == 1:
#             canvas.create_rectangle(x * 80, y * 80, x * 80 + 79, y * 80 + 79, fill="skyblue", width = 0)
            
# img = tkinter.PhotoImage(file="cat.png")
# canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag="MYCHR")
# main_proc()
# root.mainloop()


import tkinter
import random

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y
    
def mouse_press(e):
    global mouse_c
    mouse_c = 1
    
neko = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x * 72 + 60, y * 72 + 60, image = img_neko[neko[y][x]],tag="NEKO")
                
def drop_neko():
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y][x] != 0 and neko[y + 1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0

def game_main():
    global cursor_x, cursor_y, mouse_c
    drop_neko()
    if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
        cursor_x = int((mouse_x - 24) / 72)
        cursor_y = int((mouse_y - 24) / 72)
        if mouse_c == 1:
            mouse_c = 0