from bs4 import BeautifulSoup
from tkinter import *
import urllib.request
import requests 
import random
from PIL import Image,ImageTk
import os


def search():
    global user_input,screen,img
    link = "https://www.flaticon.com/free-icons/"+user_input.get()
    info = requests.get(link)
    contents = info.content
    soup = BeautifulSoup(contents,'html5lib')
    imgs = soup.find_all("img")
    random_image = random.choice(imgs)
    urllib.request.urlretrieve(random_image['src'],"gfg.png")
    img =  ImageTk.PhotoImage(Image.open("gfg.png"))
    screen.config(image=img)
    # print(random_image['src'])
def delete():
    os.remove("gfg.png")
    win.destroy()
win = Tk()

win.protocol("WM_DELETE_WINDOW",delete)
user_input = Entry(win,width=40,font=("Arial",23))
subButton = Button(win,font=("Arial",23),text="Submit",command=search)

user_input.grid(row=0,column=0)
subButton.grid(row=0,column=1)

screen = Label(win)
screen.grid(row=1,column=0)


win.mainloop()
