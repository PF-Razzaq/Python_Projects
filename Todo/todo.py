
from tkinter import *
from tkinter import messagebox

# 1
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('Todo List')
ws.config(bg='#223344')
ws.resizable(width=False,height=False)

# 4

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

# 5
def deleteTask():
    lb.delete(ANCHOR)


# 3
frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#6a6a6a',
    activestyle='none'
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Eat apple',
    'Drink Water',
    'Go Gym'
]

for item in task_list:
    lb.insert(END,item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry= Entry(
    ws,font=('item',24) 
)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 15 '),
    background='#c5f777',
    padx=20,
    pady=10,
    command=newTask 
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)



# 2
ws.mainloop()
