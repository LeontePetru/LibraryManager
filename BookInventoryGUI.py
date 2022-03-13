
import tkinter as tk
from tkinter import ttk, CENTER
from tkinter.messagebox import showinfo
from BookPresententer import BookPresenter

#WIDTH = 1280
#HEIGHT = 720

root = tk.Tk()
root.geometry('1280x720')

background_image = tk.PhotoImage(file='.\Images\BookInventoryGUI.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

canvas=tk.Canvas(root)
canvas.place(relx=0.175,rely=0.2,relheight=0.3,relwidth=0.65)


tv = ttk.Treeview(canvas,selectmode='browse')
vsb = ttk.Scrollbar(orient="vertical", command=tv.yview)
tv.configure(yscrollcommand=vsb.set)


tv['columns']=('number', 'title', 'author','isbn','genre','publisher','inventoryNumber','state')

tv.column('#0',width=0)
tv.column('number', anchor=CENTER,width=30)
tv.column('title', anchor=CENTER,width=180)
tv.column('author', anchor=CENTER,width=120)
tv.column('isbn', anchor=CENTER,width=100)
tv.column('genre', anchor=CENTER,width=100)
tv.column('publisher', anchor=CENTER,width=130)
tv.column('inventoryNumber', anchor=CENTER,width=70)
tv.column('state', anchor=CENTER,width=100)

tv.heading('number', text='No#', anchor=CENTER)
tv.heading('title', text='Title', anchor=CENTER)
tv.heading('author', text='Author', anchor=CENTER)
tv.heading('isbn', text='ISBN', anchor=CENTER)
tv.heading('genre', text='Genre', anchor=CENTER)
tv.heading('publisher', text='Publisher', anchor=CENTER)
tv.heading('inventoryNumber', text='InvNo#', anchor=CENTER)
tv.heading('state', text='Status', anchor=CENTER)


presenter= BookPresenter()
bookData=presenter.stringOfBooks()
n=bookData.__len__()
index=-1

for i in range(n):
    index=index+1
    #for j in range(7):
    tv.insert(parent='',index=index,iid=index,values=(index,bookData[i][0],bookData[i][1],bookData[i][2],bookData[i][3],
                                                      bookData[i][4],bookData[i][5],bookData[i][6]))

tv.pack()


root.mainloop()