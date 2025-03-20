import tkinter as tk

# Loo Tkinteri aken
root = tk.Tk()
root.title("Filmi andmete sisestamine")

# Loo sildid ja sisestusväljad
labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label] = entry

# Loo nupp andmete sisestamiseks
submit_button = tk.Button(root, text="Sisesta andmed")
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

# Näita Tkinteri akent
root.mainloop()
