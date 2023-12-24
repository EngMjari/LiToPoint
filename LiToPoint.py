import pyperclip
import re
from tkinter import messagebox


def show_warning_message():
    # Error Message for Wrong Copy
    messagebox.showerror("پیام  خطا", "مقدار درست کپی نشده است")


file = pyperclip.paste()
regtex = r"X=(\d*.\d*)\D+Y=(\d*.\d*)"

point = re.findall(regtex, file)
if point:
    # Creat point file:
    with open("outpout.txt", 'w') as newFile:
        for i, k in enumerate(point):
            line = f"{i+1},{k[0]},{k[1]}"
            newFile.write(line)
            if i != len(point)-1:
                newFile.write('\n')

else:
    show_warning_message()
