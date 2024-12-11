import tkinter as tk
from tkinter import messagebox

#address dictionary
AddressDictionary={
    
}

#functions

def addtodictionary():
    globaldictionary=


#window

window=tk.Tk()
window.title("Address Book")
window.geometry("700x700")

addressbooklabel=tk.Label(window, text="My Address Book: ", font=("Arial", 12), bg="lightgrey")
addressbooklabel.place(x=180,y=0)
#listbox

listbox=tk.Listbox(window, width=50, height=25)
listbox.place(x=10,y=50)

#buttons

openFile=tk.Button(window, text="Open file", bd=2, width=10, bg="lightgrey")
openFile.place(x=350, y=0)

savefile=tk.Button(window, text="Save file", bd=2, width=25, bg="lightgrey")
savefile.place(x=250, y=650)

delete=tk.Button(window, text="Delete", bd=2, width=15, bg="lightgrey")
delete.place(x=200, y=475)

edit=tk.Button(window, text="Edit", bd=2, width=15, bg="lightgrey")
edit.place(x=10, y=475)

Update=tk.Button(window, text="Update/Add", bd=2, width=15, bg="lightgrey")
Update.place(x=500, y=375)


#secondary labels
firstnamelabel=tk.Label(window, text="First name:", font=("Arial", 10), bg="lightgrey")
firstnamelabel.place(x=400, y=75)

addresslabel=tk.Label(window,text="Address:", font=("Arial", 10), bg="lightgrey")    
addresslabel.place(x=400, y=125)

mobilelabel=tk.Label(window, text="Mobile:", font=("Arial", 10), bg="lightgrey")    
mobilelabel.place(x=400, y=175)

emaillabel=tk.Label(window ,text="Email:", font=("Arial", 10), bg="lightgrey")  
emaillabel.place(x=400, y=225)  

birthdaylabel=tk.Label(window,text="Address:", font=("Arial", 10), bg="lightgrey")    
birthdaylabel.place(x=400, y=275)

#entries for ^^^

firstnameentry=tk.Entry(window, width=20, bd=2)
firstnameentry.place(x=500,y=75)

addressentry=tk.Entry(window, width=20, bd=2)
addressentry.place(x=500,y=125)

mobileentry=tk.Entry(window, width=20, bd=2)
mobileentry.place(x=500,y=175)

emailentry=tk.Entry(window, width=20, bd=2)
emailentry.place(x=500,y=225)

birthdayentry=tk.Entry(window, width=20, bd=2)
birthdayentry.place(x=500,y=275)

window.mainloop()