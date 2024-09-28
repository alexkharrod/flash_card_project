from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"
# setup gui
window = Tk()
window.title("Flash Cards")
window.config(width=850, height=676,bg=BACKGROUND_COLOR)

# setup card canvas

canvas = Canvas(bg="white", highlightthickness=0)

canvas.place(width=800, height=526, x=25, y=20)

# setup Word Labels
language_label = Label(text="French",bg='white', fg="black",justify=LEFT,  font=("arial", 40, "italic"))
language_label.place(x=360, y=150)

word_label = Label(text="Word",bg='white', fg="black",justify=LEFT, font=("arial", 60, "bold"))
word_label.place(x=360, y=250)


# setup buttons
check_img = PhotoImage(file='./images/right.png')
check_button = Button(width=90, height=90, bg=BACKGROUND_COLOR, image=check_img, compound=TOP, highlightthickness=0)
check_button.place(x=580, y=560)

x_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(width=90, height=90, bg=BACKGROUND_COLOR, image=x_img, compound=TOP, highlightthickness=0)
wrong_button.place(x=180, y=560)












window.mainloop()