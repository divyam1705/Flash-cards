BACKGROUND_COLOR = "#B1DDC6"
import pandas
from tkinter import *
from random import randint
w1=Tk()
w1.title("FLASHCARDS")
w1.minsize(900,625)
w1.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
canvas=Canvas(width=800,height=525,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.grid(column=1,row=0)
wrongimg=PhotoImage(file="./images/wrong.png")
rightimg=PhotoImage(file="./images/right.png")

data=pandas.read_csv("wordstolearn.csv")  #CHANGE TO ADD NEW WORDS
randomwords=None
front = PhotoImage(file="card_front.png")
x=canvas.create_image(400, 265, image=front)
y=canvas.create_text(400, 100, text="French", font=("Arial", 40, "italic"))
z=canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
back = PhotoImage(file="card_back.png")
def change(w):
    global eword,x,y,z,back
    canvas.itemconfig(x, image=back)  # (400,265)
    canvas.itemconfig(y,text="English",fill="#FFFFFF")
    canvas.itemconfig(z, text=w,fill="#FFFFFF")

fwords=data["French"].to_list()
ewords=data["English"].to_list()
randomwords = randint(0, len(fwords)-1)
timer1=0
def play():
    global front,y,x,z,fwords,ewords,randomwords
    global timer1
    fword = fwords[randomwords]
    eword = ewords[randomwords]
    canvas.itemconfig(x,image=front)
    canvas.itemconfig(y, text="French",fill="#000000")
    canvas.itemconfig(z, text=fword, fill="#000000")
    timer1=w1.after(3000,change,eword)

play()
def right():
    global data,randomwords,ewords,fwords,timer1
    w1.after_cancel(timer1)
    ewords.pop(randomwords)
    fwords.pop(randomwords)
    randomwords=randint(0, len(ewords))
    with open("wordstolearn.csv", "w") as f:
        wtl = pandas.DataFrame({"French": fwords, "English": ewords})
        wtl.to_csv("wordstolearn.csv",index=False)
    play()
def wrong():
    global randomwords,fwords
    randomwords=randint(0, len(fwords))
    play()
wrongbut=Button(image=wrongimg,highlightthickness=0,command=wrong)
wrongbut.grid(column=0,row=1)
rightbut=Button(image=rightimg,highlightthickness=0,command=right)
rightbut.grid(column=2,row=1)






w1.mainloop()
