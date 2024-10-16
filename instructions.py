from tkinter import *
from tkinter import ttk

class Inst:
    def __init__(self) -> None:
        info = Tk()
        
        Label(info, text="1) Натисність на кнопку обрати файл", font="30").grid(row=0, column=0, padx=10, pady=10)
        Label(info, text="2) Оберіть потрібний файл", font="30").grid(row=1, column=0, padx=10, pady=10)
        Label(info, text="3) Далі программа все зробить за вас", font="30").grid(row=2, column=0, padx=10, pady=10)
        
        Button(info, text="Зачинити", width=50, command=info.destroy).grid(row=3, column=0, padx=10, pady=10)