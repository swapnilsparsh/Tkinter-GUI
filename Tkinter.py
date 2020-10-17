from tkinter import *
def sum():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    t3.insert(0,c)

# GUI 
root =Tk()
root.geometry('250x250')
root.title("Sum")

l1=Label(root,text="First Number")
l1.grid(row=0,column=0)
t1=Entry(root)
t1.grid(row=0,column=1)

l2=Label(root,text="Second Number")
l2.grid(row=1,column=0)
t2=Entry(root)
t2.grid(row=1,column=1)

l3=Label(root,text="Result")
l3.grid(row=2,column=0)
t3=Entry(root)
t3.grid(row=2,column=1)

b1=Button(root,text="Click For SUM",command=sum)
b1.grid(row=3,column=0)

root.mainloop()