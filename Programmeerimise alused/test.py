import tkinter as tk

def double_click(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = listbox.get(selected_index[0])
        label.config(text=f'Selected: {selected_index}')
root = tk.Tk()
root.title("Listbox with double klick")
listbox = tk.Listbox(root, height=5)
listbox.pack()
items = ['Apple', 'Banana', 'Orange', 'Pear']
for item in items:
    listbox.insert(tk.END, item)
listbox.bind("<Double-Button-1>", double_click)
label = tk.Label(root, text='Selected: ')
label.pack()
root.mainloop()