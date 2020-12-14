import tkinter as tk
import emoji

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

buttonGame = tk.Button(Window, highlightbackground='#FFB6C1', text="game", font=40)
buttonGame.place(relx=0.52, rely=0.055, anchor='n')

# frame to displays messages
frame = tk.Frame(Window, bg='#80c1ff', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(frame)
label.place(relwidth=1, relheight=1)

# frame to type messages
lower_frame = tk.Frame(Window, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.1, anchor='n')

entryMsg = tk.Entry(lower_frame, font=40)
entryMsg.place(relwidth=0.75, relheight=1)
entryMsg.focus()

buttonMsg = tk.Button(lower_frame, text='send', font=40)
buttonMsg.place(relx=0.8, relheight=1, relwidth=0.2)

textCons = tk.Text(frame,
                   font="Helvetica 14")

textCons.place(relheight=1,
               relwidth=1,)

textCons.config(cursor="arrow")

# create a scroll bar
scrollbar = tk.Scrollbar(textCons)

# place the scroll bar
# into the gui window
scrollbar.place(relheight=1,
                relx=0.974)

scrollbar.config(command=textCons.yview)

textCons.config(state=tk.DISABLED)

Window.mainloop()
