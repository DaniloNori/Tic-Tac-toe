from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title('Tic Tac Toe')

p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)

player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0


def disable_buttons():
    for button in buttons:
        button.configure(state=DISABLED)


def bnt_click(button):
    global bclick, flag, player1_name, player2_name, playerb, pa
    if button['text'] == '' and bclick:
        button['text'] = 'X'
        bclick = False
        playerb = p2.get() + ' Wins!'
        pa = p1.get() + ' Wins!'
        check_for_win()
        flag += 1

    elif button['text'] == '' and not bclick:
        button['text'] = 'O'
        bclick = True
        check_for_win()
        flag += 1
    else:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'Button already clicked!')


def check_for_win():
    global buttons
    for i in range(0, 8, 3):
        if buttons[i]['text'] == buttons[i+1]['text'] == buttons[i+2]['text'] != '':
            disable_buttons()
            winner = pa if buttons[i]['text'] == 'X' else playerb
            tkinter.messagebox.showinfo('Tic-Tac-Toe', winner)
            return

    for i in range(3):
        if buttons[i]['text'] == buttons[i+3]['text'] == buttons[i+6]['text'] != '':
            disable_buttons()
            winner = pa if buttons[i]['text'] == 'X' else playerb
            tkinter.messagebox.showinfo('Tic-Tac-Toe', winner)
            return

    if buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] != '':
        disable_buttons()
        winner = pa if buttons[0]['text'] == 'X' else playerb
        tkinter.messagebox.showinfo('Tic-Tac-Toe', winner)
        return

    if buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] != '':
        disable_buttons()
        winner = pa if buttons[2]['text'] == 'X' else playerb
        tkinter.messagebox.showinfo('Tic-Tac-Toe', winner)
        return

    if flag == 8:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', 'It is a Tie')


buttons = []
for i in range(3):
    for j in range(3):
        button = Button(tk, text='', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                        command=lambda b=button: bnt_click(b))
        button.grid(row=i+3, column=j)
        buttons.append(button)

label = Label(tk, text='Player 1:', font='Times 20 bold', bg='white', fg='red', height=1, width=8)
label.grid(row=1, column=0)

label = Label(tk, text='Player 2:', font='Times 20 bold', bg='white', fg='blue', height=1, width=8)
label.grid(row=2)