import curses
import sys
from asciirenderer import ascii_art1, ascii_art2

# Get the name and course number passed as command-line arguments
name = sys.argv[1] if len(sys.argv) > 1 else "User"
initial_course_number = int(sys.argv[2]) if len(sys.argv) > 2 else 1


#Table of contents menu for user to choose next course
def show_toc(stdscr):
    """Display the Table of Contents and allow the user to choose a course using arrow keys."""
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

def main1(stdscr, course_number):
    """Main function to display course content."""
    stdscr.clear()
    a1 = ascii_art1()
    a2 = ascii_art2()

    # Define content for each course
    courses_content = {
        1: [
            (
                f"Page 1:\n\nHello {name}, welcome to your first lesson on Python in Pajamas!\n"
                "Since you are so curious to learn, let's get to it!\n\n"
                "So, what is binary?\nYou know how sometimes in class or around other people, you don't want them to know what you are saying, so you speak a made-up language?\n"
                "Binary is exactly the same! It is a secret language that a computer uses to communicate between the different parts of the computer, like the screen.\n"
                "The funny thing about this language is that it only has two letters: 1 and 0!\n"
                "How would the computer be able to tell the other parts what to do with just 1s and 0s?\n"
                "Well, it works kind of like math: a certain combination of 0s and 1s will make a certain letter or command.\n\n"
                "Here is a cute illustration so that you understand better:\n\n"
                f"{a1}\n"
            ),
            (
                "Page 2:\n\nContinuing...\nThat illustration shows the Central Processing Unit (CPU) telling the display to light up! By saying, 'Hello! You seem bright today!'\n"
                "Obviously, it's not as simple as giving the screen a compliment, but that is essentially how it works. The CPU is like the president, telling all the other parts what to do, and it uses binary to do that.\n\n"
                "To make it simple, let's say that you pressed 'a'. Think about it like the brain, when you touch something hot, your hand will quickly move back, right? It is essentially the same thing!\n"
                "When you press the 'a' key, Mr. A Key quickly sends a message using Binary to the CPU (aka the Brain), and the CPU decides what to do. In this case, the CPU decides to display the letter 'a' on the screen.\n"
                "The CPU sends a Binary message to Mr. Screen to display 'a'.\n\n"
                "Now you know what happens when you type into YouTube!\nEverything I have mentioned here is called, ""machine language"". Now you know!\n"
            ),
            (
                "Page 3:\n\nThis is the End of Course 1. Press ""q"" to select the next course."
            )
        ],
        2: [
            (
                f"Page 1:\n\nWelcome to Course 2, {name}!\nThis course will focus on understanding how the Python Programming Language works.\n"
                "So, what is Python?\nRemember we talked about how binary has 0s and 1s? Imagine if everybody had to code in 0s and 1s, what a pain that would be!\n"
                "That is why languages like Python exist. Think of it as a simplified version of the secret language: You can actually speak it!\n"
                "There are other languages like Python, such as C, C++, C#, but those are a little too tricky for your little minds!\n"
                "For now, let's stick to Python.\nWhere were we... ah! How does it work?\n"
                "When you code in Python, it converts the binary form into something that coders like you can understand.\n"
                "For example, rather than having to type a long line of 1s and 0s to print something (oh, what a headache!), in Python you can simply type:\n\n"
                '    print("Python is easy!")\n'
            ),
            (
                f"Page 2:\n\nContinuing with Course 2...\nPython is known as a ""high-level"" language because it allows you to write instructions using words that you can understand:.\n"
                "You can think of high-level programming languages like a ladder: When you run a Python script, it goes down the 'ladder' to the CPU, which translates it into its own language.\n"
                "After translating, the CPU sends out its order!\n\n"
                "For the code above, the CPU will command the screen to print 'Python is easy!'\n"
                "Machine language is a 'low-level' language because the CPU doesn't need to use that high of its power level to understand what the code wants to do!\n\n"
                f"{a2}\n"
            ),
            (
                "Page 3:\n\nEnd of Course 2, Chapter 1. Press ""q"" to select the next course."
            )
        ],
        3: [
            (
                f"Page 1:\n\nWelcome to Course 3, {name}!\nIn this lesson, we'll dive into how binary interacts with memory...\n"
                "Every action you take on a computer involves storing and retrieving data from memory...\n"
            ),
            (
                "Page 2:\n\nCourse 3 continues with a deeper dive into memory management...\n"
                "Understanding how data is stored in bits...\n"
            ),
            (
                "Page 3:\n\nEnd of Course 3, Chapter 1. Press ""q"" to select the next course."
            )
        ]
    }

    # Get the content for the selected course
    pages_course = courses_content.get(course_number, ["This course is not available."])

    # Initialize variables
    current_page = 0
    key = 0

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

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_RIGHT or key == ord('n'):
            current_page = (current_page + 1) % len(pages_course)
        elif key == curses.KEY_LEFT or key == ord('p'):
            current_page = (current_page - 1) % len(pages_course)
        elif key == ord('q'):
            return 'toc'

def main(stdscr):
    """Main entry point of the program."""
    course_number = initial_course_number
    while True:
        result = main1(stdscr, course_number) if course_number else show_toc(stdscr)
        if result == 'quit':
            break
        elif result == 'toc':
            course_number = None
        elif isinstance(result, int):
            course_number = result

if __name__ == "__main__":
    curses.wrapper(main)

