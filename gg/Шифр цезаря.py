from tkinter import*

g = Tk()
g.title("Шифр")
g.geometry("600x500")
g.resizable(width=False, height=False)

frame = Frame(g, bg="yellow")
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text="Ведіть текст для шифрування", bg="gray", font=42)
title.pack()


key123 = Entry(frame, bg="white")
key123.pack()

keyy = Label(frame, text="Ключ для шифру", bg="gray", font=42)
keyy.pack()

def baton1():
    teext = key123.get()
    sam = [' ']
    for i in sam:
        teext = teext.replace(i, "")
    hft = ""
    
    for i in teext:
        if "a" <= i.lower() <= "z":
            hft += chr(((ord(i) - ord("a") + 2) % 26) + ord("a"))
        elif "а" <= i <= "я":
            hft += chr(((ord(i) - ord("а") + 2) % 33) + ord("а"))
        else:
            hft += i 
    
    sam_text = Tk()
    sam_text.geometry("600x500")
    sam_text2 = Label(sam_text, text= hft, font = 30)
    sam_text2.pack()
    sam_text.mainloop()
    

btn = Button(frame, text="ключ 2:", bg="gray", command=baton1)
btn.pack()

def baton2():
    teext = key123.get()
    sam = [' ']
    for i in sam:
        teext = teext.replace(i, "")
    hft = ""
    
    for i in teext:
        if "a" <= i <= "z":
            hft += chr(((ord(i) - ord("a") + 3) % 26) + ord("a"))
        elif "а" <= i <= "я":
            hft += chr(((ord(i) - ord("а") + 3) % 33) + ord("а"))
        else:
            hft += i 
    
    sam_text = Tk()
    sam_text.geometry("600x500")
    sam_text2 = Label(sam_text, text= hft, font = 30)
    sam_text2.pack()
    sam_text.mainloop()

btn1 = Button(frame, text="ключ 3:", bg="gray", command=baton2)
btn1.pack()

def baton3():
    teext = key123.get()
    sam = [' ']
    for i in sam:
        teext = teext.replace(i, "")
    hft = ""
    
    for i in teext:
        if "a" <= i <= "z":
            hft += chr(((ord(i) - ord("a") + 4) % 26) + ord("a"))
        elif "а" <= i <= "я":
            hft += chr(((ord(i) - ord("а") + 4) % 33) + ord("а"))
        else:
            hft += i 
    
    sam_text = Tk()
    sam_text.geometry("600x500")
    sam_text2 = Label(sam_text, text= hft, font = 30)
    sam_text2.pack()
    sam_text.mainloop()

btn2 = Button(frame, text="ключ 4:", bg="gray", command=baton3)
btn2.pack()



g.mainloop()