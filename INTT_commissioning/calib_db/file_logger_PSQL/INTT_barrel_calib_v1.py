# test
import tkinter as tk
import glob, os
from tkinter import filedialog

def print_selection():
    print("Selected number:", var_ladder.get())

def simple_print(*args,var_barrel):
    print("aaa",var_barrel)


def update_dropdown(*args,var_barrel,var_ladder,dropdown_ladder):
    print("button feedback : ",var_barrel)
    if (var_barrel == "B0L0" or var_barrel == "B0L1" or var_barrel == "NaN ") :
        opt_ladder = ["00", "01", "02","03","04","05","06","07","08","09","10","11"]
    else:
        opt_ladder = ["00", "01", "02","03","04","05","06","07","08","09","10","11","12","13","14","15"]
    var_ladder.set(opt_ladder[0])
    
    # note : so it deletes the items in the list, and use the for loop to add them back, one by one.
    dropdown_ladder['menu'].delete(0, 'end')
    for option in opt_ladder:
        dropdown_ladder['menu'].add_command(label=option, command=tk._setit(var_ladder, option))


def print_all():

    ROC1_check_tag = 0
    ROC2_check_tag = 0

    print("====================================================================================")
    print("File name :", file_name_entry.get(), "Side :", var_NS.get())
    
    for i in range (8) :
        if (var_barrel[i].get() != "NaN "):
            ROC1_check_tag = 1
            break

    for i in range (8) :
        if (var_barrel_2[i].get() != "NaN "):
            ROC2_check_tag = 1
            break

    if (ROC1_check_tag == 1):
        for i in range (8) :
            if (var_barrel[i].get() != "NaN ") :
                print("ROC :",ROC1_entry.get(),"ID :",i+1,"Ladder :", var_barrel[i].get()+var_ladder[i].get(),"module_ID :",var_module[i].get())

    
    if (ROC2_check_tag == 1):
        print(" ")
        for i in range (8) :
            if (var_barrel_2[i].get() != "NaN ") :
                print("ROC :",ROC2_entry.get(),"ID :",i+1,"Ladder :", var_barrel_2[i].get()+var_ladder_2[i].get(),"module_ID :",var_module_2[i].get())

    if (note1_entry.get() != " "):
        print(" ")
        print(note1_entry.get())
    if (note2_entry.get() != " "):
        print(" ")
        print(note2_entry.get())
    if (note3_entry.get() != " "):
        print(" ")
        print(note3_entry.get())
    # for i in var_barrel :
    #     print(i.get())
    
    # for il in var_ladder :
    #     print(il.get())


def reset_all():
    file_name_entry.delete(0, 'end')
    ROC1_entry.delete(0, 'end')
    ROC2_entry.delete(0, 'end')
    note1_entry.delete(0,'end')
    note2_entry.delete(0,'end')
    note3_entry.delete(0,'end')

    var_NS.set(opt_NS[0])
    dropdown_NS['menu'].delete(0, 'end')
    for option_NS in opt_NS :
        dropdown_NS['menu'].add_command(label=option_NS, command=tk._setit(var_NS, option_NS))

    for i in range (8) :
        var_ladder[i].set(opt_ladder[0])
        dropdown_ladder_list[i]['menu'].delete(0, 'end')

        var_ladder_2[i].set(opt_ladder[0])
        dropdown_ladder_list_2[i]['menu'].delete(0, 'end')

        for option in opt_ladder:
            dropdown_ladder_list  [i]['menu'].add_command(label=option, command=tk._setit(var_ladder[i], option))
            dropdown_ladder_list_2[i]['menu'].add_command(label=option, command=tk._setit(var_ladder_2[i], option))
        

        var_barrel[i].set(opt_barrrel[0])
        dropdown_barrel['menu'].delete(0, 'end')

        var_barrel_2[i].set(opt_barrrel[0])
        dropdown_barrel_2['menu'].delete(0, 'end')

        for option in opt_barrrel:
            dropdown_barrel  ['menu'].add_command(label=option, command=tk._setit(var_barrel[i], option))
            dropdown_barrel_2['menu'].add_command(label=option, command=tk._setit(var_barrel_2[i], option))
            # dropdown_barrel_2['menu'].add_command(command=lambda value_2, i=i: update_dropdown(var_barrel = value_2, var_ladder = var_ladder_2[i],dropdown_ladder=dropdown_ladder_list_2[i]))
            

        
        var_module[i].set(opt_module[0])
        dropdown_module['menu'].delete(0, 'end')

        var_module_2[i].set(opt_module[0])
        dropdown_module_2['menu'].delete(0, 'end')

        for option in opt_module:
            dropdown_module['menu'].add_command(label=option, command=tk._setit(var_module[i], option))
            dropdown_module_2['menu'].add_command(label=option, command=tk._setit(var_module_2[i], option))


