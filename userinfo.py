import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

screen_height = screen_height - (screen_height * 0.1)
screen_width = screen_width - (screen_width * 0.1)

print(f"Résolution: {screen_width} x {screen_height}")

root.destroy()