import curses
import sys
from asciirenderer import get_ascii_art

# Get the name and course number passed as command-line arguments
name = sys.argv[1] if len(sys.argv) > 1 else "User"
course_number = int(sys.argv[2]) if len(sys.argv) > 2 else 1

def main1(stdscr):
    # Clear screen
    stdscr.clear()

    # Get the ASCII art
    ascii_art = get_ascii_art()

    # Define content for each course
    courses_content = {
        1: [
            f"Page 1:\n\nHello {name}, welcome to your first lesson on Python in Pajamas!\n"
            f"Since you are so curious to learn, let's get to it!\n\n\n"
            f"So what is binary?\nYou know how sometimes in class or around other people, you don't want them to know what you are saying, so you speak a made-up language?\n"
            f"Binary is exactly the same! It is a secret language that a computer uses to communicate between the different parts of the computer, for example the screen.\n"
            f"The funny thing about this language, however, is that it only has two letters! 1, or 0!\n"
            f"How would the computer be able to tell the other parts what to do with just 1s and 0s?\n"
            f"Well, it works kind of like maths: a certain combination of 0s and 1s will make a certain letter or command:\n\n\n\n"
            f"Here is a cute illustration so that you understand better!\n\n{ascii_art}\n\n",
            "Page 2:\n\nContinuing....\nThat illustration shows the Central Processing Unit (CPU) telling the display to light up! By saying, 'Hello! You seem bright today!'\n"
            "Obviously, it's not as simple as giving the screen a compliment, but that is essentially how it works. The CPU is like the president, telling all the other parts what to do, and it uses binary to tell them what to do.\n\n"
            "To make it simple, let's say that you pressed 'a'. Think about it like the brain, when you touch something hot, your hand will quickly move back, right? It is essentially the same thing!\n"
            "When you press the 'a' key, Mr. A Key quickly sends a message using Binary to the CPU (aka the Brain), the CPU decides what to do. Let's say that in this case, the CPU decides to display the letter 'a' on the screen.\n"
            "The CPU sends a Binary message to Mr. Screen to display 'a'.\n\n"
            "Now you know what happens when you type into YouTube!",
            "Page 3:\n\n\n\n\n\nThis is the End of Course 1, Chapter 1. Press the right arrow to continue to the next section!"
        ],
        2: [
            "Page 1:\n\nWelcome to Course 2, {name}!\nThis course will focus on understanding how binary translates to machine code.\n...",
            "Page 2:\n\nContinuing with Course 2...\n",
            "Page 3:\n\nEnd of Course 2, Chapter 1. Press the right arrow to continue."
        ],
        3: [
            "Page 1:\n\nWelcome to Course 3, {name}!\nIn this lesson, we'll dive into how binary interacts with memory...\n",
            "Page 2:\n\nCourse 3 continues with a deeper dive into memory management...\n",
            "Page 3:\n\nEnd of Course 3, Chapter 1. Press the right arrow to continue."
        ]
    }

    # Get the content for the selected course
    pagesCourse = courses_content.get(course_number, ["This course is not available."])

    # Initialize variables
    current_page = 0
    key = 0

    # Main loop
    while key != ord('q'):
        stdscr.clear()

        # Get screen dimensions
        max_y, max_x = stdscr.getmaxyx()

        # Display the current page text
        text = pagesCourse[current_page]
        lines = text.splitlines()

        for i, line in enumerate(lines):
            # Truncate the line if too long
            if len(line) > max_x - 2:
                line = line[:max_x - 2]

            if i < max_y - 1:
                stdscr.addstr(i, 1, line)

        # Draw a border around the text box
        stdscr.box()

        # Display navigation instructions
        stdscr.addstr(max_y - 1, 1, "Use arrow keys or 'n'/'p' to navigate, 'q' to quit.")

        # Refresh the screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Handle navigation (keybinds)
        if key in [curses.KEY_RIGHT, ord('n')]:
            if current_page < len(pagesCourse) - 1:
                current_page += 1
        elif key in [curses.KEY_LEFT, ord('p')]:
            if current_page > 0:
                current_page -= 1

if __name__ == "__main__":
    curses.wrapper(main1)