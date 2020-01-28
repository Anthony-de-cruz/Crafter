from tkinter import *
import csv

# Initialise Lists
item_name = []
item_amount = []

# Read the CSV file and extra information then appending it to a list
with open('items.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        name = row[0]
        amount = row[1]

        item_name.append(name)
        item_amount.append(amount)


print(item_name)
print(item_amount)


# Initialise the root window
root = Tk()
root.title("Tkinter Listbox & CSV Demontration")
root.geometry('500x300')

Label(root, text="Listbox:", fg='black', font='none 15 bold') .grid(row=0, column=0)

# Create and position frames
frame_listbox = Frame(root)
frame_listbox.grid(row=1, column=0)

# Create and position listbox and scrollbar
scrollbar = Scrollbar(frame_listbox)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame_listbox, height=15, width=25, border=1, yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)


# Create a label to display what has been selected
label_selected_string = StringVar()
label_selected = Label(root, textvariable=label_selected_string, fg='black', font='none 10 bold').grid(row=0, column=1)


# This function is for updating the selection label
def select_item(event):

    index = listbox.curselection()[0]
    label_selected_string.set(item_name[index])


# Binds the listbox to the select_item function
listbox.bind('<<ListboxSelect>>', select_item)

# Create display string
for row in range(len(item_name)):
    listbox.insert(END, item_name[row] + " : " + item_amount[row])


# Create and position delete button
button_delete = Button(root, text="Delete Selection", command=lambda: listbox.delete(ANCHOR), fg='black', font='none 10')
button_delete.grid(row=1, column=1, padx=(10, 0), pady=(10, 0), sticky=N)


root.mainloop()
