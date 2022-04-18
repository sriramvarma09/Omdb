from logging import root
from msilib.schema import PatchPackage
from tkinter import PhotoImage
import requests as r
from tkinter import *
import base64
from PIL import ImageTk,Image
from io import BytesIO
root=Tk()
root.geometry('600x600')
link='https://m.media-amazon.com/images/M/MV5BMTYwNjAyODIyMF5BMl5BanBnXkFtZTYwNDMwMDk2._V1_SX300.jpg'
x=r.get(link)
con=x.content

img=ImageTk.PhotoImage(Image.open(BytesIO(con)))

imgl=Label(root,image=img)
imgl.pack()

#bytdata=base64.encodestring(con)
#yy=PhotoImage(data=bytdata)



root.mainloop()
