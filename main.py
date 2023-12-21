import tkinter as tk
from tkinter import PhotoImage

app = tk.Tk()
app.title("Wanted!")
app.configure(bg="#FBFBD0")

wanted_text = tk.Label(app, text="WANTED", font=("Times New Roman", 50))
wanted_text.pack()

cat_image = PhotoImage(file="./image/1.jpg")
cat = tk.Label(app, image=cat_image)
cat.pack()

app.mainloop()
