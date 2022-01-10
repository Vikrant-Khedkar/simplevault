import tkinter as tk
import ekg as e




window = tk.Tk()
window.geometry("300x300")
entry= tk.Entry(show="*",width=100)
B2 = tk.Button(text ="encrypt",command = e.compress,width=20)
B3 = tk.Button(text ="decrypt",command = e.decompress)
B4 = tk.Button(text ="delete raw",command = e.prune)
B5 = tk.Button(text ="exit",command = exit)

def password():
    passwd = entry.get()
    
    if e.password(passwd) == True:
        B2.pack()
        B3.pack()
        B4.pack()
        B5.pack()
        B1.destroy
        entry.destroy
        





B1 = tk.Button(text ="submit",command = password,width=20)
entry.pack()
B1.pack()

tk.mainloop()



    