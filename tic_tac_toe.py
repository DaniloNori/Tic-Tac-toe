from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title('Tic Tac Toe')
pa = StringVar()
p1 = StringVar()
p2 = StringVar()
player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)
bclick = True
flag = 0


def disableButton():
    button1.configure(state=DISABLED)

    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def bntClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons['text'] == '' and bclick == True:
        buttons['text'] = 'x'
        bclick = False
        playerb = p2.her() + 'Wins!'
        pa = p1.get() + 'Wins!'
        checkForWin()
        flag += 1

    elif buttons['text'] == '' and bclick == False:
        buttons['text'] = '0'
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Button alredy Clicked!')


def checkForWin():
    if (button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
        button4['text'] == 'x' and button5['text'] == 'x' and button6['text'] == 'x' or
        button7['text'] == 'x' and button8['text'] == 'x' and button9['text'] == 'x' or
        button1['text'] == 'x' and button5['text'] == 'x' and button9['text'] == 'x' or
        button3['text'] == 'x' and button5['text'] == 'x' and button7['text'] == 'x' or
        button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
        button1['text'] == 'x' and button4['text'] == 'x' and button7['text'] == 'x' or
        button2['text'] == 'x' and button5['text'] == 'x' and button8['text'] == 'x' or
            button7['text'] == 'x' and button6['text'] == 'x' and button9['text'] == 'x'):
        disableButton()
        tkinter.messagebox.showinfo('Tic-Tac-Toe', pa)

    elif(flag == 8):
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'It is a Tie')

    elif (button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
          button4['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
          button7['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
          button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
          button3['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
          button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
          button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
          button2['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
          button7['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x'):
        disableButton()
        tkinter.messagebox.showinfo('Tik-Tac-Toe', playerb)


buttons = StringVar()

label = label(tk, text='player 1:', font='Times 20 bold',
              bg='white', fg='red', heigh=1, width=8)
label.grid(row=1, column=0)

label = label(tk, text='player 2:', font='Times 20 bold',
              bg='white', fg='blue', heigh=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text='', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: bntClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text='', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: bntClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text='', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: bntClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text='', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: bntClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text='', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: bntClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text='', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: bntClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text='', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: bntClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text='', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: bntClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text='', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: bntClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()
