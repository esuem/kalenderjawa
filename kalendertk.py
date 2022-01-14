#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date
#from tkinter import filedialog

import kalender as kal


def f_b1():
    try:
        y, m, d  = int(e11.get()), int(e12.get()), int(e13.get())
        x = kal.masehi(y, m, d)
        l11['text'] = x.tglmasehi(wuku=True)
        l12['text'] = "{} (neptu: {} + {} = {})".format(x.tgljawa(weton=False, windu=False), 
            x.neptu(7), x.neptu(5), x.neptu(35))
        l13['text'] = x.tgljawa(weton=False, tanggal=False, windu=True)
        l14['text'] = x.mangsa()
    except Exception:
        messagebox.showerror('Kesalahan!', 'Cek input anda!')


def f_b2():
    try:
        y, m, d  = int(e21.get()), int(e22.get()), int(e23.get())
        x = kal.jawa(y, m, d)
        l21['text'] = x.tglmasehi(wuku=True)
        l22['text'] = "{} (neptu: {} + {} = {})".format(x.tgljawa(weton=False, windu=False), 
            x.neptu(7), x.neptu(5), x.neptu(35))
        l23['text'] = x.tgljawa(weton=False, tanggal=False, windu=True)
        l24['text'] = x.mangsa()
    except Exception:
        messagebox.showerror('Kesalahan!', 'Cek input anda!')


def f_b3():
    try:
        y, m, d  = int(e31.get()), int(e32.get()), int(e33.get())
        x = kal.masehi(y, m, d)
        l31['text'] = x.tglmasehi(wuku=False)
        l32['text'] = x.pendhak(dina=5)
        l33['text'] = x.pendhak(dina=35)
        l34['text'] = x.pendhak(dina=245)
    except Exception:
        messagebox.showerror('Kesalahan!', 'Cek input anda!')


def f_b4():
    try:
        y, m, d  = int(e41.get()), int(e42.get()), int(e43.get())
        x = kal.masehi(y, m, d)
        l41['text'] = x.tglmasehi(wuku=False)
        l42['text'] = x.pendhak(dina=3, pati=True)
        l43['text'] = x.pendhak(dina=7, pati=True)
        l44['text'] = x.pendhak(dina=40, pati=True)
        l45['text'] = x.pendhak(dina=100, pati=True)
        l46['text'] = x.pendhak(taun=1, pati=True)
        l47['text'] = x.pendhak(taun=2, pati=True)
        l48['text'] = x.pendhak(dina=1000, pati=True)
    except Exception:
        messagebox.showerror('Kesalahan!', 'Cek input anda!')

today = date.today()


###------MAIN WINDOW------###


# Make Widget
root = tk.Tk()
root.title('Kalender Jawa')

# Make main window
main = ttk.Notebook(root)
main.pack()

# Make 1st Tab
tab1 = tk.Frame(main)
main.add(tab1, text="Tanggal Masehi")

v11 = tk.IntVar()
v11.set(today.year)
e11 = tk.Entry(tab1, text=v11, width=16)
e11.grid(column=3, row=0)
v12 = tk.IntVar()
v12.set(today.month)
e12 = tk.Entry(tab1, text=v12, width=8)
e12.grid(column=2, row=0)
v13 = tk.IntVar()
v13.set(today.day)
e13 = tk.Entry(tab1, text =v13, width=8)
e13.grid(column=1, row=0)

b11 = tk.Button(tab1, command=f_b1, text = "          Hitung!          ")
b11.grid(row=1, columnspan=5)

l10 =tk.Label(tab1, text='Tanggal:', width=12)
l10.grid(row=0, column=0)
l11 = tk.Label(tab1)
l11.grid(row=2, columnspan=5)
l12 = tk.Label(tab1)
l12.grid(row=3, columnspan=5)
l13 = tk.Label(tab1)
l13.grid(row=4, columnspan=5)
l14 = tk.Label(tab1)
l14.grid(row=5, columnspan=5)


# Make 2nd Tab
tab2 = tk.Frame(main)
main.add(tab2, text="Tanggal Jawa")

v21 = tk.IntVar()
v21.set(1924)
e21 = tk.Entry(tab2, text=v21, width=16)
e21.grid(column=3, row=0)
v22 = tk.IntVar()
v22.set(12)
e22 = tk.Entry(tab2, text=v22, width=8)
e22.grid(column=2, row=0)
v23 = tk.IntVar()
v23.set(15)
e23 = tk.Entry(tab2, text =v23, width=8)
e23.grid(column=1, row=0)

b21 = tk.Button(tab2, command=f_b2, text = "          Hitung!          ")
b21.grid(row=1, columnspan=5)

