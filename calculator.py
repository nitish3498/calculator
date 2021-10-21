from tkinter import*
box = Tk()
def click(a):
    input.insert(END,str(a))

def calculate():
    global b
    input_from_box=input.get()
    try:
    output_ = eval(str(input_from_box))
    input.delete(0,END)
    b=str(output_)
    input.insert(END,b)
    except:
        b = 'cannot divide by zero'
        input.insert(END,b)
        
def delete():
    input.delete(0,END)

box.title("calculator")
input = Entry(box,width=40,borderwidth = 5)
input.grid(row = 0, column=0,columnspan=4)
button0 =Button(box,width=10,height = 5,text= "0",font=17,command= lambda :click('0'),borderwidth = 5)
button1 =Button(box,width=10,height = 5,text= "1",command= lambda :click('1'),borderwidth = 5,font=17)
button2 =Button(box,width=10,height = 5,text= "2",command= lambda :click('2'),borderwidth = 5,font=17)
button3 =Button(box,width=10,height = 5,text= "3",command= lambda :click('3'),borderwidth = 5,font=17)
button4 =Button(box,width=10,height = 5,text= "4",command= lambda :click('4'),borderwidth = 5,font=17)
button5 = Button(box,width=10,height = 5,text= "5",command= lambda :click('5'),borderwidth = 5,font=17)
button6 =Button(box,width=10,height = 5,text= "6",command= lambda :click('6'),borderwidth = 5,font=17)
button7 = Button(box,width=10,height = 5,text= "7",command= lambda :click('7'),borderwidth = 5,font=17)
button8 =Button(box,width=10,height = 5,text= "8",command= lambda :click('8'),borderwidth = 5,font=17)
button9 = Button(box,width=10,height = 5,text= "9",command= lambda :click('9'),borderwidth = 5,font=17)
buttonsub = Button(box,width=10,height = 5,text= "-",command= lambda :click('-'),borderwidth = 5,font=17)
buttonadd = Button(box,width=10,height = 5,text= "+",command= lambda :click('+'),borderwidth = 5,font=17)
buttondiv =Button(box,width=10,height = 5,text= "/",command= lambda :click('/'),borderwidth = 5,font=17)
buttonmultiply = Button(box,height = 5,width=10,text= "*",command= lambda :click('*'),borderwidth = 5,font=17)
buttonequal = Button(box,height = 5,width=10,text="=",command= calculate,borderwidth = 5,font=17)
buttonclear = Button(box,height = 5,width=10,text="CE",command= delete,borderwidth = 5,font=17)
button0.grid(row=4,column=1)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
buttonadd.grid(row=1,column=3)
buttonsub.grid(row=2,column=3)
buttondiv.grid(row=3,column=3)
buttonmultiply.grid(row=4,column=3)
buttonequal.grid(row = 4,column=2)
buttonclear.grid(row=4,column=0)
box.mainloop()
