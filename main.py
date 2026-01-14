import tkinter as tk
from assets.version_checker import get_local_version


def main():
    root = tk.Tk()
    base_title = "Noxxer Base v" + get_local_version()
    root.title(base_title)
    root.geometry("800x600")
    icon = tk.PhotoImage(file="assets/icon.png")  # musi być PNG lub GIF
    root.iconphoto(True, icon)


    # ---------- AKTYWNY FRAME ----------
    active_frame = tk.StringVar(value="main")

    # ---------- MENU KONTEKSTOWE ----------
    def show_main():
        main_frame.tkraise()
        root.title(f"{base_title} - Main Frame")
    def show_overlay():
        overlay_frame.tkraise()
        root.title(f"{base_title} - Overlay Frame")

    context_menu = tk.Menu(root, tearoff=0)

    def update_menu():
        context_menu.delete(0, tk.END)
        context_menu.add_radiobutton(
            label="Main Frame",
            variable=active_frame,
            value="main",
            command=show_main
        )
        context_menu.add_radiobutton(
            label="Overlay Frame",
            variable=active_frame,
            value="overlay",
            command=show_overlay
        )
        context_menu.add_separator()
        context_menu.add_command(label="Exit", command=root.quit)

    def show_context_menu(event):
        update_menu()
        context_menu.tk_popup(event.x_root, event.y_root)

    # ---------- KONFIGURACJA KOLUMN ----------
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(0, weight=1)

    # ---------- MAIN FRAME ----------
    main_frame = tk.Frame(root)
    main_frame.place(relwidth=1, relheight=1)  # <- musimy go umieścić w oknie
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_columnconfigure(2, weight=1)
    main_frame.grid_rowconfigure(0, weight=1)

    main_label = tk.Label(main_frame, text="Main Frame", font=("Segoe UI", 24), fg="white")
    main_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    btn = tk.Button(main_frame, text="|||")
    btn.grid(row=0, column=2, padx=10, pady=10, sticky="ne")
    btn.bind("<Button-1>", show_context_menu)

    # ---------- OVERLAY FRAME ----------
    overlay_frame = tk.Frame(root)
    overlay_frame.place(relwidth=1, relheight=1)
    overlay_frame.grid_columnconfigure(0, weight=1)
    overlay_frame.grid_columnconfigure(1, weight=1)
    overlay_frame.grid_rowconfigure(0, weight=1)
    overlay_frame.grid_rowconfigure(1, weight=2)

    main_overlay_label = tk.Label(
        overlay_frame, text="Overlay content", font=("Segoe UI", 24), fg="white"
    )
    main_overlay_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")



    btn = tk.Button(overlay_frame, text="|||")
    btn.grid(row=0, column=2, padx=10, pady=10, sticky="ne")
    btn.bind("<Button-1>", show_context_menu)

    # ---------- START OKNA ----------
    main_frame.tkraise()  # <-- pokazujemy główny ekran na starcie

    root.mainloop()


if __name__ == "__main__":
    main()
