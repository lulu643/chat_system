import tkinter as tk
import time

# to show chat window
Window = tk.Tk()
Window.title("CHATROOM")

# add canvas
canvas = tk.Canvas(Window, height=500, width=600)
canvas.pack()

# add background image onto canvas
background_image = tk.PhotoImage(file='/Users/nyu/Desktop/ics_project/images/landscape.png')
background_label = tk.Label(Window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# text menu
menu_canvas = tk.Canvas(Window)
menu_canvas.create_text((250, 200), anchor='n')
canvas.itemconfig(menu_canvas, text='menu', font="Helvetica 50 bold")

# frame to type messages
lower_frame = tk.Frame(Window, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.1, anchor='n')

entryMsg = tk.Entry(lower_frame, font=40)
entryMsg.place(relwidth=0.75, relheight=1)
entryMsg.focus()

buttonMsg = tk.Button(lower_frame, text='send', font=40)
buttonMsg.place(relx=0.8, relheight=1, relwidth=0.2)

Window.mainloop()