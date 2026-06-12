# Program Name: Assignment1.py
# Course: IT3883/Section 52337
# Student Name: Tim Ombongi
# Assignment Number: Assignment 1
# Due Date: 06/11/2026
# Purpose: This Program allows the user to input buffer and choose to display them, clear them, or store them. When the user is done they can exit the program.
# Pycharm
buffer = ""
choice = ""

while choice != "4":

    print("Menu")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            text = input("Enter text: ")
            buffer += text
            print("Data appended.")

        case "2":
            buffer = ""
            print("Buffer cleared.")

        case "3":
            print("Current Buffer:")
            print(buffer)

        case "4":
            print("exiting program..")

        case _:
            print("Invalid input.")