l20 =tk.Label(tab2, text='Tanggal:', width=12)
l20.grid(row=0, column=0)
l21 = tk.Label(tab2)
l21.grid(row=2, columnspan=5)
l22 = tk.Label(tab2)
l22.grid(row=3, columnspan=5)
l23 = tk.Label(tab2)
l23.grid(row=4, columnspan=5)
l24 = tk.Label(tab2)
l24.grid(row=5, columnspan=5)


# Make 3rd Tab
tab3 =tk.Frame(main)
main.add(tab3, text="Kelahiran")

v31 = tk.IntVar()
v31.set(2021)
e31 = tk.Entry(tab3, text=v31, width=16)
e31.grid(column=3, row=0)
v32 = tk.IntVar()
v32.set(9)
e32 = tk.Entry(tab3, text=v32, width=8)
e32.grid(column=2, row=0)
v33 = tk.IntVar()
v33.set(4)
e33 = tk.Entry(tab3, text =v33, width=8)
e33.grid(column=1, row=0)

b31 = tk.Button(tab3, command=f_b3, text = "          Hitung!          ")
b31.grid(row=1, columnspan=5)

l30 =tk.Label(tab3, text='Tanggal:', width=12)
l30.grid(row=0, column=0)
l310 = tk.Label(tab3, text="Hari Kelahiran")
l310.grid(row=2, column=0, sticky="W")
l31 = tk.Label(tab3)
l31.grid(row=2, column=1, columnspan=3, sticky="W")
l320 = tk.Label(tab3, text="Sepasaran")
l320.grid(row=3, column=0, sticky="W")
l32 = tk.Label(tab3)
l32.grid(row=3, column=1, columnspan=3, sticky="W")
l330 = tk.Label(tab3, text="Selapanan")
l330.grid(row=4, column=0, sticky="W")
l33 = tk.Label(tab3)
l33.grid(row=4, column=1, columnspan=3, sticky="W")
l340 = tk.Label(tab3, text="Tedhak Siten")
l340.grid(row=5, column=0, sticky="W")
l34 = tk.Label(tab3)
l34.grid(row=5, column=1, columnspan=3, sticky="W")

# Make 4th Tab
tab4 = tk.Frame(main)
main.add(tab4, text="Kematian")

v41 = tk.IntVar()
v41.set(2019)
e41 = tk.Entry(tab4, text=v41, width=16)
e41.grid(column=3, row=0)
v42 = tk.IntVar()
v42.set(11)
e42 = tk.Entry(tab4, text=v42, width=8)
e42.grid(column=2, row=0)
v43 = tk.IntVar()
v43.set(23)
e43 = tk.Entry(tab4, text =v43, width=8)
e43.grid(column=1, row=0)

b41 = tk.Button(tab4, command=f_b4, text = "          Hitung!          ")
b41.grid(row=1, columnspan=5)

l40 =tk.Label(tab4, text='Tanggal:', width=12)
l40.grid(row=0, column=0)
l410 = tk.Label(tab4, text="Hari Kematian")
l410.grid(row=2, column=0, sticky="W")
l41 = tk.Label(tab4)
l41.grid(row=2, column=1, columnspan=3, sticky="W")
l420 = tk.Label(tab4, text="Hari ke-3")
l420.grid(row=3, column=0, sticky="W")
l42 = tk.Label(tab4)
l42.grid(row=3, column=1, columnspan=3, sticky="W")
l430 = tk.Label(tab4, text="Hari ke-7")
l430.grid(row=4, column=0, sticky="W")
l43 = tk.Label(tab4)
l43.grid(row=4, column=1, columnspan=3, sticky="W")
l440 = tk.Label(tab4, text="Hari ke-40")
l440.grid(row=5, column=0, sticky="W")
l44 = tk.Label(tab4)
l44.grid(row=5, column=1, columnspan=3, sticky="W")
l450 = tk.Label(tab4, text="Hari ke-100")
l450.grid(row=6, column=0, sticky="W")
l45 = tk.Label(tab4)
l45.grid(row=6, column=1, columnspan=3, sticky="W")
l460 = tk.Label(tab4, text="Tahun ke-1")
l460.grid(row=7, column=0, sticky="W")
l46 = tk.Label(tab4)
l46.grid(row=7, column=1, columnspan=3, sticky="W")
l470 = tk.Label(tab4, text="Tahun ke-2")
l470.grid(row=8, column=0, sticky="W")
l47 = tk.Label(tab4)
l47.grid(row=8, column=1, columnspan=3, sticky="W")
l480 = tk.Label(tab4, text="Hari ke-1000")
l480.grid(row=9, column=0, sticky="W")
l48 = tk.Label(tab4)
l48.grid(row=9, column=1, columnspan=3, sticky="W")


root.mainloop()
