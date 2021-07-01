import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# Create window for the timer program.
window = tk.Tk()
window.title(text="Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Create canvas with background image and timer text.
canvas = tk.Canvas(width=200, height=224)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(x=103, y=112, image=tomato_image)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

window.mainloop()