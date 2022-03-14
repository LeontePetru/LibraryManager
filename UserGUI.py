
import tkinter as tk
from tkinter import ttk, CENTER
from tkinter.messagebox import showinfo
from BookPresententer import BookPresenter
import tkinter.font as tkFont

class GUIUser:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1280x720')
        self.background_image = tk.PhotoImage(file='.\Images\BookInventoryGUI.png')
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1,relheight=1)

        presenter= BookPresenter()
        bookData=presenter.stringOfBooks()
        n=bookData.__len__()

        genres = presenter.genres
        states = presenter.states
        publishers = presenter.publishers
        authors = presenter.authors

        font = tkFont.Font(family="Times New Roman",size=12,weight="bold")

        selectGenres = ttk.Combobox(self.root,font=(12),foreground="#ff6366",background="#cccccc")
        selectGenres['values'] = genres
        selectGenres.current(0)
        selectGenres.place(relx=0.025,rely=0.2,relheight=0.04,relwidth=0.125)

        selectAuthors = ttk.Combobox(self.root,font=(12),foreground="#ff6366",background="#cccccc")
        selectAuthors['values'] = authors
        selectAuthors.current(0)
        selectAuthors.place(relx=0.025,rely=0.26,relheight=0.04,relwidth=0.125)

        selectPublishers = ttk.Combobox(self.root,font=(12),foreground="#ff6366",background="#cccccc")
        selectPublishers['values'] = publishers
        selectPublishers.current(0)
        selectPublishers.place(relx=0.025,rely=0.32,relheight=0.04,relwidth=0.125)

        selectStates = ttk.Combobox(self.root,font=(12),foreground="#ff6366",background="#cccccc")
        selectStates['values'] = states
        selectStates.current(0)
        selectStates.place(relx=0.025,rely=0.38,relheight=0.04,relwidth=0.125)

        titleEntry=tk.Entry(bg="#cccccc",font=font)
        titleEntry.place(relx=0.835,rely=0.245,relheight=0.06,relwidth=0.155)

        def sortButtonFunc():
            sortParameters =[]
            sortGenres=selectGenres.get()
            sortParameters.append(sortGenres)
            sortStates = selectStates.get()
            sortParameters.append(sortStates)
            sortPublishers = selectPublishers.get()
            sortParameters.append(sortPublishers)
            sortAuthors = selectAuthors.get()
            sortParameters.append(sortAuthors)
            createTable(presenter.sortedListOfStrings(sortParameters))

        def searchByTitle():
            createTable(presenter.nameSortedListOfStrings(titleEntry.get()))

        sortButton=tk.Button(font=(12),text="Sort by",command=sortButtonFunc,foreground="#ff6366",bg="#cccccc")
        sortButton.place(relx=0.025,rely=0.44,relheight=0.04,relwidth=0.125)
        sortButton=tk.Button(font=(12),text="Search title",command=searchByTitle,foreground="#ff6366",bg="#cccccc")
        sortButton.place(relx=0.835,rely=0.32,relheight=0.06,relwidth=0.155)

        def createTable(data):
            canvas = tk.Canvas(self.root)
            canvas.place(relx=0.175, rely=0.2, relheight=0.28, relwidth=0.65)

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

            index=-1
            bookData=data
            n1=bookData.__len__()

            for i in range(n1):
                index = index + 1
                tv.insert(parent='',index=index,iid=index,values=(index,bookData[i][0],bookData[i][1],bookData[i][2],
                                                                            bookData[i][3],bookData[i][4],bookData[i][5],bookData[i][6]))
            tv.pack()

        createTable(presenter.stringOfBooks())
        #self.root.mainloop()

    def getRoot(self):
        return self.root

class GUILogIn:

    def __init__(self):
        self.root = tk.Canvas
        #self.root.geometry('1280x720')

        self.background_image = tk.PhotoImage(file='.\Images\LogIn.png')
        self.background_label = tk.Label(image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)
        self.status=0

        font = tkFont.Font(family="Times New Roman", size=16, weight="bold")

        userEntry = tk.Entry(bg="#cccccc", font=font)
        userEntry.place(relx=0.65, rely=0.525, relheight=0.06, relwidth=0.23)

        passwordEntry = tk.Entry(bg="#cccccc", font=font)
        passwordEntry.place(relx=0.65, rely=0.68, relheight=0.06, relwidth=0.23)

        def buttonLogInFunc(self):
            print(userEntry.get())
            print(passwordEntry.get())

        def Guest(self):
            print(1)

          #  os.system('BookInventoryGUI.py')
           # # root.destroy()

        logInButton = tk.Button(bg="#cccccc", font=font, text="Log In", command=buttonLogInFunc, foreground="#ff6366")
        logInButton.place(relx=0.675, rely=0.77, relheight=0.06, relwidth=0.18)

        guestButton = tk.Button(bg="#cccccc", font=font, text="Continue as Guest", command=lambda:Guest(self), foreground="#ff6366")
        guestButton.place(relx=0.675, rely=0.86, relheight=0.06, relwidth=0.18)

    # passwordEntry.pack()
        #self.root.mainloop()

    def getRoot(self):
        return self.root

    def getStatus(self):
        return self.status


ws=tk.Tk()
gui=GUILogIn()
gui.getRoot().place(relx=0,rely=0,width=1,height=1)
ws.mainloop()

