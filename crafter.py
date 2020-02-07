from tkinter import *
import csv
from subprocess import call

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

print(item_name)


# -----------------------------------------------------------------------------------
# Create widget containers
# -----------------------------------------------------------------------------------

# Create widget containers
inventory_area = Frame(root)
crafting_area = Frame(root)
crafting_table = Frame(crafting_area)

# Place widget containers
inventory_area.grid(row=1, column=0, sticky=W)
crafting_area.grid(row=1, column=1, sticky=W)
crafting_table.grid(row=0, column=0, sticky=N)


# -----------------------------------------------------------------------------------
# Create title labels
# -----------------------------------------------------------------------------------

# Create inventory label
label_inventory = Label(root, text="Inventory", fg='black', font='none 20 bold')
label_inventory.grid(row=0, column=0, sticky=EW)

# Create crafting-table label
label_crafting_area = Label(root, text="Crafting Table", fg='black', font='none 20 bold')
label_crafting_area.grid(row=0, column=1, sticky=EW)


# -----------------------------------------------------------------------------------
# Create the inventory
# -----------------------------------------------------------------------------------

# Create inventory item heading
label_inventory_item = Label(inventory_area, text="Item : Amount", fg='black', font='none 10 bold')
label_inventory_item.grid(row=0, column=0)

# Create and position listbox and scrollbar
scrollbar = Scrollbar(inventory_area)
scrollbar.grid(row=1, column=1, sticky="news")

listbox = Listbox(inventory_area, height=15, width=25, border=1, yscrollcommand=scrollbar.set)
listbox.grid(row=1, column=0)

scrollbar.config(command=listbox.yview)

# Create display string and populate the listbox
for row in range(len(item_name)):
    listbox.insert(END, item_name[row] + " : " + item_amount[row])


# Create a selected item label
label_selected = Label(inventory_area, text="Selected Item:", fg='black', font='none 10 bold')
label_selected.grid(row=0, column=2, padx=(0, 10))

label_selected_string = StringVar()
label_selected_variable = Label(inventory_area, textvariable=label_selected_string, wraplength=93, fg='black', font='none 10 bold')
label_selected_variable.grid(row=1, column=2, sticky=N)


# This function is for updating the selection label
def select_item(event):

    index = listbox.curselection()[0]
    label_selected_string.set(item_name[index])


# Binds the listbox to the select_item function
listbox.bind('<<ListboxSelect>>', select_item)


# -----------------------------------------------------------------------------------
# Create the crafting system
# -----------------------------------------------------------------------------------

# Crafting table button function
def crafting_table_selection(a):
    print()
    print()
    button_crafting_table[a][1].set(".")
    print(button_crafting_table)
    print(button_crafting_table[a][1])
    print("selection?", select_item)
    print("okay", a)


# Create the list for the crafting table buttons to be stored in
button_crafting_table_string = StringVar()
button_crafting_table = []

for i in range(9):
    button_crafting_table.append([])
    button_crafting_table[i].append(0)
    button_crafting_table[i].append(button_crafting_table_string)

num = 0
print(button_crafting_table)


# Create and position the crafting table buttons
for y in range(3):
    for x in range(3):
        button_crafting_table[x][0] = Button(crafting_table, textvariable=button_crafting_table[num][1],
                                             command=lambda a=num: crafting_table_selection(a), height=2, width=5) .grid(row=y, column=x)
        num += 1


root.mainloop()
