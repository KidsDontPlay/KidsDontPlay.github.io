from Tkinter import *
def antwort():
	global label
	global var
	file_object = open('py.txt', 'r')
	var=var+1
	label.config(text=file_object.read())

root=Tk()
label=Label(root,text="Unknown")
but=Button(root,text="Refresh",command=antwort)
but.pack()
label.pack()
var=0
root.mainloop()

import Tkinter as tk

counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
root = tk.Tk()
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()
