import tkinter as tk
from tkinter import W, E, N, S, messagebox
from PIL import Image, ImageTk
def tkwindow():
    # global Label1
    # global Label2
    global Entry1
    # global Entry2
    # global Entry3
    # global Button1
    # global Button2
    # global Button3
    window = tk.Tk()
    window.geometry('800x800')
    window.resizable(False, False)
    window.title('Numerology')
    original_image = Image.open(r"C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Grafika\background.jpg")
    resized_image = original_image.resize((800, 800))  # Resize to window size
    bgimage = ImageTk.PhotoImage(resized_image)
    labelBG= tk.Label(window,image=bgimage)
    labelBG.place(x=0,y=0)
    Label1 = tk.Label(window, bg='lightgreen', font=('Arial',20,'bold'), text='Enter you Name', width = 20)
    Label1.place(x=0, y=0)
    Entry1 = tk.Entry(window, bg="lightblue", font=('Arial',20,'bold'), width = 23)
    Entry1.place(x=0, y=30)
    Button1 = tk.Button(window, text='Start', font=('Arial', 20, 'bold'), command=Start)
    Button1.place(x=700, y=0)
    # Label2 = tk.Label(window, font=('Arial', 20, 'bold'), bg='red', width = 10, height=5, text="Here you'll see an answer")
    # Label2.place(x=80, y=150)
    Button2 = tk.Button(window, text='Save result', font=('Arial', 20, 'bold'))
    Button2.place(x=615, y=55)
    Button3 = tk.Button(window, text='Show previous results', font=('Arial', 13, 'bold'))
    Button3.place(x=500, y=0)
    # LabelHuge = tk.Label(window, bg='white', font=('Arial', 20, 'bold'), text="Here you'll see clarification", width=20, height=10)
    # LabelHuge.place(x=90, y=300)
    window.mainloop()
def find_alphabet(Name):
    ENG_Count = 0
    RUS_Count = 0
    Error = 0
    ENG = ['z','x','c','v','b','n','m','a','s',
           'd','f','g','h','j','k','l','q','w',
           'e','r','t','y','u','i','o','p']
    RUS = ['я','ч','с','м','и','т','ь','б','ю',
           'ф','ы','в','а','п','р','о','л','д',
           'ж','э','й','ц','у','к','е','н','г',
           'ш','щ','з','х','ъ']
    for x in range(len(Name)):
        if Name[x] in ENG:
            ENG_Count = ENG_Count + 1
        elif Name[x] in RUS:
            RUS_Count = RUS_Count + 1
        else:
            Error = Error + 1
    return(ENG_Count, RUS_Count, Error)
def loo_vene_tabel(letter):
    vene = {'А':1, 'И':1, 'Й':1, 'С':1, 'Ы':1,
            'Б':2, 'Т':2, 'Ь':2, 'В':3, 'К':3, 
            'У':3, 'Э':3, 'Г':4, 'Л':4, 'Ф':4,
            'Д':5, 'М':5, 'Х':5, 'Я':5, 'Е':6,
            'Ё':6, 'Н':6, 'Ц':6, 'О':7, 'Ч':7,
            'Ж':8, 'П':8, 'Ш':8, 'З':9, 'Р':9,
            'Щ':9, 'Ъ':0}
    return vene.get(letter)
def loo_latina_tabel(letter):
    latina = {'A':1, 'J':1, 'S':1, 'B':2, 'K':2,
              'T':2, 'C':3, 'L':3, 'U':3, 'D':4,
              'M':4, 'V':4, 'E':5, 'N':5, 'W':5,
              'F':6, 'O':6, 'X':6, 'G':7, 'P':7,
              'Y':7, 'H':8, 'Q':8, 'Z':8, 'I':9,
              'R':9}
    return latina.get(letter)
def Start():
    Name = Entry1.get()
    print(Name)
    Name = Name.lower()
    print(Name)
    ENG_Count, RUS_Count, Error = find_alphabet(Name)
    Name = Name.upper()
    print(ENG_Count, RUS_Count, Error)
    letter_sum = 0
    if ENG_Count == 0 and Error == 0:
        for letter in range(len(Name)):
            letter_sum = letter_sum + loo_vene_tabel(Name[letter])
            if letter_sum > 9:
                calculate(letter_sum)
                print(letter_sum)
        reply_message_box(letter_sum)
    elif RUS_Count == 0 and Error == 0:
        for letter in range(len(Name)):
            letter_sum = letter_sum + loo_latina_tabel(Name[letter])
            if letter_sum > 9:
                calculate(letter_sum)
        reply_message_box(letter_sum)
    elif RUS_Count > 0 and ENG_Count > 0 and Error == 0:
        letters = ""
        for letter in range(len(Name)):
            if loo_latina_tabel(Name[letter]) is not None:
                letters = letters + f'{loo_latina_tabel(Name[letter])}:{Name[letter]},'
            elif loo_vene_tabel(Name[letter]) is not None:
                letters = letters + f'{loo_vene_tabel(Name[letter])}:{Name[letter]},'
        reply_message_box(letters)
def reply_message_box(number):
    messagebox.showinfo('Answer', number)
def calculate(letter_sum):
    letter_sum_str = str(letter_sum)
    letter_sum_temp = 0
    while letter_sum > 10:
        for xy in range(len(letter_sum_str)):
            letter_sum = letter_sum + int(letter_sum_str[xy])
    return letter_sum
def salvesta_tulemus(nimi, number):
    with open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\Grafika\Numberology_results.txt', "w", encoding="utf-8") as f:
        TempVariable = nimi, number
        f.write(TempVariable)
tkwindow()