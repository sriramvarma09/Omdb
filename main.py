import json
import os
import base64
from turtle import left
import pandas as pd
import requests as r
from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO
import psutil


def frames():
    global leftframe, rightframe
    leftframe = Frame(bottomframe, bg='#15202b')
    leftframe.pack(side='left')

    rightframe = Frame(bottomframe, bg='#15202b')
    rightframe.pack(side='right')


root = Tk()
root.title('Movie Database')
root.configure(bg='#15202b')
root.geometry('1000x900+400+10')
root.wm_attributes('-transparentcolor', '#15202b')

topframe = Frame(root, bg='#15202b')
topframe.pack(side='top')
bottomframe = Frame(root, bg='#15202b')
bottomframe.pack(side='left')


def dest():
    global leftframe, rightframe
    leftframe.destroy()
    rightframe.destroy()


def getmv():
    frames()
    global poster
    mvname = nameentry.get()
    link = 'http://www.omdbapi.com/?apikey=[APIKEY]&t=' + \
        mvname  # Details of the preferred movie
    mvfetch = r.get(link)
    mvdict = json.loads(mvfetch.text)
    posurl = mvdict['Poster']
    posresponse = r.get(posurl)
    posbyte = posresponse.content
    poster = ImageTk.PhotoImage(Image.open(BytesIO(posbyte)))
    poslabel = Label(rightframe, image=poster, bg='#15202b')
    poslabel.pack(side='right')
    del mvdict['Plot']
    del mvdict['Poster']
    del mvdict['Ratings']

    mvtable = pd.read_json(json.dumps(mvdict), orient='index')
    mvstr = mvtable.to_string()
    mvstr = str(mvstr)
    detlabel = Label(leftframe, text=mvstr, font=(
        'consolas', 10), bg='#15202b', fg='#ffffff')
    detlabel.grid(row=0, column=0)


def boxoffice():
    global leftframe
    mvname = nameentry.get()
    link = 'http://www.omdbapi.com/?apikey=[APIKEY]&t=' + \
        mvname  # Details of the preferred movie
    mvfetch = r.get(link)
    mvdict = json.loads(mvfetch.text)
    amtdoll = mvdict['BoxOffice']

    if amtdoll[0] == '$':
        amtc = mvdict['BoxOffice'].lstrip('$')
        amtc = amtc.split(',')
        amtc = ''.join(amtc)
        amtdoll = "Collections USD : "+amtdoll
        cururl = 'https://api.getgeoapi.com/v2/currency/convert?api_key=[APIKEY]&from=USD&to=INR&format=json&amount='+amtc
        inr = r.get(cururl)
        inrj = inr.json()
        rupstr = '₹'+inrj["rates"]['INR']['rate_for_amount']
        rupstr = "Collections INR : "+rupstr

    else:
        amtc = "N/A"
        rupstr = "N/A"

    dollabel = Label(leftframe, text=amtdoll, font=(
        'consolas', 10), bg='#15202b', fg='#ffffff')
    dollabel.grid(row=1, column=0, padx=0)
    ruplabel = Label(leftframe, text=rupstr, font=(
        'consolas', 10), bg='#15202b', fg='#ffffff')
    ruplabel.grid(row=2, column=0, padx=0)


ttl = Label(topframe, text="Movie Database", font=(
    'consolas', 50), bg='#15202b', fg='#ffffff')
ttl.grid(row=0, column=1)
mvar = StringVar()
mlabel = Label(topframe, text="Enter Movie Name", font=(
    'consolas', 20), bg='#15202b', fg='#fffff9')
mlabel.grid(row=1, column=1, pady=20)
nameentry = Entry(topframe, width=80, border=5, textvariable=mvar,
                  bg='#192734', fg='#ffffff', relief=SUNKEN)
nameentry.grid(row=2, column=1)
chb = Button(root, text="Get movie details", font=(
    'consolas', 10), bg='#6F8FAF', fg='#fffff9', command=getmv)
chb.place(relx=0.23, rely=0.3)
clr = Button(root, text='Clear Screen', font=('consolas', 10),
             bg='#6F8FAF', fg='#fffff9', command=dest)
clr.place(relx=0.44, rely=0.3)
bxob = Button(root, text='Box Office Collections', font=(
    'consolas', 10), bg='#6F8FAF', fg='#fffff9', command=boxoffice)
bxob.place(relx=0.6, rely=0.3)
root.mainloop()
