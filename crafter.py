from tkinter import *
import csv

# Initialise root
root = Tk()
root.title("Crafter")
root.geometry('600x350')
root.resizable(width=FALSE, height=FALSE)

# Create lists
item_name = []
item_amount = []

# Read csv file and append to created lists
with open('items.csv') as itemfile:
    itemlist = csv.reader(itemfile, delimiter=',')

    for row in itemlist:

        name = row[0]
        amount = row[1]

        item_name.append(name)
        item_amount.append(amount)

item_total = (len(item_name))
print(item_name)
print(item_name[2])


def selection_button(item_index):
    print(item_index)


# -----------------------------------------------------------------------------------
# Create widget containers
# -----------------------------------------------------------------------------------
# Create widget containers
inventory = Frame(root)
crafting_table = Frame(root)

# Place widget containers
inventory.grid(row=1, column=0, sticky=W)
crafting_table.grid(row=1, column=1, sticky=W)


# -----------------------------------------------------------------------------------
# Create title labels
# -----------------------------------------------------------------------------------

# Create inventory label
label_inventory = Label(root, text="Inventory", fg='black', font='none 20 bold')
label_inventory.grid(row=0, column=0, sticky=EW)

# Create crafting-table label
label_crafting_table = Label(root, text="Crafting Table", fg='black', font='none 20 bold')
label_crafting_table.grid(row=0, column=1, sticky=EW)


# -----------------------------------------------------------------------------------
# Create the inventory
# -----------------------------------------------------------------------------------

# Create inventory item heading
label_inventory_item = Label(inventory, text="Item : Amount", fg='black', font='none 10 bold')
label_inventory_item.grid(row=0, column=0)

# Create and position listbox and scrollbar
scrollbar = Scrollbar(inventory)
scrollbar.grid(row=1, column=1, sticky="news")

listbox = Listbox(inventory, height=15, width=25, border=1, yscrollcommand=scrollbar.set)
listbox.grid(row=1, column=0)

scrollbar.config(command=listbox.yview)

# Create display string and populate the listbox
for row in range(len(item_name)):
    listbox.insert(END, item_name[row] + " : " + item_amount[row])


# Create a selected item label
label_selected = Label(inventory, text="Selected Item:", fg='black', font='none 10 bold')
label_selected.grid(row=0, column=2, padx=(0, 10))

label_selected_string = StringVar()
label_selected_variable = Label(inventory, textvariable=label_selected_string, wraplength=93, fg='black', font='none 10 bold')
label_selected_variable.grid(row=1, column=2, sticky=N)


# This function is for updating the selection label
def select_item(event):

    index = listbox.curselection()[0]
    label_selected_string.set(item_name[index])


# Binds the listbox to the select_item function
listbox.bind('<<ListboxSelect>>', select_item)


root.mainloop()