def find_latest_file():
    file_directory = "/home/inttdev/work/cwshih/calib_db/fake_folder/"
    list_of_files = glob.glob(file_directory+"aa_*.c")
    latest_file = max(list_of_files, key=os.path.getctime)
    latest_file = latest_file.replace(file_directory,'')

    return latest_file

def update_file_latest ():
    file_name_entry.delete(0,'end')
    file_name_entry.insert('end', find_latest_file())


def browse_file():
    file_path = filedialog.askopenfilename()
    file_name_entry.delete(0,'end')
    file_name_entry.insert('end', file_path)


# note : create tkinter window
root = tk.Tk()
root.title("INTT Commissioning, Barrel calibration test")
root.geometry("1000x500")





ladder_text = ["Ladder1", "Ladder2", "Ladder3", "Ladder4", "Ladder5", "Ladder6", "Ladder7","Ladder8"]
roc_text = ["ROC1", "ROC2"]
file_name_text = "File name : "
module_text = "module id "
NS_text = "North or South : "

opt_barrrel = ["NaN ","B0L0","B0L1","B1L0","B1L1"]
opt_ladder  = ["00", "01", "02","03","04","05","06","07","08","09","10","11"]
opt_module  = [0,1,2,3,4,5,6]
opt_NS      = ["NaN","N","S"]

var_barrel = [tk.StringVar(root) for i in range(len(ladder_text))]
var_ladder = [tk.StringVar(root) for i in range(len(ladder_text))]
var_module = [tk.StringVar(root) for i in range(len(ladder_text))]
dropdown_barrel_list = []
dropdown_module_list = []
dropdown_ladder_list = []


var_barrel_2 = [tk.StringVar(root) for i in range(len(ladder_text))]
var_ladder_2 = [tk.StringVar(root) for i in range(len(ladder_text))]
var_module_2 = [tk.StringVar(root) for i in range(len(ladder_text))]
dropdown_barrel_list_2 = []
dropdown_module_list_2 = []
dropdown_ladder_list_2 = []




n_row = 1
# note : for file name 
file_name_label = tk.Label(root, text=file_name_text)
file_name_label.grid(row=n_row, column=1)

file_name_entry = tk.Entry(root,width=20,textvariable=tk.StringVar(value=""))
file_name_entry.grid(row=n_row, column=2, columnspan = 3)

button_latest = tk.Button(root, text="Latest", fg='black', command=update_file_latest)
button_latest.grid(row=n_row, column=5 )

button_browse = tk.Button(root, text="Find", fg='black', command=browse_file)
button_browse.grid(row=n_row, column=6 )

# note : for the N or S
NS_label = tk.Label(root, text=NS_text)
NS_label.grid(row=n_row, column=7)

# set initial value for menu
var_NS = tk.StringVar(root)
var_NS.set(opt_NS[0])

# create menu with options
dropdown_NS = tk.OptionMenu(root, var_NS, *opt_NS)
dropdown_NS.grid(row=n_row,column=8)

# ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= =========

