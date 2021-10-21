# Binary-Hexadecimal-Octal-Decimal (=BHOD) Computer

import tkinter
from decimal import Decimal

# Methods
def binary():
    input = e.get()
    number = int(input)
    solution = bin(number)
    lb["text"] = solution

def octal():
    input = e.get()
    number = int(input)
    solution = oct(number)
    lb["text"] = solution


def hexadecimal():
    input = e.get()
    number = int(input)
    solution = hex(number)
    lb["text"] = solution

def decimal():
    input = e.get()
    number = Decimal(input)
    solution = str(number)
    lb["text"] = solution

# Main
main = tkinter.Tk()
main.title("BHOD")
main["bg"] = "#FFFFFF"

# Input
e = tkinter.Entry(main)
e["borderwidth"] = 5
e.pack()

# Output
lb = tkinter.Label(main, text = "")
lb["font"] = "Times 13 bold"
lb["height"] = 2
lb["width"] = 20
lb["borderwidth"] = 5
lb["bg"] = "#FFFFFF"
lb["fg"] = "#000000"
lb.pack()

# Binary button
button_binary = tkinter.Button(main, text = "Binary", command = binary)
button_binary["font"] = "Times 13 bold"
button_binary["height"] = 2
button_binary["width"] = 20
button_binary["borderwidth"] = 5
button_binary["bg"] = "#6a9cfa"
button_binary["fg"] = "#000000"
button_binary.pack()

# Hexadecimal button
button_hexadecimal = tkinter.Button(main, text = "Hexadecimal", command = hexadecimal)
button_hexadecimal["font"] = "Times 13 bold"
button_hexadecimal["height"] = 2
button_hexadecimal["width"] = 20
button_hexadecimal["borderwidth"] = 5
button_hexadecimal["bg"] = "#6afa72"
button_hexadecimal["fg"] = "#000000"
button_hexadecimal.pack()

# Octal button
button_octal = tkinter.Button(main, text = "Octal", command = octal)
button_octal["font"] = "Times 13 bold"
button_octal["height"] = 2
button_octal["width"] = 20
button_octal["borderwidth"] = 5
button_octal["bg"] = "#FFC300"
button_octal["fg"] = "#000000"
button_octal.pack()

# Decimal button
button_decimal = tkinter.Button(main, text = "Decimal", command = decimal)
button_decimal["font"] = "Times 13 bold"
button_decimal["height"] = 2
button_decimal["width"] = 20
button_decimal["borderwidth"] = 5
button_decimal["bg"] = "#fa6f6a"
button_decimal["fg"] = "#000000"
button_decimal.pack()

main.mainloop()
