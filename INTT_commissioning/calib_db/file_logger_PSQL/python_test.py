import tkinter as tk

def change_color(*args,var_in,CB):
    if var_in.get():
        CB.configure(bg='green')
    else:
        CB.configure(bg='white')

root = tk.Tk()
root.geometry("200x150")

var_sharp_2  = [tk.IntVar(root) for i in range(4)]
list = []

for i in range(4):
    #var = tk.BooleanVar()
    var_sharp_2[i].set(value = False)
    check_button = tk.Checkbutton(root, text="Change color", variable=var_sharp_2[i],onvalue=True, offvalue=False)
    check_button.pack(pady=10)
    list.append(check_button)
    list[i].configure(command = lambda value, i=i: change_color(var_in=value,CB = list[i]))
    
root.mainloop()


#import tkinter as tk

#def change_color():
#    if var.get():
#        check_button.configure(bg='green')
#    else:
#        check_button.configure(bg='white')

#root = tk.Tk()
#root.geometry("200x100")

#var = tk.BooleanVar()
#check_button = tk.Checkbutton(root, text="Change color", variable=var, command=change_color)
#check_button.pack(pady=10)

#root.mainloop()
