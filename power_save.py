# import powerplan

# print(powerplan.get_current_scheme_name())
# print(powerplan.get_current_scheme_guid())
# powerplan.change_current_scheme_to_powersaver()

# print(powerplan.get_current_scheme_name())
# print(powerplan.get_current_scheme_guid())

import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'Hello World!', fg='blue', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Click Me', command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()

# import admin
# if not admin.isUserAdmin():
#         admin.runAsAdmin()



