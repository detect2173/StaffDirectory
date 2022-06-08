from tkinter import *
from tkinter import ttk

#create main window
root = Tk()
root.title('Northlands JCC Staff Directory')
root.geometry('650x400')
root.resizable(height=False, width=False)
#create frame
frame = Frame(root)
frame.grid(row=0, column=0,padx=10, pady=10, sticky=('N, E, S, W'))
title_label = ttk.Label(frame,text='Northlands JCC Staff Directory', font=('Segoe UI', 22))
title_label.grid(row=0, column=1,columnspan=4,pady=20, sticky='EW')
name_label = ttk.Label(frame, text='Name:', font=('Segoe UI', 14))
name_label.grid(row=1, column=0, padx=5, pady=5, sticky='EW')
name_cmb = ttk.Combobox(frame, font=('Segoe UI', 14))
name_cmb.grid(row=1, column=1,padx=5,pady=5, sticky='EW')
pos_label = ttk.Label(frame, text='Position:', font=('Segoe UI', 14))
pos_label.grid(row=1, column=2, padx=5, pady=5, sticky='EW')
pos_entry = ttk.Entry(frame,font=('Segoe UI', 14) )
pos_entry.grid(row=1, column=3,padx=5,pady=5, sticky='EW')
ext_label = ttk.Label(frame, text='Ext: 174+', font=('Segoe UI', 14))
ext_label.grid(row=2, column=0, padx=5, pady=5, sticky='EW')
ext_entry = ttk.Entry(frame,font=('Segoe UI', 14) )
ext_entry.grid(row=2, column=1,padx=5,pady=5, sticky='EW')



root.mainloop()