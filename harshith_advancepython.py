def sc(event):
    text=event.widget.cget("text")
    no=e.get()
    result=" "
    try:
       if text=='deg':
           result=str(m.degrees(float(no)))
       if text=='sin':
          result=str(m.sin(float(no)))
       if text=='cos':
          result=str(m.cos(float(no)))
       if text=='tan':
          result=str(m.tan(float(no)))
       if text=='lg':
         result=str(m.log10(float(no)))
       if text=='ln':
         result=str(m.log(float(no)))
       if text=='fact':

             result=str(m.factorial(float(no)))

       if text == 'sqrt':
          result = str(m.sqrt(float(no)))
       if text == '1/x':
          result = str(1/(float(no)))
       if text == 'pi':
           if no=="":
              result=str(m.pi)
           else:
              result=str(m.pi**float(no))
       if text == 'pow':
           if no=="":
              result=str(m.e)
           else:
              result=str(m.e**float(no))
       e.delete(0,END)
       e.insert(0,result)
    except:

        e.delete(0,END)
        e.insert(0,"ERROR")

def click(to_print):
    if e.get()=="ERROR":
        e.delete(0,END)
    p=to_print.widget.cget("text")
    s=e.get()
    e.delete(0,END)
    e.insert(0,s + p)
def clear(event):
    e.delete(0,END)
def bksps(event):
    s=e.get()
    leng=len(s)-1
    e.delete(leng,END)
def evaluate(event):
    try:
       s=e.get()
       s=eval(s)
       e.delete(0,END)
       e.insert(0,s)
    except:
        d="ERROR"
        e.delete(0,END)
        e.insert(0,d)
from tkinter import *
import math as m
window=Tk()
window.title("MY CALCI")
window.geometry("700x1000")
e=Entry(window,bg="Black",fg='White',font="lucida 15 bold",width=100,bd=5)
e.grid(row=0,column=0,columnspan=10)
lg=Button(window,text='lg',bg='Black',fg='white',padx=25,pady=10)
lg.bind("<Button-1>",sc)
pow=Button(window,text='pow',bg='Black',fg='white',padx=25,pady=10)
pow.bind("<Button-1>",sc)
ln=Button(window,text='ln',bg='Black',fg='white',padx=25,pady=10)
ln.bind("<Button-1>",sc)
sqrt=Button(window,text='sqrt',bg='Black',fg='white',padx=25,pady=10)
sqrt.bind("<Button-1>",sc)
fact=Button(window,text='fact',bg='Black',fg='white',padx=25,pady=10)
fact.bind("<Button-1>",sc)
sin=Button(window,text='sin',bg='Black',fg='white',padx=25,pady=10)
sin.bind("<Button-1>",sc)
cos=Button(window,text='cos',bg='Black',fg='white',padx=25,pady=10)
cos.bind("<Button-1>",sc)
tan=Button(window,text='tan',bg='Black',fg='white',padx=25,pady=10)
tan.bind("<Button-1>",sc)
b1=Button(window,text='(',bg='Black',fg='white',padx=25,pady=10)
b1.bind("<Button-1>",click)
b2=Button(window,text=')',bg='Black',fg='white',padx=25,pady=10)
b2.bind("<Button-1>",click)



B7=Button(window,text='7',bg='Black',fg='white',padx=25,pady=10)
B7.bind("<Button-1>",click)
B8=Button(window,text='8',bg='Black',fg='white',padx=25,pady=10)
B8.bind("<Button-1>",click)
B9=Button(window,text='9',bg='Black',fg='white',padx=25,pady=10)
B9.bind("<Button-1>",click)
plus=Button(window,text='+',bg='Black',fg='white',padx=25,pady=10)
plus.bind("<Button-1>",click)
BKS=Button(window,text='BKSPS',bg='Black',fg='white',padx=25,pady=10)
BKS.bind("<Button-1>",bksps)
B4=Button(window,text='4',bg='Black',fg='white',padx=25,pady=10)
B4.bind("<Button-1>",click)
B5=Button(window,text='5',bg='Black',fg='white',padx=25,pady=10)
B5.bind("<Button-1>",click)
B6=Button(window,text='6',bg='Black',fg='white',padx=25,pady=10)
B6.bind("<Button-1>",click)
sub=Button(window,text='-',bg='Black',fg='white',padx=25,pady=10)
sub.bind("<Button-1>",click)
clr=Button(window,text='clr',bg='Red',fg='white',padx=25,pady=10)
clr.bind("<Button-1>",clear)
B1=Button(window,text='1',bg='Black',fg='white',padx=25,pady=10)
B1.bind("<Button-1>",click)
B2=Button(window,text='2',bg='Black',fg='white',padx=25,pady=10)
B2.bind("<Button-1>",click)
B3=Button(window,text='3',bg='Black',fg='white',padx=25,pady=10)
B3.bind("<Button-1>",click)
mul=Button(window,text='*',bg='Black',fg='white',padx=25,pady=10)
mul.bind("<Button-1>",click)
res=Button(window,text='1/x',bg='Black',fg='white',padx=25,pady=10)
res.bind("<Button-1>",sc)



modiv=Button(window,text='%',bg='Black',fg='white',padx=25,pady=10)
modiv.bind("<Button-1>",click)
B0=Button(window,text='0',bg='Black',fg='white',padx=25,pady=10)
B0.bind("<Button-1>",click)
point=Button(window,text='.',bg='Black',fg='white',padx=25,pady=10)
point.bind("<Button-1>",click)
div=Button(window,text='/',bg='Black',fg='white',padx=25,pady=10)
div.bind("<Button-1>",click)
equal=Button(window,text='=',bg='Black',fg='white',padx=25,pady=10)
equal.bind("<Button-1>",evaluate)
lg.grid(row=1,column=0)
ln.grid(row=1,column=1)
pow.grid(row=1,column=2)
sqrt.grid(row=1,column=3)
fact.grid(row=1,column=4)
sin.grid(row=2,column=0)
cos.grid(row=2,column=1)
tan.grid(row=2,column=2)
b1.grid(row=2,column=3)
b2.grid(row=2,column=4)
B7.grid(row=3,column=0)
B8.grid(row=3,column=1)
B9.grid(row=3,column=2)
plus.grid(row=3,column=3)
BKS.grid(row=3,column=4)
B4.grid(row=4,column=0)
B5.grid(row=4,column=1)
B6.grid(row=4,column=2)
sub.grid(row=4,column=3)
clr.grid(row=4,column=4)
B1.grid(row=5,column=0)
B2.grid(row=5,column=1)
B3.grid(row=5,column=2)
mul.grid(row=5,column=3)
res.grid(row=5,column=4)

modiv.grid(row=6,column=0)
B0.grid(row=6,column=1)
point.grid(row=6,column=2)
div.grid(row=6,column=3)
equal.grid(row=6,column=4)
window.mainloop()