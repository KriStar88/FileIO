from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {"file": f}
                response = requests.post("http://file.io", files=files)
                response.raise_for_status()
                link = response.json().get('link')
                if link:
                    entry.delete(0, END)
                    entry.insert(0, link)
                else:
                    raise ValueError("Не удалось получить ссылку")
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
