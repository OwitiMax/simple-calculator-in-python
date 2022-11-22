from tkinter import *
import math
def Addnumbers(number):
    current=field.get()
    field.delete(0,END)
    field.insert(0,f'{current}{number}')

def clear():
    field.delete(0,END)
def Add():
    first_number=field.get()
    global f_num
    f_num=int(first_number)
    global math
    math='add'
    field.delete(0,END)
def Equal():
    second_num=field.get()
    field.delete(0,END)
    if(math=='add'):
        field.insert(0,f_num+int(second_num))
    if (math == 'multiply'):
        field.insert(0, f_num * int(second_num))
    if (math == 'divide'):
        field.insert(0, f_num / int(second_num))
    if (math == 'substract'):
        field.insert(0, f_num - int(second_num))

def multiply():
    first_number = field.get()
    global f_num
    f_num = int(first_number)
    global math
    math = 'multiply'
    field.delete(0, END)
def divide():
    first_number = field.get()
    global f_num
    f_num = int(first_number)
    global math
    math = 'divide'
    field.delete(0, END)
def substract():
    first_number = field.get()
    global f_num
    f_num = int(first_number)
    global math
    math = 'substract'
    field.delete(0, END)
root=Tk()
root.title("simple calculator")
root.resizable(False,False)
#root.geometry('x375')
field=Entry(root,width=40,borderwidth=5)
field.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#adding the buttons
button_1=Button(root,padx=30,pady=20,text='1',command=lambda:Addnumbers(1))
button_2=Button(root,padx=30,pady=20,text='2',command=lambda :Addnumbers(2))
button_3=Button(root,padx=30,pady=20,text='3',command=lambda :Addnumbers(3))
button_4=Button(root,padx=30,pady=20,text='4',command=lambda :Addnumbers(4))
button_5=Button(root,padx=30,pady=20,text='5',command=lambda:Addnumbers(5))
button_6=Button(root,padx=30,pady=20,text='6',command=lambda:Addnumbers(6))
button_7=Button(root,padx=30,pady=20,text='7',command=lambda:Addnumbers(7))
button_8=Button(root,padx=30,pady=20,text='8',command=lambda:Addnumbers(8))
button_9=Button(root,padx=30,pady=20,text='9',command=lambda :Addnumbers(9))
button_0=Button(root,padx=30,pady=20,text='0',command=lambda :Addnumbers(0))
#putting the butns on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
#the new *,/ and subtraction signs in the calculator
button_mult=Button(root,padx=30,pady=20,text='*',command=multiply)
button_divide=Button(root,padx=30,pady=20,text='/',command=divide)
button_substact=Button(root,padx=30,pady=20,text='-',command=substract)

#thier position in the root window
button_mult.grid(row=4,column=1)
button_divide.grid(row=5,column=0)
button_substact.grid(row=4,column=2)
#trigonometry
button_tan=Button(root,padx=20,pady=20,text='Tan()',command=substract)
button_cos=Button(root,padx=20,pady=20,text='Cos()',command=substract)
#position of the trigonometry
button_tan.grid(row=6,column=0)
button_cos.grid(row=6,column=1)
#clear screen addition and equals
button_add=Button(root,padx=30,pady=20,text='+',command=Add)
button_clear=Button(root,padx=20,pady=20,text='clear',command=clear)
button_equals=Button(root,padx=30,pady=20,text='=',command=Equal)
#adding the new buttons to the screen
button_add.grid(row=5,column=1)
button_clear.grid(row=5,column=2)
button_equals.grid(row=6,column=2)
root.mainloop()