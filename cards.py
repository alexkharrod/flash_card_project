from tkinter import Canvas, PhotoImage
BACKGROUND_COLOR = "#B1DDC6"


class Cards(Canvas):
    def __init__(self):
        super().__init__()
        self.back = PhotoImage(file='./images/card_back.png')
        self.front = PhotoImage(file='./images/card_front.png')
        self.configure(width=800, height = 526, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.place(x=0, y=0)



    def show_back(self):
        self.create_image((400, 263), image=self.back)

