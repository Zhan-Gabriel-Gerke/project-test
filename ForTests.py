import tkinter as tk
def show_frame(frame):
    frame.tkraise()  # Перемещает нужный фрейм на передний план

root = tk.Tk()
root.geometry("300x200")

container = tk.Frame(root)
container.pack(fill="both", expand=True)

frame1 = tk.Frame(container, bg="lightgreen")
frame2 = tk.Frame(container, bg="lightcoral")

for frame in (frame1, frame2):
    frame.place(relwidth=1, relheight=1)  # Заполняем весь контейнер

btn1 = tk.Button(frame1, text="Переключиться", command=lambda: show_frame(frame2))
btn1.pack(pady=50)

btn2 = tk.Button(frame2, text="Назад", command=lambda: show_frame(frame1))
btn2.pack(pady=50)

show_frame(frame1)  # Начальный экран

root.mainloop()
