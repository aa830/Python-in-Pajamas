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
        "Binary and Memory Management"
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
    # Main function to display course content.
    stdscr.clear()
    a1 = ascii_art1()
    a2 = ascii_art2()
    a3 = Image.open('Screenshot 2024-10-28 at 4.10.11 PM.png')

    # ----------------------------------------------------------------INIT VARIABLES AND WRITE COURSE CONTENTS---------------------------------------------------------------- #

    # Define content for each course using a character string
    courses_content = {
        1: [
            (
                f"Page 1:\n\nHello {name}, welcome to your first lesson on Python in Pajamas!\n"
                "Since you are so curious to learn, let's get to it!\n\n"
                "So, what is binary?\n\n"
                "You know how sometimes, in class or around others, you don't want them to know "
                "what you're saying, so you speak a made-up language?\n\n"
                "Binary is exactly the same! It's a secret language that computers use to "
                "communicate between different parts, like the screen.\n\n"
                "The funny thing about this language is that it only has two 'letters': 1 and 0!\n\n"
                "But how does the computer communicate with just 1s and 0s?\n\n"
                "It works like math: a certain combination of 0s and 1s will represent a letter or command.\n\n"
                "Here's a cute illustration to help you understand better:\n\n"
                f"{a1}\n"
            ),
            (
                "Page 2:\n\nContinuing...\n\n"
                "That illustration shows the Central Processing Unit (CPU) telling the display to light up!\n"
                "The CPU acts like the brain of the computer, giving instructions to all other parts, "
                "and it uses binary to do that.\n\n"
                "For example, when you press the 'a' key on your keyboard, the CPU decides to display 'a' "
                "on the screen by sending a binary message to the display.\n\n"
                "Everything we've described so far is called 'machine language'—now you know!"
            ),
            (
                "Page 3:\n\nThis is the End of Course 1. Press 'q' to select the next course."
            )
        ],
        2: [
            (
                f"Page 1:\n\nWelcome to Course 2, {name}!\n"
                "In this course, we'll dive into how Python programming works.\n\n"
                "So, what is Python?\n\n"
                "Remember how we talked about binary (0s and 1s)? Imagine if everyone had to code in binary!"
                " It would be so hard, right?\n\n"
                "That's where languages like Python come in—they make coding easier by letting you use words.\n\n"
                "There are other languages like Python (e.g., C, C++, Java), but for now, let's focus on Python.\n\n"
                "Instead of writing long sequences of 1s and 0s to make the computer do something, you can simply write:\n\n"
                '    print("Python is easy!")\n\n'
                "Python translates this code into binary, and the CPU understands it."
            ),
            (
                f"Page 2:\n\nContinuing with Course 2...\n\n"
                "Python is known as a 'high-level' programming language because it lets you write "
                "commands in words you can understand.\n\n"
                "When you run a Python script, it translates your code into machine language "
                "so the CPU can execute it.\n\n"
                "For example, the code from the previous page tells the CPU to print 'Python is easy!' "
                "on the screen.\n\n"
                "Here's another illustration of how Python and the CPU interact:\n\n"
                f"{a2}\n"
            ),
            (
                "Page 3:\n\nBut what about math in Python?\n\n"
                "Python can handle math really well! It uses symbols called 'operators' to perform "
                "arithmetic operations like addition, subtraction, multiplication, and division.\n\n"
                "For example:\n\n"
                "    1 * 3  # Multiplication\n"
                "    1 / 3  # Division\n\n"
                "Plus and minus work just like you'd expect!\n\n"
                "Let's write a simple Python program that adds two numbers:\n\n"
                '    number = input("Enter a number: ")\n'
                '    new_number = 1 + int(number)\n'
                '    print(f"Your new number is: {new_number}")\n\n'
                "Notice how we use 'input()' to get user input and 'int()' to make sure it's treated as a number."
            )
        ],
        3: [
            (
                f"Page 1:\n\nWelcome to Course 3, {name}!\n"
                "In this course, we'll explore how you can start programming!\n\n"
                "First, we need to download Python. You can press 'o' to open the Python website in your browser.\n\n"
                "After downloading, just double-click the file!\n\n"
                "If there is an option called 'add to PATH', make sure to select it. "
                "Then all you need to do is click install, and voila! You have Python!\n\n"
                "But... how do you write the code and test if it works?\n\n"
                "You should download Thonny! You can go to their website (https://thonny.org/) or use the terminal and type:\n\n"
                "    pip3 install thonny\n\n"
                "Thonny is like Google Docs, but for Python programming. "
                "Not only can you write code, it tries to help you fix errors!\n\n"
                "You can also run your code with the push of a button. Amazing, isn't it?"
            ),
            (
                "Page 2:\n\nIf you did all this correctly, you can officially enter the programming world! "
                "Congrats!\n\n(P.S. your Thonny should look something like this)\n\n"
            ),
            (
                "Page 3:\n\nEnd of Course 3. Press 'q' to select the next course."
            )
        ]
    }

    # Get the content for the selected course
    pages_course = courses_content.get(course_number, ["This course is not available."])

    # Initialize variables
    current_page = 0
    key = 0

    # ----------------------------------------------------------------DEFINING KEYBINDS---------------------------------------------------------------- #

    # Main loop
    while key != ord('q'):
        stdscr.clear()

        # Get screen dimensions
        max_y, max_x = stdscr.getmaxyx()

        # Display the current page text
        text = pages_course[current_page]
        lines = text.splitlines() if isinstance(text, str) else text

        for i, line in enumerate(lines):
            if len(line) > max_x - 2:
                line = line[:max_x - 2]

            if i < max_y - 1:
                stdscr.addstr(i, 1, line)

        stdscr.box()
        stdscr.addstr(max_y - 1, 1, "Use arrow keys (<-- or -->) or 'n'/'p' to navigate, 'q' to go back.")

        # Detect if we're on Course 3, Page 1 and prompt the user to open the website
        if course_number == 3 and current_page == 0:
            stdscr.addstr(max_y - 2, 1, "Press 'o' to open python.org in your browser.")
            key = stdscr.getch()

            if key == ord('o'):
                # Open the python.org website
                webbrowser.open('https://www.python.org')

        # Detect if we're on Course 3, Page 2 and show the image
        if course_number == 3 and current_page == 1:
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
