from tkinter import *
import time

def show():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(200,show)

root=Tk()
root.title("Digital clock")
root.geometry("600x250") ## window size
root.configure(background="black")
root.resizable(0,0) ## non resizable
clock=Label(root,font=("calibri",50,"italic"),bg="black",fg="red")
clock.grid(row=2,column=2,pady=35,padx=100)
show()

lbl=Label(root,text="Digital Clock",font="calibri 24 italic",bg='black',fg='white')
lbl.grid(row=0,column=2)
lbl1=Label(root,text="Hours            Minutes          Seconds",font="calibri 15 italic",bg='black',fg='white')
lbl1.grid(row=3,column=2)
root.mainloop()
