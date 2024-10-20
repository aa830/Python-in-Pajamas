import keyword
import pyfiglet
import sys
import subprocess
import time

# Get user's name and welcome them, also display a nice title screen using pyfiglet lib
displayProgramTitle = pyfiglet.figlet_format("Python in Pajamas", font="doh", width=200)
print(displayProgramTitle)
name = input("Hello user! Welcome to Python in Pajamas, please enter your name: ")

def welcomeandselect():
    print(f"Hello {name}, welcome to the wonderful world of Python, but let's quickly check how much you know!")
    userKnowledge = input("Tell me, what do you know about machine language or binary?: ")

    # List of keywords related to machine language and binary
    kwlist = [
        'computer', 'computers', '1s and 0s', '0s and 1s', '0', '1', 'language', 
        'understand', 'binary', '01', 'bit', '0 or 1', 'byte', '8 bits', 'code', 
        'instructions for the CPU', 'cpu', 'Central Processing Unit', 'instruction', 
        'command for the CPU', 'memory', 'storage for data', 'number', 
        'a value made of bits', 'zero', 'off state', 'one', 'on state', 
        'on_off', 'binary logic state', 'logic', 'rules governing operations', 
        'data', 'information processed by the CPU', 'program', 'sequence of instructions', 
        'command', 'direct instruction for a task'
    ]
    
    # Convert user input to lowercase for case-insensitive comparison
    user_input_lower = userKnowledge.lower()
    
    # Iterate over each keyword in kwlist (detect if any keywords were in user's input)
    found_keyword = False
    for kw in kwlist:
        if kw.lower() in user_input_lower:
            found_keyword = True
            break
    
    # Course selection logic
    if found_keyword:
        print("Great! You've already learned about it. Let's learn a little more, shall we?")
        course_choice = input("Select which course you would like to begin (1-4), or press enter to begin at the start: ")
    else:
        print("It's okay if you don't know that much! Let's dive in!")
        course_choice = input("I would recommend you start from Course 1, but if you want, input a number from 1-4 to select another course (4 to exit): ")

    # Check if the user pressed Enter or selected a course between 1-4
    if course_choice == "":
        print("Starting Course 1 by default...")
        start_course(1)
    elif course_choice.isdigit() and 1 <= int(course_choice) <= 4:
        if int(course_choice) in [1, 2, 3]:
            print(f"Starting Course {course_choice}...")
            start_course(int(course_choice))
        else:
            exitTitle = pyfiglet.figlet_format("Goodbye!", font="doh", width=250)
            print(exitTitle) 
            time.sleep(2)
            sys.exit()
    else:
        print("Invalid input. Starting Course 1 by default...")
        start_course(1)

def start_course(course_number):
    if course_number > 0 and course_number != 4:
        print(f"Welcome to Course {course_number}!")

    if course_number == 1:
        print("Course 1: Introduction to Machine Language and Binary")
        print("Objective: Learn the basics of machine language and binary.")
    elif course_number == 2:
        print("Course 2: Understanding the Python Programming Language")
        print("Objective: Learn how Python translates to binary.")
    elif course_number == 3:
        print("Course 3: Binary Interaction with Memory")
        print("Objective: Learn how binary manages memory in computers.")

    # Replace the learning objectives with a loading message
    print("Please wait...")
    
    # Fake loading bar (aesthetic appeal)
    for i in range(101):
        time.sleep(0.05)
        sys.stdout.write("\r[" + "=" * (i // 2) + " " * (50 - i // 2) + f"] {i}%")
        sys.stdout.flush()

    print("\nLoading complete! Let's get started...\n")

    # Pass the name and course number to terminalgui.py as command-line arguments
    subprocess.run([sys.executable, "terminalgui.py", name, str(course_number)])

# Call the welcome and select function to start the script
welcomeandselect()
