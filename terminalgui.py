import curses
import sys
from asciirenderer import ascii_art1, ascii_art2
import webbrowser
from PIL import Image


# ----------------------------------------------------------------DEFINING VARIABLES---------------------------------------------------------------- #


# Get the name and course number passed as command-line arguments
name = sys.argv[1] if len(sys.argv) > 1 else "User"
initial_course_number = int(sys.argv[2]) if len(sys.argv) > 2 else 1


# Table of contents menu for user to choose next course
def show_toc(stdscr):
    # Display the Table of Contents and allow the user to choose a course using arrow keys.
    stdscr.clear()
    toc_options = [
        "Introduction to Python in Pajamas",
        "Understanding Python Programming",
        "Setting up Python"
    ]
  
    toc_text = f"Welcome, {name}!\n\nUse the arrow keys to select a course and press Enter:\n"
    lines = toc_text.splitlines()
    max_y, max_x = stdscr.getmaxyx()

    # Current highlighted option index
    selected_option = 0

    while True:
        stdscr.clear()

        # Display the welcome message and TOC options
        for i, line in enumerate(lines):
            if len(line) > max_x - 2:
                line = line[:max_x - 2]
            if i < max_y - 1:
                stdscr.addstr(i + 1, 1, line)

        # Display TOC options with highlighting
        for idx, option in enumerate(toc_options):
            if idx == selected_option:
                stdscr.addstr(len(lines) + 2 + idx, 2, f"> {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(len(lines) + 2 + idx, 2, f"  {option}")

        # Instruction for quitting
        stdscr.addstr(max_y - 1, 1, "Press 'q' to quit.")
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Navigate the menu
        if key == curses.KEY_UP and selected_option > 0:
            selected_option -= 1
        elif key == curses.KEY_DOWN and selected_option < len(toc_options) - 1:
            selected_option += 1
        elif key == ord('\n'):  # Enter key
            return selected_option + 1  # Return the selected course number (1-based index)
        elif key == ord('q'):
            return 'quit'


# Main function to display course images
def main1(stdscr, course_number):
    stdscr.clear()
    a1 = ascii_art1()
    a2 = ascii_art2()
    a3 = Image.open('Screenshot 2024-10-28 at 4.10.11 PM.png')

    courses_content = {
        1: [
            (f"Page 1:\n\nHello {name}, welcome to your first lesson on Python in Pajamas!\n"
             "In this course, you will learn the basics of Python programming.\n"
             "You will be introduced to data types, control structures, and basic syntax.\n"
             "Let's start by learning about variables and how to use them in your code.\n"
             "\nVariables are used to store information to be referenced and manipulated in a program.\n"
             "For example:\n\n"
             "my_variable = 5\n\n"
             "This line creates a variable called my_variable and assigns it the value 5.\n"),
            ("Page 2:\n\nIn the next lesson, we will explore data types in Python.\n"
             "There are several built-in data types in Python, including integers, floats, strings, and booleans.\n"
             "You will learn how to define and use these data types in your programs.\n"
             "Let's get started by looking at integers!\n"),
            ("Page 3:\n\nThis is the End of Course 1. Press 'q' to select the next course.")
        ],
        2: [
            (f"Page 1:\n\nWelcome to Course 2, {name}!\nIn this course, we will dive deeper into Python programming.\n"
             "You will learn about functions, loops, and how to manage your code effectively.\n"
             "By the end of this course, you will be able to write more complex programs and understand how to debug them.\n"
             "Let's begin by discussing functions and how they can help you organize your code.\n"),
            ("Page 2:\n\nA function is a block of code that only runs when it is called.\n"
             "You can pass data, known as parameters, into a function.\n"
             "Here is a simple example:\n\n"
             "def my_function(parameter):\n"
             "    print(parameter)\n\n"
             "You can call this function with a specific value.\n"),
            ("Page 3:\n\nBut what about math in Python? Python has built-in mathematical operations!\n"
             "You can perform addition, subtraction, multiplication, and division.\n"
             "Let's practice some calculations before moving on!\n")
        ],
        3: [
            (f"Page 1:\n\nWelcome to Course 3, {name}!\n\n"
             "First, we need to download Python. You can press 'o' to open the Python website in your browser.\n"
             "Once you have Python installed, we will begin exploring advanced concepts such as object-oriented programming.\n"
             "This course will help you understand how to create your own classes and objects, making your code more organized.\n"),
            ("Page 2:\n\nIf you did all this correctly, you can officially enter the programming world! "
             "Press the right arrow to see the image!\n\n"
             "This is where you will see how to implement everything you learned in this course.\n"
             "Let's get started by looking at a simple class in Python!\n"),
            ("Page 3:\n\nEnd of Course 3. Press 'q' to select the next course. Thank you for using my prototype!")
        ]
    }

    pages_course = courses_content.get(course_number, ["This course is not available."])

    current_page = 0
    key = 0

    while key != ord('q'):
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()
        text = pages_course[current_page]
        lines = text.splitlines() if isinstance(text, str) else text

        for i, line in enumerate(lines):
            if len(line) > max_x - 2:
                line = line[:max_x - 2]
            if i < max_y - 1:
                stdscr.addstr(i, 1, line)

        stdscr.box()
        stdscr.addstr(max_y - 1, 1, "Use arrow keys (<-- or -->) or 'n'/'p' to navigate, 'q' to go back.")

        # Only display the 'o' prompt on Course 3, Page 1
        if course_number == 3 and current_page == 0:
            stdscr.addstr(max_y - 2, 1, "Press 'o' to open python.org in your browser.")
            stdscr.refresh()
            key = stdscr.getch()  # Get the key press here

            if key == ord('o'):
                webbrowser.open('https://www.python.org')
                continue  # Skip the rest of the loop to avoid moving to the next page

        # Detect if we're on Course 3, Page 2 and show the image
        if course_number == 3 and current_page == 1:
            stdscr.addstr(max_y - 2, 1, "Press the right arrow to see the image.")
            stdscr.refresh()
            key = stdscr.getch()

            if key == curses.KEY_RIGHT or key == ord('n'):
                a3.show()  # Open the image in a separate window

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_RIGHT or key == ord('n'):
            current_page = (current_page + 1) % len(pages_course)
        elif key == curses.KEY_LEFT or key == ord('p'):
            current_page = (current_page - 1) % len(pages_course)
        elif key == ord('q'):
            return 'toc'


# Main application loop
def main(stdscr):
    # Main application loop to display TOC and allow navigation between courses.
    curses.curs_set(0)
    course_number = initial_course_number

    while True:
        if course_number == 'quit':
            break
        elif course_number == 'toc':
            course_number = show_toc(stdscr)
        else:
            course_number = main1(stdscr, course_number)


# ----------------------------------------------------------------RUN THE CODE!!! YAY!!!!!---------------------------------------------------------------- #
if __name__ == '__main__':
    curses.wrapper(main)
