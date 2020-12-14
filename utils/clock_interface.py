import time
import tkinter as tk


def clock():
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    second = time.strftime('%S')

    clock_label.config(text=f'{hour}:{minute}:{second} ')
    clock_label.after(1000, clock)


Window = tk.Tk()
clock_label = tk.Label(Window, text='', font=('Helvetica', 18))
clock_label.pack(pady=10)

clock()
Window.mainloop()
