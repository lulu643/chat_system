import tkinter as tk

HEIGHT = 500
WIDTH = 500


def get_weather(city):
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)

def create_interface():
    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='images/2.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)

    button = tk.Button(frame, text="SEND", font=40, command=lambda: get_weather(entry.get()))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame)
    label.place(relwidth=1, relheight=1)

    root.mainloop()
