from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from instructions import Inst
from logics import Logics

class MainWindow:
    def __init__(self) -> None:
        self.root = Tk()
        frm = ttk.Frame(self.root, padding=10)
        frm.grid
        
        ttk.Label(text="Варіант 2", font="30").grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(text="Обрати файл", width=50, command=self.handler).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(text="Інструкція", width=50, command=self.call_instructions).grid(row=2, column=0, padx=10, pady=10)
    
    def run(self):
        self.root.mainloop()
    
    def handler(self):
        self.file_path = filedialog.askopenfilename(
                title="Выберите файл",
                filetypes=[("Exel", "*.xlsx"), ("Все файлы", "*.*")]
            )
        
        self.control = Logics(self.file_path)
        self.control.read_data()
        self.control.draw_graph()
        self.draw_data()
        
    def call_instructions(self):
        Inst()
        
    def draw_data(self):
        data = self.control.calculations()
        info = Tk()
        
        Label(info, text=f"K: {data[0]}", font="30").grid(row=0, column=0, padx=10, pady=10)
        Label(info, text=f"Значення розрахунку для пошуку T: {data[1]}", font="30").grid(row=1 ,column=0, padx=10, pady=10)
        Label(info, text=f"T: {data[-1]}", font="30").grid(row=2, column=0, padx=10, pady=10)
        
        Button(info, text="Вийти", width=50, command=info.destroy).grid(row=3, column=0, padx=10, pady=10)