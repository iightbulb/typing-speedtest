import requests
import tkinter as tk
import random


BLACK = "#000000"
CREAM = "#FFE6E6"
FONT_NAME = "Courier"

window = tk.Tk()
window.title("Test your typing speed")
window.config(padx=60, pady=40, bg=CREAM)
fg = BLACK

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

window = window
user_entry = tk.Entry(window)
user_entry.grid(row=2, column=1, pady=50)
user_entry.focus()
words = tk.Label(window, text='Ready? Click start')
words.grid(row=0, column=1)
timer_text = tk.Label(window, text=30)
timer_text.grid(row=4, column=1, pady=10)


def thirty():
    timer_text['text'] = 30


def sixty():
    timer_text['text'] = 60


def one_twenty():
    timer_text['text'] = 120


def tksleep(t):
    ms = int(t*1000)
    var = tk.IntVar(window)
    window.after(ms, lambda: var.set(1))
    window.wait_variable(var)


def new_word():
    user_entry.delete(0)
    words.config(text=random.choice(WORDS))


def start():
    total_time = int(timer_text['text'])
    print(total_time)
    words.config(text=random.choice(WORDS))
    i = 0
    word_count = 0
    while i < total_time:
        tksleep(1)
        i += 1
        timer_text['text'] = total_time - i
        print(f"b'{user_entry.get()}'")
        print(words['text'])
        if f"b'{user_entry.get()}'" == words['text']:
            new_word()
            word_count += 1
    words.config(text=f"Time's up!You type at {int(word_count/total_time)} words per minute.")


start_button = tk.Button(text="Start", highlightthickness=0, command=start)
start_button.grid(row=3, column=1, pady=10)
thirty_seconds = tk.Button(text="30 seconds", highlightthickness=0, command=thirty)
thirty_seconds.grid(row=5, column=0)
sixty_seconds = tk.Button(text="60 seconds", highlightthickness=0, command=sixty)
sixty_seconds.grid(row=5, column=1)
two_minutes = tk.Button(text="120 seconds", highlightthickness=0, command=one_twenty)
two_minutes.grid(row=5, column=2)


window.mainloop()
