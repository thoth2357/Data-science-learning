# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 21:54:30 2019

@author: oyewunmi oluwaseyi
"""

# =============================================================================
#The calculation of Volume weighted average price 
#The higher the volume, the more significant a price move typically is. VWAP is
#often used in algorithmic trading and is calculated using volume values as weights.
# =============================================================================
def NewUser():
    import tkinter as tk
    Dictionary={}
    root=tk.Tk()
    entry1=tk.Entry(root)
    entry2=tk.Entry(root)
    entry1.pack()
    entry2.pack()
    def commands():
        Dictionary[entry1.get()]=entry2.get()
        print(Dictionary)
    frame=tk.Frame(root)
    q=tk.Button(frame,text='REGISTER',fg='blue',width=10,command=commands)
    v=tk.StringVar()
    tk.Entry(root,textvariable=v).pack(side='top',fill='x')
    v.set('Enter your password')
    frame.pack()
    q.pack()
    tk.mainloop()  
NewUser()

class Message(tk.Toplevel): #class for message display
         def __init__(self,width=700,height=200,text="Copy To Clipboard",bg="white",font=('arial 20 bold italic')):#self is the class initializer
          tk.Toplevel.__init__(self)
          self.font=font
          self.text=text
          self.bg=bg
          self.width=width
          self.height=height
          self.focus_force()
          self.overrideredirect(True)
          self.creating_label()
         def creating_label(self):
              tk.Label(self,text=self.text,bg=self.bg,font=self.font).pack(expand='yes',fill='both')
         def timer_is_starting(self):
          x=1.0
          for i in range(110):
           time.sleep(0.02)
           self.update_idletasks()
           self.update()
           self.attributes('-alpha',x)
           x=x-0.01
          return 
              
