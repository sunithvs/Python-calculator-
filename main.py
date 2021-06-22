from tkinter import *

root = Tk()
root.title('Calculator')
# constants
padding = 45
width = 60


# functions

def button_click(num):
    operations = ['+', '-', '/', '*']
    current = str(text_box.get())
    text_box.delete(0, END)
    if num == 'ac':
        current = ''
    elif num == '=':
        try:
            current=eval(current)
        except:
            current='sytax error press ac to clear the screen'
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

text_box = Entry(root, width=width, borderwidth=5)
text_box.grid(row=0, column=0, columnspan=4)

# buttons are creating here

button_1 = Button(root, text='1', padx=padding, pady=padding, command=lambda: button_click('1'))
button_2 = Button(root, text='2', padx=padding, pady=padding, command=lambda: button_click('2'))
button_3 = Button(root, text='3', padx=padding, pady=padding, command=lambda: button_click('3'))
button_4 = Button(root, text='4', padx=padding, pady=padding, command=lambda: button_click('4'))
button_5 = Button(root, text='5', padx=padding, pady=padding, command=lambda: button_click('5'))
button_6 = Button(root, text='6', padx=padding, pady=padding, command=lambda: button_click('6'))
button_7 = Button(root, text='7', padx=padding, pady=padding, command=lambda: button_click('7'))
button_8 = Button(root, text='8', padx=padding, pady=padding, command=lambda: button_click('8'))
button_9 = Button(root, text='9', padx=padding, pady=padding, command=lambda: button_click('9'))
button_0 = Button(root, text='0', padx=padding, pady=padding, command=lambda: button_click('0'))
button_add = Button(root, text='+', padx=padding, pady=padding, command=lambda: button_click('+'))
button_sub = Button(root, text='-', padx=padding, pady=padding, command=lambda: button_click('-'))
button_mul = Button(root, text='x', padx=padding, pady=padding, command=lambda: button_click('x'))
button_div = Button(root, text='/', padx=padding, pady=padding, command=lambda: button_click('/'))
button_clear = Button(root, text='AC', padx=padding - 3, pady=padding, command=lambda: button_click('ac'))
button_equal = Button(root, text='=', padx=padding - 2, pady=padding, command=lambda: button_click('='))

button_9.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=2)
button_6.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=2)
button_3.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=2)
button_0.grid(row=4, column=0)

button_clear.grid(row=1, column=3)
button_add.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_mul.grid(row=4, column=1)
button_div.grid(row=4, column=2)
button_equal.grid(row=4, column=3)

root.mainloop()
