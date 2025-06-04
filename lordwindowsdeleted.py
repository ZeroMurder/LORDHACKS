import os
import sys
import time
import subprocess
import threading
import ctypes
import tkinter as tk

try:
    import pyautogui
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
    import pyautogui

pyautogui.FAILSAFE = False

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
fake_file = os.path.join(desktop_path, "crack1231313.txt")

exit_flag = False

def block_cursor():
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth // 2, screenHeight // 2)

def open_cmd_briefly():
    proc = subprocess.Popen("cmd.exe")
    time.sleep(1)
    proc.terminate()

def create_and_delete_fake_file():
    try:
        with open(fake_file, "w") as f:
            f.write("This is a crack file. Nothing harmful.")
        time.sleep(0.5)
        os.remove(fake_file)
    except Exception:
        pass

class FakeVirusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows Deleted")
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.config(cursor="none", bg="black")
        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<FocusOut>", self.on_focus_out)

        self.label = tk.Label(root, text="Windows Deleted\nClosing in 10 seconds...", fg="red",
                              bg="black", font=("Consolas", 48, "bold"), justify='center')
        self.label.pack(expand=True)

        self.counter = 10

        self.hide_taskbar()  # Скрываем панель задач и кнопку Пуск

        self.countdown()
        self.block_mouse_loop()

    def hide_taskbar(self):
        HWND = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)
        StartBtn = ctypes.windll.user32.FindWindowW("Button", None)
        ctypes.windll.user32.ShowWindow(HWND, 0)       # Скрыть панель задач
        ctypes.windll.user32.ShowWindow(StartBtn, 0)   # Скрыть кнопку Пуск

    def show_taskbar(self):
        HWND = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)
        StartBtn = ctypes.windll.user32.FindWindowW("Button", None)
        ctypes.windll.user32.ShowWindow(HWND, 5)       # Показать панель задач
        ctypes.windll.user32.ShowWindow(StartBtn, 5)   # Показать кнопку Пуск

    def disable_event(self):
        # Запрет закрытия окна
        pass

    def on_focus_out(self, event):
        # Возвращаем окно на передний план
        self.root.attributes('-topmost', True)
        self.root.focus_force()

    def on_key_press(self, event):
        global exit_flag
        if event.keysym == 'F7':
            exit_flag = True
            self.exit_all()

    def countdown(self):
        global exit_flag
        if exit_flag:
            return
        if self.counter > 0:
            self.label.config(text=f"Windows Deleted\nClosing in {self.counter} seconds...")
            self.counter -= 1
            self.root.after(1000, self.countdown)
        else:
            # Закрываем основное окно перед запуском следующих этапов
            self.root.destroy()
            threading.Thread(target=self.next_steps).start()

    def block_mouse_loop(self):
        global exit_flag
        if exit_flag:
            return
        block_cursor()
        self.root.after(50, self.block_mouse_loop)

    def next_steps(self):
        open_cmd_briefly()
        create_and_delete_fake_file()
        self.show_message("Warning", "Вирус проник в базу и уничтожает данные!")
        self.show_message("Прощайте", "Спасибо за внимание!")
        self.exit_all()

    def show_message(self, title, message):
        if exit_flag:
            return
        msg_win = tk.Toplevel()
        msg_win.title(title)
        msg_win.attributes('-topmost', True)
        msg_win.geometry("600x200+{}+{}".format(
            (msg_win.winfo_screenwidth() // 2) - 300,
            (msg_win.winfo_screenheight() // 2) - 100))
        msg_win.config(bg="black")
        msg_win.protocol("WM_DELETE_WINDOW", lambda: None)

        label = tk.Label(msg_win, text=message, fg="red", bg="black", font=("Consolas", 24, "bold"))
        label.pack(expand=True, fill='both')

        def on_key(event):
            global exit_flag
            if event.keysym == 'F7':
                exit_flag = True
                msg_win.destroy()
                self.exit_all()

        msg_win.bind("<Key>", on_key)
        msg_win.focus_set()
        msg_win.grab_set()
        msg_win.wait_window()

    def exit_all(self):
        global exit_flag
        exit_flag = True
        self.show_taskbar()  # Восстанавливаем панель задач и кнопку Пуск
        try:
            self.root.destroy()
        except:
            pass
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeVirusApp(root)
    root.mainloop()



