from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Interest calculator")
window.geometry("600x600")
choice_label = Label(window, text = "Enter type of interest(Simple / Compound): ", bg = "#4a9d9c", fg = "white")
choice_entry = Entry()
#Input
P_label = Label(window, text = "Enter Principal/Capital: ", bg = "#4a9d9c", fg = "white")
P_entry = Entry()
r_label = Label(window, text = "Enter Rate of interest: ", bg = "#4a9d9c", fg = "white")
r_entry = Entry()
n_label = Label(window, text = "Times interest gained: ", bg = "#4a9d9c", fg = "white")
n_entry = Entry()
#Functions
def calculate_simple():
    p = int(P_entry.get())
    r1 = float(r_entry.get())
    r2 = r1 / 100
    n = int(n_entry.get())
    result = p * r2 * n
    messagebox.showinfo("Interest", result)
def calculate_compound():
    p = int(P_entry.get())
    r1 = float(r_entry.get())
    r2 = r1 / 100
    n = int(n_entry.get())
    result = p * (1 + r2 / 100) ** n - p
    messagebox.showinfo("Interest", result)
def calculate_choice():
    choice =  choice_entry.get()
    if choice == "simple" or choice == "Simple":
        calculate_simple()
    elif choice == "compound" or choice == "Compound":
        calculate_compound()
#Button
calc_btn = Button(text = "Calculate", relief = GROOVE, command = calculate_choice, bg = "#FF3D3D")
#Geometry
choice_label.place(x = 20, y = 20)
choice_entry.place(x = 275, y = 20)
P_label.place(x = 20, y = 80)
P_entry.place(x = 160, y = 80)
r_label.place(x = 20, y = 140)
r_entry.place(x = 160, y = 140)
n_label.place(x = 20, y = 200)
n_entry.place(x = 160, y = 200)
calc_btn.place(x = 140, y = 260)
window.mainloop()