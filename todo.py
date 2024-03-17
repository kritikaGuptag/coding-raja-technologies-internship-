
from curses import def_prog_mode
from logging import root
from operator import add
from tkinter import *
from tkinter import ttk
from tkinter import _ButtonCommand
from tkinter.tix import ButtonBox
from typing import ItemsView, Self

class todo:
    def_prog_mode(Self,root);
    Self.root = root
    Self.root.title('to-do-list')
    Self.root.geometry('650+410+150')

    Self.label =Label(Self.root,text="to-do-list-app",font='ariel,25',width=10,bd=5,bg='pink',fg='black')
    Self.label.pack(side='top',fill=BOTH)
    
    Self.label2 =Label(Self.root,text="Add task",font='ariel,18',width=10,bd=5,bg='pink',fg='black')
    Self.label2.place(x=40,y=54)

    Self.label3 =Label(Self.root,text=" Tasks",font='ariel,18',width=10,bd=5,bg='pink',fg='black')
    Self.label3.place(x=320,y=54)
    
    Self.main_text=Listbox(Self.root,height=9,bd=5,width=23,font="ariel,20 Italic bold")
    Self.main_text.place(x=280,y=100)
    
    Self.text=Text(Self.root,bd=5,height=2,width=30,font="ariel,10 bold")
    Self.text.place(x=20,y=120)
    

    def add():
           content=Self.text.get(1.0,END)
           Self.main.text.insert(END,content)
           with open("data.txt",'w') as file:
               file.write(content)
               file.seek(0)
               file.close()
    Self.text.delete(1.0,END)
    
    def delete():
             delete_=Self.main_text.curselection()
             look=Self.main_text.get(delete_)
             with open("data.txt","r+") as f:
                 new_f=f.readlines
                 f.seek(0)
                 for line in new_f:
                     Item=str(look)
                     if ItemsView not in line:
                         f.write(line)
             f.truncate()
             Self.main_text.delete_(delete_)

             with open("data.txt",'r') as file:
                 read=file.readlines()
                 for i in read:
                     ready=look.split()
                     Self.main_text.Insert(END,ready)
             file.close()
             
             Self.button=ButtonBox(Self.root,Text="Add",font='sarif,20 bold italic',width=10,bd=5,bg='pink',fg="black",COMMAND=add)
             Self.button.place(x=30,y=280)

             Self.button=_ButtonCommand(Self.root,Text="Delete",font='sarif,20 bold italic',width=10,bd=5,bg='pink',fg="black",COMMAND=delete_)
             Self.button.place(x=30,y=280)

def main():
    root=Tk()
    u1=todo(root)
    root.mainloop()     
                 

if __name__=="_main_":
     main()


