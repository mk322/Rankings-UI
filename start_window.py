from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sys

class legend_window:
    def __init__(self, dict, gui) -> None:
        self.gui = gui
        self.root2 = Tk()
        self.root2.title('Legend Window for Rankings UI')
        self.root2.geometry('700x500+100+150')
        
        self.dict = dict
        self.graph_attr = list(dict.keys())
        self.ratings = list(dict.values()) + ["None"]
        self.ratings.remove("Overall Score")
        self.var_list = []
        
        for i in range(1, len(self.graph_attr)):
            tkvarq = StringVar(self.root2)
            tkvarq.set("Please Select a Rating")
            self.var_list.append(tkvarq)
            self.create_wigets(self.graph_attr[i], i-1)

        submit_button = Button(self.root2, text="Submit and Reopen the Main Window", command=self.return_pairs)
        paddings = {'padx': 5, 'pady': 5}
        submit_button.grid(column=1, row=len(self.graph_attr))
        #Answer entry
        #answer_entry = Entry(root, width=30)
        #answer_entry.pack()

        
    def create_wigets(self, ga, order):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self.root2, text=f'Please Select the Rating Displayed by the Graphical Attribute of {ga}:')
        label.grid(column=0, row=order, sticky=tk.W, **paddings)
        #if order != 0:
        # option menu
        option_menu = ttk.OptionMenu(
            self.root2,
            self.var_list[order],
            self.dict[ga],
            *self.ratings)
        #else:
            #option_menu = ttk.OptionMenu(
                #self.root2,
                #self.var_list[order],
                #self.dict[ga],
                #*[self.dict[ga]])

        option_menu.grid(column=1, row=order, sticky=tk.W, **paddings)

    def return_pairs(self):
        self.result = {}
        pairs = list(i.get() for i in self.var_list if i.get() != "None")
        #if len(set(pairs)) == len(pairs):
        for i in range(len(self.var_list)):
            self.result[self.graph_attr[i+1]] = self.var_list[i].get()
        self.gui.update_all_rects(self.result)
        self.root2.destroy()
        #else:
            #messagebox.showerror(title="Illegal Matching", message="Please Make Sure to Assign every Rating to Only One Graphical Attribute.")        
    
    def show(self):
        self.root2.mainloop()

    def get_pair(self):
        return self.result
