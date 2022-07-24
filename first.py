from tkinter import *

root = Tk()
root.title('py calculator')

entry = Entry(root,
              width=50,
              borderwidth=5
              )
entry.grid(row=0, column=0,
    columnspan=3,
    padx=10,
    pady=10)
def number_click(num):
    current = entry.get()
    entry.delete(0,END)
    print(num)
    entry.insert(0,current+str(num))

button = [Button(root, text=str(i),
                 font=('Arial', 20, 'bold'),
                 padx=40, pady=20) for i in range(10)]

t = [i for i in range(10)]
print(t)
for r in range(10):
    print(t[r])
    button[r].config(command=lambda:number_click(t[r]))

x = 1

for i in range(3, 0, -1):
    for j in range(3):
        button[x].grid(row=i, column=j)
        x += 1
button[0].grid(row=4, column=0)
operators = ['+', '-', '*', '/', '=']
operator_button = [Button(root, text=i,
                          font=('Arial', 20, 'bold'),
                          padx=40, pady=20)
                   for i in operators]
operator_button[0].grid(row=4, column=1)
operator_button[1].grid(row=4, column=2)
x = 2
for i in range(5, 6):
    for j in range(3):
        operator_button[x].grid(row=i, column=j)
        x += 1

ans_button = Button(root, text='=', padx=40, pady=20)
root.mainloop()
