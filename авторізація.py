from tkinter import *
from tkinter import messagebox

def click():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Іван" and password == "b2812":
        messagebox.showinfo('', f'Вход подтвержден')
    elif username == "Іларіон" and password == "b2812":
        messagebox.showinfo('', f'Вход подтвержден')
    elif username == "Цух" and password == "b2812":
        messagebox.showinfo('', f'Вход подтвержден')
    elif username == "Грабовий" and password == "b2812":
        messagebox.showinfo('', f'Вход подтвержден')
    elif username == "Денис" and password == "b2812":
        messagebox.showinfo('', f'Вход подтвержден')
    elif username == "Віктор" and password == "b2812":
        messagebox.showinfo('', f'Вход подтвержден')
    elif username == "Андрій" and password == "b2812":
        messagebox.showinfo('', f'Вход подтвержден')
    elif username == "Євген" and password == "b2812":
        messagebox.showinfo('', f'Вход подтвержден')
    else:
        messagebox.showinfo('', f'Вход отменен')
root = Tk()
root.title('Авторизація')
root.geometry('450x230')
root.resizable(width=False, height=False)
root["bg"] = 'black'

main_label = Label(root, text='Авторизація', font='Arial 15 bold', bg='black', fg='white')
main_label.pack()

username_label = Label(root, text='Імя користувача', font='Arial 11 bold', bg='black', fg='white', padx= 10, pady=8 )
username_label.pack()

username_entry = Entry(root, bg='black', fg= 'lime', font="Arial 12 bold")
username_entry.pack()

password_label = Label(root, text='Пароль', font='Arial 11 bold', bg='black', fg='white', padx= 10, pady=8 )
password_label.pack()

password_entry = Entry(root, bg='black', fg= 'lime', font="Arial 12 bold")
password_entry.pack()

send_btn = Button(root, text='Війти', command=click)
send_btn.pack()

root.mainloop()