import tkinter as tk
from tkinter import messagebox
import sys

class UpdateWindow:
    def __init__(self, check_update_callback, download_callback, continue_callback):
        self.check_update_callback = check_update_callback
        self.download_callback = download_callback
        self.continue_callback = continue_callback

        self.root = tk.Tk()
        self.root.title("Update Check")
        self.root.geometry("420x220")
        self.root.resizable(False, False)

        self.label = tk.Label(
            self.root,
            text="Checking for updates...",
            font=("Segoe UI", 12),
            justify="center"
        )
        self.label.pack(pady=40)

        self.button_frame = tk.Frame(self.root)

        self.yes_button = tk.Button(
            self.button_frame,
            text="Yes",
            width=12,
            command=self.download_update
        )

        self.no_button = tk.Button(
            self.button_frame,
            text="No",
            width=12,
            command=self.skip_update
        )

        # macOS: wszystko po starcie pętli
        self.root.after(0, self._post_init)

    # -------------------------
    # macOS handling
    # -------------------------

    def _post_init(self):
        self.center_window()
        self.bring_to_front()
        self.check_update()

    def center_window(self):
        self.root.update_idletasks()

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def bring_to_front(self):
        try:
            # macOS: aktywacja aplikacji
            self.root.tk.call("::tk::mac::ReopenApplication")
        except tk.TclError:
            pass

        self.root.lift()
        self.root.focus_force()

        # topmost tylko chwilowo
        self.root.attributes("-topmost", True)
        self.root.after(300, lambda: self.root.attributes("-topmost", False))

    # -------------------------
    # Update logic
    # -------------------------

    def check_update(self):
        update_available = self.check_update_callback()

        if update_available:
            self.label.config(
                text="A new update is available.\nDo you want to download it?"
            )
            self.button_frame.pack(pady=20)
            self.yes_button.pack(side=tk.LEFT, padx=10)
            self.no_button.pack(side=tk.RIGHT, padx=10)
        else:
            self.root.destroy()
            self.continue_callback()

    def download_update(self):
        self.download_callback()
        messagebox.showinfo("Update", "Update downloaded successfully.")
        self.root.destroy()
        self.continue_callback()

    def skip_update(self):
        self.root.destroy()
        self.continue_callback()

    def run(self):
        self.root.mainloop()
