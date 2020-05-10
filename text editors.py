import os
def printtxt(name):
    f = open(name,"r",encoding="utf-8")
    b = f.read()
    f.close()
    return b

def writestr(str,name):
    with open(name,"w",encoding='utf-8') as f:
        f.write(str)

def writestr2(str,name):
    with open(name,"a",encoding='utf-8') as f:
        f.write(str)

def writelist(list,name):
    for j in range(len(list)):
        writestr2(str(list[j])+" ",name)

def write2dlist(list,name):
    for i in range(len(list)):
        writelist(list[i],name)
        writestr2("\n",name)
    writestr2("\n",name)


from tkinter import *
import time

class App():
  def __init__(self):
    App.window = Tk()

  def const_say(self, text):
    App.say_text = Label(App.window,text = text)
    App.say_text.pack()

  def say(self, x, y, text):
    App.say_text2 = Label(App.window,text = text)
    App.say_text2.place(x = x, y = y, anchor = NW)

  def windows(self, l, w):
    App.window.geometry(str(w) + "x" + str(l))

  def button(self, text, a):
    App.B = Button(App.window, text = text, command = a)
    App.B.pack()

  def button2(self, text, a, x, y):
    App.B2 = Button(App.window, text = text, command = a)
    App.B2.place(x = x, y = y, anchor = NW)

  def input_str(self, text, f):
    App.inputstr = Entry(App.window)
    App.inputstr.pack()

    b1 = Button(App.window, text = text, command = f)
    b1.pack()

  def input_str2(self, text, f, entry_x, entry_y, button_x, button_y):

    App.inputstr2 = Entry(App.window)
    App.inputstr2.place(x = entry_x, y = entry_y, anchor = NW)

    App.b2 = Button(App.window, text = text, command = f)
    App.b2.place(x = button_x, y = button_y, anchor = NW)
    
  def input_text(self, text, f):
    App.inputtext = Text(App.window, width = 100, heigh = 30)
    App.inputtext.pack()

    b3 = Button(App.window, text = text, command = f)
    b3.pack()


  

  

a = App()

a.windows(500,700)

a.window.title("text editors")

def b():
    global name
    name = a.inputstr.get()

    try:
        a.inputtext.delete(0.0,"end")
        a.inputtext.insert("insert",printtxt(name))
    except FileNotFoundError:
        writestr("",name)

def d():
    e = a.inputtext.get(0.0, "end")
    writestr(e,name)
    
    a.inputtext.delete(0.0,"end")
    a.inputtext.insert("insert",printtxt(name))
    

a.say(0, 0, " Please Input File Name:")
a.input_str("OK", b)
a.input_text("write", d)

a.window.mainloop()
