import curses
import sys
from asciirenderer import ascii_art1, ascii_art2
import webbrowser
from PIL import Image
import textwrap

# ----------------------------------------------------------------DEFINING VARIABLES---------------------------------------------------------------- #

# Get the name and course number passed as command-line arguments
name = sys.argv[1] if len(sys.argv) > 1 else "User"
initial_course_number = int(sys.argv[2]) if len(sys.argv) > 2 else 1

# Function to wrap text to fit the terminal width
def wrap_text(text, width):
    wrapped_lines = []
    for line in text.splitlines():
        wrapped_lines.extend(textwrap.wrap(line, width=width))
    return wrapped_lines

# Table of contents menu for user to choose next course
def show_toc(stdscr):
    stdscr.clear()
    toc_options = [
        "Introduction to Python in Pajamas",
        "Understanding Python Programming",
        "Setting up Python"
    ]
    
    toc_text = f"Welcome, {name}!\n\nUse the arrow keys to select a course and press Enter:\n"
    lines = toc_text.splitlines()
    max_y, max_x = stdscr.getmaxyx()

    selected_option = 0

    while True:
        stdscr.clear()

        for i, line in enumerate(lines):
            if i < max_y - 1:
                stdscr.addstr(i + 1, 1, line)

        for idx, option in enumerate(toc_options):
            if idx == selected_option:
                stdscr.addstr(len(lines) + 2 + idx, 2, f"> {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(len(lines) + 2 + idx, 2, f"  {option}")

        stdscr.addstr(max_y - 1, 1, "Press 'q' to quit.")
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and selected_option > 0:
            selected_option -= 1
        elif key == curses.KEY_DOWN and selected_option < len(toc_options) - 1:
            selected_option += 1
        elif key == ord('\n'):
            return selected_option + 1
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
        ]
    }

    pages_course = courses_content.get(course_number, ["This course is not available."])
    current_page = 0
    key = 0
    max_y, max_x = stdscr.getmaxyx()

    quit_pressed = False

    while True:
        stdscr.clear()
        text = pages_course[current_page]
        lines = wrap_text(text, max_x - 2)  # Wrap text to terminal width

        for i, line in enumerate(lines):
            if i < max_y - 1:
                stdscr.addstr(i, 1, line)

        stdscr.box()
        stdscr.addstr(max_y - 1, 1, "Use arrow keys (<-- or -->) or 'n'/'p' to navigate, 'q' to go back.")

        if course_number == 3 and current_page == 0:
            stdscr.addstr(max_y - 2, 1, "Press 'o' to open python.org in your browser.")
            key = stdscr.getch()

            if key == ord('o'):
                webbrowser.open('https://www.python.org')

        elif course_number == 3 and current_page == 1:
            a3.show()

        else:
            key = stdscr.getch()

        if key == curses.KEY_RIGHT or key == ord('n'):
            current_page = (current_page + 1) % len(pages_course)
        elif key == curses.KEY_LEFT or key == ord('p'):
            current_page = (current_page - 1) % len(pages_course)
        elif key == ord('q'):
            if quit_pressed:
                return 'quit'
            else:
                quit_pressed = True
                return 'toc'

# Run the application
def main(stdscr):
    curses.curs_set(0)
    selected_course = initial_course_number

    if selected_course == 'quit':
        return

    main1(stdscr, selected_course)

if __name__ == "__main__":
    curses.wrapper(main)
