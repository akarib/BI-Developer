import tkinter

app = tkinter.Tk()

Label = tkinter.Label(app, text="Bienvenu")

Label.config(text="New msg")

Label.pack()
app.mainloop()