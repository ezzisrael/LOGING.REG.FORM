from tkinter import *
from tkinter import ttk

class Main(object):
    def __init__(self,master):
        self.master = master
    
#TOP FRAME
        mainFrame = Frame(self.master)
        mainFrame.pack()
        topFrame = Frame(mainFrame, 
        width=1350, 
        height=70, 
        bg='gray',
        padx= 20, 
        relief=SUNKEN, 
        borderwidth=2
        )
        topFrame.pack(side=TOP,fill=X)
#CENTER FRAME
        centerFrame = Frame(mainFrame, 
        width= 1350,
        relief= RIDGE,
        bg= '#e0f0f0',
        height= 680
        )
        centerFrame.pack(side=TOP)
#CENTER LEFT FRAME
        centerLeftFrame = Frame(centerFrame,
        width= 900,
        height=700,
        bg='light blue',
        borderwidth= 2,
        relief= SUNKEN
        )
        centerLeftFrame.pack(side=LEFT)
#CENTER RIGHT FRAME
        centerRightFrame = Frame(centerFrame, 
        width=450, 
        height=700, 
        bg='orange',
        relief= SUNKEN
        )
        centerRightFrame.pack()
#SEARCH BAR
        search_bar = LabelFrame(centerRightFrame,
        width=440,
        height=175,
        text='Search Box',
        bg='#9bc9ff'
        )
        search_bar.pack(fill=BOTH)
#LIST
        list_bar =LabelFrame(centerRightFrame,
        width=400,
        height=175,
        text='List Box',
        bg='brown'
        )
        list_bar.pack(fill=BOTH)
#ADD BOOK
        self.iconbook=PhotoImage(file='C:/Users/Umoren Joshua/3D Objects/Books-red-32.png')
        self.btnbook= Button(topFrame,
        text='Add Book',
        image=self.iconbook,
        compound=LEFT,
        font='ar 12 bold'
        )
        self.btnbook.pack(side=LEFT, padx=10)
#ADD MEMBER
        self.iconmember= PhotoImage(file='C:/Users/Umoren Joshua/3D Objects/User-Group-icon (2).png')
        self.btnmember= Button(topFrame,
        text='Add member',
        font='ar 12 bold',
        padx=10
        )
        self.btnmember.configure(image=self.iconmember,
        compound= LEFT
        )
        self.btnmember.pack(side=LEFT)
#GIVE BOOK
        self.icongive=PhotoImage(file='C:/Users/Umoren Joshua/Music/Marvel-Book-icon (1).png')
        self.btngive= Button(topFrame,
        text= 'Add Member',
        font= 'ar 12 bold',
        padx= 10
        )

def main():
    root = Tk()
    app = Main(root)
    root.title('Library Management System')
    root.geometry('1350x750+350+200')
    root.iconbitmap(r'C:/Users/Umoren Joshua/Downloads/Library-48.png')
    root.mainloop()

if __name__ == '__main__':
    main()
