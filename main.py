from tkinter import *
import pandas as  pd
import random

from pandas.core.interchange.dataframe_protocol import DataFrame

new_word = {}


# get data into pandas and convert to dict
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")

finally:
    to_learn = df.to_dict('records')

print(to_learn)


def show_back():
    global new_word
    english_word = new_word["English"]
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=english_word)

def next_word():
    """ picks a random number key from the dictionary"""
    window.after_cancel(cancel_win)
    global new_word
    new_word = random.choice(to_learn)
    french_word = new_word["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french_word)
    window.after(3000, show_back)

def known_word():
    global to_learn
    to_learn.remove(new_word)
    dframe = pd.DataFrame.from_records(to_learn)
    dframe.to_csv('data/words_to_learn', index=False)
    next_word()


# update the canvas text with the associated value from pick_random for each lanage

BACKGROUND_COLOR = "#B1DDC6"
# setup gui
window = Tk()
window.title("Flash Cards")
window.config(width= 850, height=686,  padx=30, pady=50, bg=BACKGROUND_COLOR)
cancel_win = window.after(3000, show_back, new_word)

# setup buttons
check_img = PhotoImage(file='./images/right.png')
right_button = Button(width=90, height=90, bg=BACKGROUND_COLOR, image=check_img, compound=TOP, highlightthickness=0, command=known_word)
right_button.grid(row=1,column=1)
#
x_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(width=90, height=90, bg=BACKGROUND_COLOR, image=x_img, compound=TOP, highlightthickness=0, command=next_word)
wrong_button.grid(row=1,column=0)

#setup canvas
canvas = Canvas()
back_image = PhotoImage(file='./images/card_back.png')
front_image = PhotoImage(file='./images/card_front.png')
canvas.configure(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image((400, 263), image=front_image)
card_title = canvas.create_text((400, 150), text="", font=("arial", 40, "italic"), fill="black")
card_word = canvas.create_text((400, 250), text="", font=("arial", 60, "normal"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

next_word()



window.mainloop()