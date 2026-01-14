import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Main Application")
    root.geometry("800x600")

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    # Konfiguracja wierszy (opcjonalnie)
    root.grid_rowconfigure(0, weight=1)

    tk.Label(root, text="Left column").grid(row=0, column=0, padx=10, pady=10, sticky="n")
    tk.Label(root, text="III").grid(row=0, column=2, padx=10, pady=10, sticky="se")
    context_menu_button = tk.Button(root, text="Click Me").grid(row=0, column=2, padx=10, pady=10, sticky="ne")
    tk.Button.config(root, cursor="hand2")

    root.mainloop()

if __name__ == "__main__":
    main()
