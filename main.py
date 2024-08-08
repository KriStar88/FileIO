from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from  tkinter import messagebox as mb
import requests
import pyperclip


def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {"file": open(filepath, 'rb')}
                response = requests.post("http://file.io", files=files)
                response.raise_for_status()
                link = response.json()['link']
                entry.delete(0, END)
                entry.insert(0, link)
                pyperclip.copy(link)
                mb.showinfo("Ссылка скопирована", f"Ссылка {link} успешно скопирована в буфер обмена")
    except Exception as e:
        mb.showerror("Ошибка", f"произошла ошибка: {e}")

window = Tk()
window.title("Сохранение файла в облаке")
window.geometry("400x300")
button = ttk.Button(text="Загрузить файл", command=upload)
button.pack()
entry = ttk.Entry()
entry.pack()
window.mainloop()