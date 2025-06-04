import tkinter as tk
from tkinter import messagebox
import random
import string
import os

# Цвета для оформления
BG_COLOR = "#1a1a1a"
FG_COLOR = "#e0e0e0"
BTN_COLOR = "#333"
BTN_ACTIVE = "#555"
ENTRY_BG = "#222"
ENTRY_FG = "#fff"

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

class PasswordPrompt(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LORD - Вход")
        self.configure(bg=BG_COLOR)
        self.geometry("320x120")
        self.resizable(False, False)

        tk.Label(self, text="Введите пароль для доступа:", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 10)).pack(pady=10)
        self.password_entry = tk.Entry(self, show="*", bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 12))
        self.password_entry.pack(pady=5)
        self.password_entry.focus()

        tk.Button(self, text="Ввод", bg=BTN_COLOR, fg=FG_COLOR, activebackground=BTN_ACTIVE, command=self.check_password).pack(pady=5)

    def check_password(self):
        if self.password_entry.get() == "LORD111":
            self.destroy()
            app = MainApp()
            app.mainloop()
        else:
            messagebox.showerror("Ошибка", "Неверный пароль")
            self.password_entry.delete(0, tk.END)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LORD")
        self.configure(bg=BG_COLOR)
        self.geometry("540x350")
        self.resizable(False, False)

        # "Логотип"/шапка
        tk.Label(self, text="LORD", bg=BG_COLOR, fg="#ff00ff", font=("Arial Black", 24)).pack(pady=10)

        # Request
        frame_req = tk.Frame(self, bg=BG_COLOR)
        frame_req.pack(pady=2)
        tk.Label(frame_req, text="Request:", bg=BG_COLOR, fg=FG_COLOR, width=10, anchor='e').pack(side=tk.LEFT)
        self.req_entry = tk.Entry(frame_req, bg=ENTRY_BG, fg=ENTRY_FG, width=40)
        self.req_entry.pack(side=tk.LEFT, padx=5)
        tk.Label(frame_req, text="(необязательно)", bg=BG_COLOR, fg="#888").pack(side=tk.LEFT)

        # Activation
        frame_act = tk.Frame(self, bg=BG_COLOR)
        frame_act.pack(pady=2)
        tk.Label(frame_act, text="Activation:", bg=BG_COLOR, fg=FG_COLOR, width=10, anchor='e').pack(side=tk.LEFT)
        self.act_entry = tk.Entry(frame_act, bg=ENTRY_BG, fg=ENTRY_FG, width=40)
        self.act_entry.pack(side=tk.LEFT, padx=5)
        tk.Label(frame_act, text="(необязательно)", bg=BG_COLOR, fg="#888").pack(side=tk.LEFT)

        # Путь сохранения
        frame_path = tk.Frame(self, bg=BG_COLOR)
        frame_path.pack(pady=2)
        tk.Label(frame_path, text="Путь:", bg=BG_COLOR, fg=FG_COLOR, width=10, anchor='e').pack(side=tk.LEFT)
        self.path_entry = tk.Entry(frame_path, bg=ENTRY_BG, fg=ENTRY_FG, width=40)
        self.path_entry.pack(side=tk.LEFT, padx=5)
        self.path_entry.insert(0, r"D:\Desktop")  # Значение по умолчанию

        # Имя файла
        frame_file = tk.Frame(self, bg=BG_COLOR)
        frame_file.pack(pady=2)
        tk.Label(frame_file, text="Имя файла:", bg=BG_COLOR, fg=FG_COLOR, width=10, anchor='e').pack(side=tk.LEFT)
        self.file_entry = tk.Entry(frame_file, bg=ENTRY_BG, fg=ENTRY_FG, width=40)
        self.file_entry.pack(side=tk.LEFT, padx=5)
        self.file_entry.insert(0, "keys")

        # Длина и количество
        frame_len = tk.Frame(self, bg=BG_COLOR)
        frame_len.pack(pady=2)
        tk.Label(frame_len, text="Длина:", bg=BG_COLOR, fg=FG_COLOR, width=10, anchor='e').pack(side=tk.LEFT)
        self.len_entry = tk.Entry(frame_len, bg=ENTRY_BG, fg=ENTRY_FG, width=8)
        self.len_entry.pack(side=tk.LEFT, padx=5)
        self.len_entry.insert(0, "16")
        tk.Label(frame_len, text="Кол-во:", bg=BG_COLOR, fg=FG_COLOR, width=10, anchor='e').pack(side=tk.LEFT)
        self.count_entry = tk.Entry(frame_len, bg=ENTRY_BG, fg=ENTRY_FG, width=8)
        self.count_entry.pack(side=tk.LEFT, padx=5)
        self.count_entry.insert(0, "5")

        # Кнопки
        frame_btn = tk.Frame(self, bg=BG_COLOR)
        frame_btn.pack(pady=15)
        tk.Button(frame_btn, text="Patch", width=10, bg=BTN_COLOR, fg=FG_COLOR, activebackground=BTN_ACTIVE, command=self.patch_stub, state="disabled").pack(side=tk.LEFT, padx=8)
        tk.Button(frame_btn, text="Generate", width=10, bg=BTN_COLOR, fg=FG_COLOR, activebackground=BTN_ACTIVE, command=self.generate_keys).pack(side=tk.LEFT, padx=8)
        tk.Button(frame_btn, text="Quit", width=10, bg=BTN_COLOR, fg=FG_COLOR, activebackground=BTN_ACTIVE, command=self.quit).pack(side=tk.LEFT, padx=8)

        # Строка состояния
        self.status = tk.Label(self, text="", bg=BG_COLOR, fg="#ff00ff", font=("Arial", 10))
        self.status.pack(pady=5)

    def patch_stub(self):
        messagebox.showinfo("Stub", "Функция Patch не реализована.")

    def generate_keys(self):
        path = self.path_entry.get().strip()
        filename = self.file_entry.get().strip()
        try:
            length = int(self.len_entry.get())
            count = int(self.count_entry.get())
            if length <= 0 or count <= 0:
                raise ValueError
        except ValueError:
            self.status.config(text="Ошибка: длина и количество — положительные числа")
            return
        if not path or not filename:
            self.status.config(text="Ошибка: укажите путь и имя файла")
            return
        if not os.path.isdir(path):
            self.status.config(text="Ошибка: путь не существует")
            return

        filepath = os.path.join(path, f"{filename}.txt")

        try:
            with open(filepath, "a", encoding="utf-8") as f:
                for _ in range(count):
                    pwd = generate_password(length)
                    f.write(pwd + "\n")
            self.status.config(text=f"Сохранено в {filepath}")
        except Exception as e:
            self.status.config(text=f"Ошибка сохранения: {e}")

if __name__ == "__main__":
    PasswordPrompt().mainloop()
