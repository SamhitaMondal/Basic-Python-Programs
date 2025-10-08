# GRAPHICAL CALCULATOR
import tkinter as tk
#GLOBAL DECLARATION


root =tk.Tk()   #CREATE MAIN WINDOW
root.title("CALCULATOR")  #SET TITLE
root.geometry("300x400")   #SET WINDOW HEIGHT AND WIDTH
root.configure(background="blue")

expression=" "
equation= tk.StringVar()   #TKINTER VARIABLE(CONNECTED TO ENTRY)

def press(num):
    global expression
    expression+=str(num) #ADD THE BUTTON'S VALUE(NUM) TO THE EXPRESSION STRING
    equation.set(expression)  #UPDATE SCREEN (ENTRY BOX) WITH CURRENT EXPRESSION

def clear():
    global expression
    expression=" "  #reset the string
    equation.set(" ") #update the screen to empty


#entry box(Calculator screen)
entry = tk.Entry(root,textvariable=equation,font=("Arial",20),bd=10,relief="ridge")
entry.grid(row=0,column=0,columnspan=4,pady=10)

#Digits Layout
digits=[('7',1,0),('8',1,1),('9',1,2),
        ('4',2,0),('5',2,1),('6',2,2),
        ('1',3,0),('2',3,1),('3',3,2),
        ('0',4,1)]
for (text,row,col) in digits:
    button=tk.Button(root,text=text,width=5,height=2,font=("Arial",16),command=lambda t=text:press(t))#false function created which waits till the button is pressed to call that function
    button.grid(row=row,column=col,padx=5,pady=5)#pady=adds vertical padding and padx=adds horizontal padding

#Clear button

clear_btn=tk.Button(root,text="C",width=5,height=2,font=("Arial",16),command=clear)
clear_btn.grid(row=4,column=0,padx=5,pady=5)

#OPERATORS
add_btn=tk.Button(root,text="+",width=10,height=2,command=lambda:press("+"))
add_btn.grid(row=1,column=3,pady=5)

sub_btn=tk.Button(root,text="-",width=10,height=2,command=lambda:press("-"))
sub_btn.grid(row=2,column=3,pady=5)

mul_btn=tk.Button(root,text="*",width=10,height=2,command=lambda:press("*"))
mul_btn.grid(row=3,column=3,pady=5)

div_btn=tk.Button(root,text="/",width=10,height=2,command=lambda:press("/"))
div_btn.grid(row=4,column=3,pady=5)

def equalpress():
    global expression
    try:
        result = str(eval(expression))   # evaluate expression
        equation.set(result)             # show result
        expression = result              # allow continuing calculation
    except:
        equation.set("Error")
        expression = ""


equal_btn=tk.Button(root,text="=",width=10,height=2,command=equalpress)
equal_btn.grid(row=4,column=2,pady=10)
root.mainloop()