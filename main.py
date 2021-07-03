from tkinter import *
from Buttons import buttons
root = Tk()
root.title('Calculator')


# constants
width = 10
height = 5

"""
    This function perform according to the input
    
"""
def button_click(num):
    current = str(text_box.get())
    text_box.delete(0, END)
    if num == 'Ac':
        current = ''
    elif num == '=':
        try:
            current = eval(current)
        except:
            current = 'syntax error press Ac to clear the screen'
    elif not num.isdigit() and len(current) > 0:
        if not current[-1].isdigit():
            temp = current[:-1] + str(num)
            current = temp
        else:
            current = str(current) + num
    elif not num.isdigit() and len(current) == 0:
        current = ''
    else:
        current += num
    text_box.insert(0, current)


# input box goes here
text_box = Entry(root, width=width*5, borderwidth=5)
text_box.grid(row=0, column=0, columnspan=4)

#   Buttons are created and displayed here
for btn in buttons:
    btn["btn_object"] = Button(root, text=btn["text"], width=width, height=height, command=  lambda text=btn["text"]: button_click(text))
    btn["btn_object"].grid(row=btn["position"][0], column=btn["position"][1])

root.mainloop()