n_row += 1
separate_bar1 = tk.Label(root, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------")
separate_bar1.grid(row=n_row, column = 1, columnspan = 10)

# ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= =========

# note : create 7 ladders selections
n_row += 1
n_column = 1

ROC1_label = tk.Label(root, text=roc_text[0])
ROC1_label.grid(row=n_row, column=n_column,padx=20)

ROC1_entry = tk.Entry(root,width=10,textvariable=tk.StringVar(value=""))
ROC1_entry.grid(row=n_row+1, column=n_column, rowspan = 2, padx=20)


for i in range( len(ladder_text) ):

    # set initial value for menu
    var_ladder[i].set(opt_ladder[0])

    # create menu with options
    dropdown_ladder = tk.OptionMenu(root, var_ladder[i], *opt_ladder)
    dropdown_ladder.grid(row=n_row+2,column=n_column+i+2)
    dropdown_ladder_list.append(dropdown_ladder)

for i in range( len(ladder_text) ):
    # create label for menu
    label_barrel = tk.Label(root, text=ladder_text[i])
    label_barrel.grid(row=n_row,column=n_column+i+2)

    # set initial value for menu
    var_barrel[i].set(opt_barrrel[0])

    # create menu with options
    dropdown_barrel = tk.OptionMenu(root, var_barrel[i], *opt_barrrel,command=lambda value, i=i: update_dropdown(var_barrel = value, var_ladder = var_ladder[i],dropdown_ladder=dropdown_ladder_list[i]))
    dropdown_barrel.grid(row=n_row+1,column=n_column+i+2)

n_row += 3
for i in range( len(ladder_text) ):
    # create label for menu
    label_module = tk.Label(root, text=module_text)
    label_module.grid(row=n_row,column=n_column+i+2)

    # set initial value for menu
    var_module[i].set(opt_module[0])

    # create menu with options
    dropdown_module = tk.OptionMenu(root, var_module[i], *opt_module)
    dropdown_module.grid(row=n_row+1,column=n_column+i+2)

# ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= =========

n_row += 2
separate_bar2 = tk.Label(root, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------")
separate_bar2.grid(row=n_row, column = 1, columnspan = 10)

# ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= =========


# note : ==================================================================================================================================
n_row += 2
ROC2_label = tk.Label(root, text=roc_text[1])
ROC2_label.grid(row=n_row, column=n_column,padx=20)

ROC2_entry = tk.Entry(root,width=10,textvariable=tk.StringVar(value=""))
ROC2_entry.grid(row=n_row+1, column=n_column, rowspan = 2, padx=20)


for i in range( len(ladder_text) ):

    # set initial value for menu
    var_ladder_2[i].set(opt_ladder[0])

    # create menu with options
    dropdown_ladder_2 = tk.OptionMenu(root, var_ladder_2[i], *opt_ladder)
    dropdown_ladder_2.grid(row=n_row+2,column=n_column+i+2)
    dropdown_ladder_list_2.append(dropdown_ladder_2)

for i in range( len(ladder_text) ):
    # create label for menu
    label_barrel_2 = tk.Label(root, text=ladder_text[i])
    label_barrel_2.grid(row=n_row,column=n_column+i+2)

    # set initial value for menu
    var_barrel_2[i].set(opt_barrrel[0])

    # create menu with options
    dropdown_barrel_2 = tk.OptionMenu(root, var_barrel_2[i], *opt_barrrel,command=lambda value_2, i=i: update_dropdown(var_barrel = value_2, var_ladder = var_ladder_2[i],dropdown_ladder=dropdown_ladder_list_2[i]))
    dropdown_barrel_2.grid(row=n_row+1,column=n_column+i+2)

n_row += 3
for i in range( len(ladder_text) ):
    # create label for menu
    label_module_2 = tk.Label(root, text=module_text)
    label_module_2.grid(row=n_row,column=n_column+i+2)

    # set initial value for menu
    var_module_2[i].set(opt_module[0])

    # create menu with options
    dropdown_module_2 = tk.OptionMenu(root, var_module_2[i], *opt_module)
    dropdown_module_2.grid(row=n_row+1,column=n_column+i+2)







# ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= =========

n_row += 2
separate_bar3 = tk.Label(root, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------")
separate_bar3.grid(row=n_row, column = 1, columnspan = 10)

# ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= ========= =========


# note : for file name 
n_row += 3
note1_label = tk.Label(root, text="Note 1 : ")
note1_label.grid(row=n_row, column=1)

note1_entry = tk.Entry(root,width=95,textvariable=tk.StringVar(value=" "))
note1_entry.grid(row=n_row, column=2, columnspan = 8)

n_row += 1
note2_label = tk.Label(root, text="Note 2 : ")
note2_label.grid(row=n_row, column=1)

note2_entry = tk.Entry(root,width=95,textvariable=tk.StringVar(value=" "))
note2_entry.grid(row=n_row, column=2, columnspan = 8)

n_row += 1
note3_label = tk.Label(root, text="Note 3 : ")
note3_label.grid(row=n_row, column=1)

note3_entry = tk.Entry(root,width=95,textvariable=tk.StringVar(value=" "))
note3_entry.grid(row=n_row, column=2, columnspan = 8)


n_row += 1
button_print = tk.Button(root, text="Print", command=print_all)
button_print.grid(row=n_row, column=1 )

button_reset = tk.Button(root, text="reset", fg='red', command=reset_all)
button_reset.grid(row=n_row, column=9 )


root.mainloop()
