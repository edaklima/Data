import tkinter
import keyboard

canvas = tkinter.Canvas()
canvas.pack()

#up = input("Zadej text: ")

canvas.create_line(15, 20, 50, 100)

if keyboard.is_pressed('a'):
    print ("KURVA HURA")


#if up == "a":
#    canvas.create_rectangle(100, 150, 200, 100)

#print (up)

canvas.mainloop()
