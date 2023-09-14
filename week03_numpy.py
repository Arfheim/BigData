import numpy as np
import random
import tkinter as tk #Built in GUI
from tkinter import messagebox #popup
def click_button():
    try:
        a = int(en_number.get())
        lst = [random.randint(1, 100) for i in range(a)]
        v = np.array(lst, dtype='int16')
        lbl_result.config(text=v)
    except ValueError as err :
        #lbl_result.config(text=f"입력된 값이 없습니다.\n{err}")
        messagebox.showerror('Error!',f"입력된 값이 없습니다.\n{err}")

window = tk.Tk()
window.title('numpy gui version v1.0')
window.geometry('300x150')
#create widget
lbl_result = tk.Label(text="random numpy array")
en_number = tk.Entry()
btn_click = tk.Button(text="click me", command=click_button)
#widget layout
# lbl_result.place(x=50,y=50)
# btn_click.place(x=0,y=0)
lbl_result.grid(row=0, column=0, columnspan=2)
en_number.grid(row=1, column=0)
btn_click.grid(row=1, column=1)


# lbl_result.pack(side='right')
# en_number.pack(side='right')
# btn_click.pack(side='right')


window.mainloop()

