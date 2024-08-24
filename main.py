from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text= "00:00")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 

    reps += 1

    if(reps % 2 == 0):
        marks=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_mark.config(text=marks)

    if(reps % 2 != 0):
        count_down(WORK_MIN * 60)
        label.config(text="Work", fg=GREEN)
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
    elif(reps % 8 == 0):
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Long Break", fg=RED)
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Short Break", fg=PINK)
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    global timer

    if min == 0:
        min = "00"
    elif min < 10:
        min = "0" + str(min)
    
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = "0" + str(sec)

    canvas.itemconfig(timer_text, text= f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset)
reset_btn.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW,  highlightthickness=0)
check_mark.grid(row=3, column=1)

window.mainloop()