from tkinter import *

def updateDisplay(buttonString):
	content = display.get()
	if content==0:
		content=""
	display.set(content+buttonString)

def calculate():
	result = eval(display.get())
	display.set(display.get()+'=\n'+str(result) )

def clear():
	display.set('')


def backspace():
	display.set(str(display.get()[:-1]))






mainUI = Tk()
mainUI.title('calculator')
mainUI.geometry('200x320+300+300')

display = StringVar()
display.set('')

textLabel = Label(mainUI)
textLabel.config(bg='gray',width=28,height=3,anchor=SE)
textLabel['textvariable']=display

textLabel.grid(row=0,column=0,columnspan=4)

clearButton = Button(mainUI,text="C",fg='orange',width=3,command=clear)
clearButton.grid(row=1,column=0)

Button(mainUI,text='DEL',width=3,command=backspace).grid(row=1,column=1)

Button(mainUI,text='/',width=3,command=lambda:updateDisplay('/')).grid(row=1,column=2)

Button(mainUI,text='*',width=3,command=lambda:updateDisplay('*')).grid(row=1,column=3)

Button(mainUI,text='7',width=3,command=lambda:updateDisplay('7')).grid(row=2,column=0)

Button(mainUI,text='8',width=3,command=lambda:updateDisplay('8')).grid(row=2,column=1)

Button(mainUI,text='9',width=3,command=lambda:updateDisplay('9')).grid(row=2,column=2)

Button(mainUI,text='-',width=3,command=lambda:updateDisplay('-')).grid(row=2,column=3)

Button(mainUI,text='4',width=3,command=lambda:updateDisplay('4')).grid(row=3,column=0)

Button(mainUI,text='5',width=3,command=lambda:updateDisplay('5')).grid(row=3,column=1)

Button(mainUI,text='6',width=3,command=lambda:updateDisplay('6')).grid(row=3,column=2)

Button(mainUI,text='+',width=3,command=lambda:updateDisplay('+')).grid(row=3,column=3)

Button(mainUI,text='1',width=3,command=lambda:updateDisplay('1')).grid(row=4,column=0)

Button(mainUI,text='2',width=3,command=lambda:updateDisplay('2')).grid(row=4,column=1)

Button(mainUI,text='3',width=3,command=lambda:updateDisplay('3')).grid(row=4,column=2)

Button(mainUI,text='=',width=3,bg='orange',height=3,command=lambda:calculate()).grid(row=4,column=3,rowspan=2)

Button(mainUI,text='0',width=10,command=lambda:updateDisplay('0')).grid(row=5,column=0,columnspan=2)

Button(mainUI,text='.',width=3,command=lambda:updateDisplay('.')).grid(row=5,column=2)

mainUI.mainloop()
