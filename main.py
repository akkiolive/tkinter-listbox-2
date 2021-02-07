import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import ttk
import tkinter as tk

# root window
root = tk.Tk()
root.title("Plot Analysis")
root.geometry("1000x800")



pw = tk.PanedWindow(root, orient="horizontal", sashwidth=4, sashrelief="sunken")
pw.pack(expand=True, fill="both")
pw2 = tk.PanedWindow(pw, orient="vertical", sashwidth=4, sashrelief="sunken")

frame1 = tk.Frame(pw2)
class search_box_input:
    def __init__(self):
        self.frame = tk.Frame(frame1)
        self.entry = ttk.Entry(self.frame)
        self.entry.grid(row=0, column=0)
        self.button = ttk.Button(self.frame, text="Clear")
        self.button.grid(row=0, column=1)
        self.frame.pack()
search_box_input()

class signal_all_listbox:
    def __init__(self):
        self.frame = tk.LabelFrame(frame1, text="All signals")
        self.txt = tk.StringVar(value=["initialize..."])
        self.dict = {}
        self.lb = tk.Listbox(self.frame, listvariable=self.txt, height=20, selectmode="extended")
        self.lb.bind('<<ListboxSelect>>', self.select_now)
        self.lb.pack(expand=True, fill="both")
        self.sb = ttk.Scrollbar(self.lb, orient=tk.VERTICAL, command=self.lb.yview)
        self.lb["yscrollcommand"] = self.sb.set
        self.sb.pack(side=tk.RIGHT,  fill="y")
        self.frame.pack(expand=True, fill="both")
    
    def select_now(self, event):
        for i in self.lb.curselection(): #現在選択されている項目を取得
            print(str(i)+'番目を選択中')

    def set_row(self, _list):
        self.lb.delete(0, "end")
        self.txt = tk.StringVar(value=_list)
        self.dict = {}
        for i, v in enumerate(_list):
            self.add_row(v)
            self.dict[v] = i

        
    def add_row(self, str):
        self.lb.insert(tk.END, str)

    def remove_str(self, str):
        self.txt = self.lb.get(0, "end")
        removed_idx = []
        for i, t in enumerate(self.txt):
            if t == str:
                self.lb.delete(i)
                removed_idx.append(i)
        self.txt = self.lb.get(0, "end")
        self.dict = {}
        for i, v in enumerate(self.txt):
            self.dict[v] = i
        return removed_idx
    
    def set_color(self, _str, color):
        if _str not in self.dict:
            return False
        else:
            i = self.dict[_str]
            self.lb.itemconfig(i, background=color)

sai = signal_all_listbox()


frame2 = tk.Frame(pw2)


frame3 = tk.Frame(pw)
class matplot_frame:
    def __init__(self):
        self.upper_frame = tk.Frame(frame3)
        self.button1 = tk.Button(self.upper_frame, text="upp")
        self.button1.pack(side=tk.TOP)
        self.upper_frame.pack(side=tk.RIGHT, fill="y")
        self.frame = tk.Frame(frame3)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
        self.ax.plot([1,2,4,5], [4,5,6,7])
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=True, fill="both")
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

matplot_frame()



# ペインドウィンドウに追加
pw2.add(frame1)
pw2.add(frame2)

pw.add(pw2)
pw.add(frame3)


root.mainloop()


