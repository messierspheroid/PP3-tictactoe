from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic Tac Toe")

# canvas = Canvas(window, width=835, height=835)
# background_png = PhotoImage(file="background_618x618.png")
# canvas.create_image(420, 420, image=background_png)
# canvas.grid()

# x_shape = PhotoImage(file="x_shape.png", width=230)
# o_shape = PhotoImage(file="o_shape.png", width=230)
# x = canvas.create_image(image=x_shape)
# o = canvas.create_image(image=o_shape)

clicked = True
count = 0


def disable_all_buttons():
    button_0_0.config(state=DISABLED)
    button_0_1.config(state=DISABLED)
    button_0_2.config(state=DISABLED)
    button_1_0.config(state=DISABLED)
    button_1_1.config(state=DISABLED)
    button_1_2.config(state=DISABLED)
    button_2_0.config(state=DISABLED)
    button_2_1.config(state=DISABLED)
    button_2_2.config(state=DISABLED)


def checkifwon():
    global winner
    winner = False

    if button_0_0["text"] == "X" and button_0_1["text"] == "X" and button_0_2["text"] == "X":
        button_0_0.config(bg="red")
        button_0_1.config(bg="red")
        button_0_2.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
        disable_all_buttons()

    elif button_0_0["text"] == "X" and button_1_1["text"] == "X" and button_2_2["text"] == "X":
        button_0_0.config(bg="red")
        button_1_1.config(bg="red")
        button_2_2.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
        disable_all_buttons()

    elif button_0_2["text"] == "X" and button_1_1["text"] == "X" and button_2_0["text"] == "X":
        button_0_2.config(bg="red")
        button_1_1.config(bg="red")
        button_2_0.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
        disable_all_buttons()

    elif button_2_0["text"] == "X" and button_2_1["text"] == "X" and button_2_2["text"] == "X":
        button_2_0.config(bg="red")
        button_2_1.config(bg="red")
        button_2_2.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
        disable_all_buttons()

    elif button_0_2["text"] == "X" and button_1_2["text"] == "X" and button_2_2["text"] == "X":
        button_0_2.config(bg="red")
        button_1_2.config(bg="red")
        button_2_2.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
        disable_all_buttons()

    elif button_0_0["text"] == "X" and button_1_0["text"] == "X" and button_2_0["text"] == "X":
        button_0_0.config(bg="red")
        button_1_0.config(bg="red")
        button_2_0.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins!")
        disable_all_buttons()
        
    # check for O win
    if button_0_0["text"] == "O" and button_0_1["text"] == "O" and button_0_2["text"] == "O":
        button_0_0.config(bg="red")
        button_0_1.config(bg="red")
        button_0_2.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins!")
        disable_all_buttons()

    elif button_0_0["text"] == "O" and button_1_1["text"] == "O" and button_2_2["text"] == "O":
        button_0_0.config(bg="red")
        button_1_1.config(bg="red")
        button_2_2.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins!")
        disable_all_buttons()

    elif button_0_2["text"] == "O" and button_1_1["text"] == "O" and button_2_0["text"] == "O":
        button_0_2.config(bg="red")
        button_1_1.config(bg="red")
        button_2_0.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins!")
        disable_all_buttons()

    elif button_2_0["text"] == "O" and button_2_1["text"] == "O" and button_2_2["text"] == "O":
        button_2_0.config(bg="red")
        button_2_1.config(bg="red")
        button_2_2.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins!")
        disable_all_buttons()

    elif button_0_2["text"] == "O" and button_1_2["text"] == "O" and button_2_2["text"] == "O":
        button_0_2.config(bg="red")
        button_1_2.config(bg="red")
        button_2_2.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins!")
        disable_all_buttons()

    elif button_0_0["text"] == "O" and button_1_0["text"] == "O" and button_2_0["text"] == "O":
        button_0_0.config(bg="red")
        button_1_0.config(bg="red")
        button_2_0.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins!")
        disable_all_buttons()

    # check if tie
    else:
        if count == 9 and winner == False:
            messagebox.showinfo("Tic Tac Toe", "It's a Tie\nNo one wins!")
            disable_all_buttons()


def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()

    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()

    else:
        messagebox.showerror("Tic Tac Toe", "Hey, that box has already been selected\nPick another box.")


def reset():
    global clicked, count
    global button_0_0, button_0_1, button_0_2, button_1_0, button_1_1, button_1_2, button_2_0, button_2_1, button_2_2
    clicked = True
    count = 0
    # row 0
    button_0_0 = Button(window, text=" ", font=("Helvetica", 20), height=7, width=14, bg="SystemButtonFace",
                        command=lambda: b_click(button_0_0))
    button_0_0.grid(row=0, column=0)
    button_0_1 = Button(window, text=" ", font=("Helvetica", 20), height=7, width=14, bg="SystemButtonFace",
                        command=lambda: b_click(button_0_1))
    button_0_1.grid(row=0, column=1)
    button_0_2 = Button(window, text=" ", font=("Helvetica", 20), height=7, width=14, bg="SystemButtonFace",
                        command=lambda: b_click(button_0_2))
    button_0_2.grid(row=0, column=2)

    # row 1
    button_1_0 = Button(window, text=" ", font=("Helvetica", 20), height=7, width=14, bg="SystemButtonFace",
                        command=lambda: b_click(button_1_0))
    button_1_0.grid(row=1, column=0)
    button_1_1 = Button(window, text=" ", font=("Helvetica", 20), height=7, width=14, bg="SystemButtonFace",
                        command=lambda: b_click(button_1_1))
    button_1_1.grid(row=1, column=1)
    button_1_2 = Button(window, text=" ", font=("Helvetica", 20), height=7, width=14, bg="SystemButtonFace",
                        command=lambda: b_click(button_1_2))
    button_1_2.grid(row=1, column=2)

    # row 2
    button_2_0 = Button(window, text=" ", font=("Helvetica", 20), height=7, width=14, bg="SystemButtonFace",
                        command=lambda: b_click(button_2_0))
    button_2_0.grid(row=2, column=0)
    button_2_1 = Button(window, text=" ", font=("Helvetica", 20), height=7, width=14, bg="SystemButtonFace",
                        command=lambda: b_click(button_2_1))
    button_2_1.grid(row=2, column=1)
    button_2_2 = Button(window, text=" ", font=("Helvetica", 20), height=7, width=14, bg="SystemButtonFace",
                        command=lambda: b_click(button_2_2))
    button_2_2.grid(row=2, column=2)


my_menu = Menu(window)
window.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()
window.mainloop()
