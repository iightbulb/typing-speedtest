# GUI typing speedtest application using tkinter


import tkinter as tk
from tkinter import *
import random


BLACK = "#000000"
CREAM = "#FFE6E6"
FONT_NAME = "Courier"

window = tk.Tk()
window.title("Test your typing speed")
window.config(padx=60, pady=40, bg=CREAM)
fg = BLACK

word_list = []
with open('words.txt', 'r') as f:
    for line in f.readlines():
        word_list.append(line.replace('\n', ''))

val = tk.StringVar()
user_entry = tk.Entry(window, textvariable=val)
user_entry.grid(row=2, column=1, pady=50)
user_entry.focus()
words = tk.Label(window, text='Choose the duration of the test below. When ready, click Start.', bg=CREAM)
words.config(font=('Arial', 20))
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


def correct_word():
    if user_entry.get() == words['text']:
        print('delete user entry')
        user_entry.delete(0, END)
        words.config(text=random.choice(word_list))
        return True
    else:
        return False


def start():
    total_time = int(timer_text['text'])
    words.config(text=random.choice(word_list))
    i = 0
    word_count = 0
    while i < total_time:
        if correct_word():
            word_count += 1
            word_count_text = tk.Label(window, text=f"Word count: {word_count}")
            word_count_text.grid(row=4, column=2)
        tksleep(1)
        i += 1
        timer_text['text'] = total_time - i
        print(f"b'{user_entry.get()}'")
        print(words['text'])
    print(word_count)
    print(total_time)
    words.config(text=f"Time's up!You type at {word_count/total_time*60} words per minute.")


start_button = tk.Button(text="Start", highlightthickness=0, command=start)
start_button.grid(row=3, column=1, pady=10)
thirty_seconds = tk.Button(text="30 seconds", highlightthickness=0, command=thirty)
thirty_seconds.grid(row=5, column=0)
sixty_seconds = tk.Button(text="60 seconds", highlightthickness=0, command=sixty)
sixty_seconds.grid(row=5, column=1)
two_minutes = tk.Button(text="120 seconds", highlightthickness=0, command=one_twenty)
two_minutes.grid(row=5, column=2)


window.mainloop()
