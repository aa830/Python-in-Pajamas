import curses
import sys
from asciirenderer import ascii_art1, ascii_art2

# Get the name and course number passed as command-line arguments
name = sys.argv[1] if len(sys.argv) > 1 else "User"
initial_course_number = int(sys.argv[2]) if len(sys.argv) > 2 else 1

def display_toc_menu(stdscr):
    """Display the Table of Contents menu for course selection."""
    # List of available courses
    courses = [
        "Course 1: Introduction to Machine Language and Binary",
        "Course 2: Understanding Python",
        "Course 3: Binary Interaction with Memory"
    ]
    
    selected_course = 0
    key = 0
    quit_attempts = 0  # Counter for 'q' key presses

    while key != ord('\n'):  # Enter key to select
        stdscr.clear()

        # Get screen dimensions
        max_y, max_x = stdscr.getmaxyx()

        # Display the TOC menu
        stdscr.addstr(0, max_x // 2 - len("Table of Contents") // 2, "Table of Contents", curses.A_BOLD | curses.A_UNDERLINE)

        for idx, course in enumerate(courses):
            if idx == selected_course:
                stdscr.attron(curses.A_REVERSE)  # Highlight selected course
                stdscr.addstr(2 + idx, max_x // 2 - len(course) // 2, course)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(2 + idx, max_x // 2 - len(course) // 2, course)

        stdscr.addstr(max_y - 1, 1, "Use arrow keys to navigate, 'Enter' to select, or 'q' to exit.")

        # Refresh the screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Handle up and down arrow key navigation
        if key == curses.KEY_UP and selected_course > 0:
            selected_course -= 1
            quit_attempts = 0  # Reset quit attempts on navigation
        elif key == curses.KEY_DOWN and selected_course < len(courses) - 1:
            selected_course += 1
            quit_attempts = 0  # Reset quit attempts on navigation
        elif key == ord('q'):
            quit_attempts += 1
            if quit_attempts == 2:
                sys.exit()  # Exit the program on double 'q'
        else:
            quit_attempts = 0  # Reset on other key presses

    # Return the selected course number (1-indexed)
    return selected_course + 1

def main1(stdscr, course_number):
    """Main function to display course content."""
    stdscr.clear()

    # Get the ASCII artworks
    ascii_art1_content = ascii_art1.splitlines()  # Split into lines
    ascii_art2_content = ascii_art2.splitlines()  # Split into lines

    # Define content for each course
    courses_content = {
        1: [
            f"Page 1:\n\nHello {name}, welcome to your first lesson on Python in Pajamas!\n"
            "Since you are so curious to learn, let's get to it!\n\n\n"
            "So what is binary?\nYou know how sometimes in class or around other people, you don't want them to know what you are saying, so you speak a made-up language?\n"
            "Binary is exactly the same! It is a secret language that a computer uses to communicate between the different parts of the computer, for example the screen.\n"
            "The funny thing about this language, however, is that it only has two letters! 1, or 0!\n"
            "How would the computer be able to tell the other parts what to do with just 1s and 0s?\n"
            "Well, it works kind of like maths: a certain combination of 0s and 1s will make a certain letter or command:\n\n\n\n"
            "Here is a cute illustration so that you understand better!\n\n",
            ascii_art1_content,  # Store ASCII art directly
            "Page 2:\n\nContinuing....\nThat illustration shows the Central Processing Unit (CPU) telling the display to light up! By saying, 'Hello! You seem bright today!'\n"
            "Obviously, it's not as simple as giving the screen a compliment, but that is essentially how it works. The CPU is like the president, telling all the other parts what to do, and it uses binary to tell them what to do.\n\n"
            "To make it simple, let's say that you pressed 'a'. Think about it like the brain, when you touch something hot, your hand will quickly move back, right? It is essentially the same thing!\n"
            "When you press the 'a' key, Mr. A Key quickly sends a message using Binary to the CPU (aka the Brain), the CPU decides what to do. Let's say that in this case, the CPU decides to display the letter 'a' on the screen.\n"
            "The CPU sends a Binary message to Mr. Screen to display 'a'.\n\n"
            "Now you know what happens when you type into YouTube!\nEverything else that I have mentioned here, this is all called machine language. Now you know!",
            "Page 3:\n\n\n\n\n\nThis is the End of Course 1, Press the right arrow to continue to the next section!"
        ],
        2: [
            f"Page 1:\n\nWelcome to Course 2, {name}!\nThis course will focus on understanding how the Python Programming Language works.\n"
            "So what is Python?\nRemember we talked about how binary has 0s and 1s? Imagine if everybody had to code in 0s and 1s, what a pain that would be!\n"
            "That is why languages like Python exist. Think of it as a simplified version of the secret language: You can actually speak it!\n"
            "There are other languages like Python, such as C, C++, C#, but those are a little too tricky for your little minds!\n"
            "For now, let's stick to Python.\nWhere were we...ah! How does it work?\n"
            "When you code in Python, it basically converts the binary form of that into something that coders like you can understand.\n"
            "For example, rather than having to type a long line of 1s and 0s to print something (oh, what a headache!), in Python you can simply type:\n\n"
            '    print("Python is easy!")',
            f"Page 2:\n\nContinuing with Course 2...\nPython is known as a high-level language because it allows you to write instructions using human-friendly syntax...\nYou can think of high level programming languages as like a ladder: When you run a python script, it goes down the 'ladder' to the CPU which translates it into its own language\nAfter translating, the CPU sends out its order!\n\nFor the code above, the CPU will command the screen to print 'Python is easy!'\nMachine language is a 'low level' language because the CPU doesn't need to use that high of its power level to understand what the code wants to do!\n\n{ascii_art2_content}",
            "Page 3:\n\nEnd of Course 2, Chapter 1. Press the right arrow to continue."
        ],
        3: [
            f"Page 1:\n\nWelcome to Course 3, {name}!\nIn this lesson, we'll dive into how binary interacts with memory...\n"
            "Every action you take on a computer involves storing and retrieving data from memory...\n",
            "Page 2:\n\nCourse 3 continues with a deeper dive into memory management...\nUnderstanding how data is stored in bits...\n",
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

        # Display the text lines
        for i, line in enumerate(lines):
            # Truncate the line if too long
            if len(line) > max_x - 2:
                line = line[:max_x - 2]

            if i < max_y - 1:
                stdscr.addstr(i, 1, line)

        # Check if the current page is ASCII art and display it
        if isinstance(pagesCourse[current_page], list):  # If it's ASCII art
            for ascii_line in pagesCourse[current_page]:
                if i < max_y - 1:
                    stdscr.addstr(i, 1, ascii_line)
                    i += 1  # Move to the next line

        # Draw a border around the text box
        stdscr.box()

        # Display navigation instructions
        stdscr.addstr(max_y - 1, 1, "Use arrow keys or 'n'/'p' to navigate, 'q' to go to the Table of Contents.")

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

    """Main function to display course content."""
    # Clear screen
    stdscr.clear()

    # Get the ASCII artworks
    ascii_art1_content = ascii_art1
    ascii_art2_content = ascii_art2

    # Define content for each course
    courses_content = {
        1: [
            f"Page 1:\n\nHello {name}, welcome to your first lesson on Python in Pajamas!\n"
            "Since you are so curious to learn, let's get to it!\n\n\n"
            "So what is binary?\nYou know how sometimes in class or around other people, you don't want them to know what you are saying, so you speak a made-up language?\n"
            "Binary is exactly the same! It is a secret language that a computer uses to communicate between the different parts of the computer, for example the screen.\n"
            "The funny thing about this language, however, is that it only has two letters! 1, or 0!\n"
            "How would the computer be able to tell the other parts what to do with just 1s and 0s?\n"
            "Well, it works kind of like maths: a certain combination of 0s and 1s will make a certain letter or command:\n\n\n\n"
            f"Here is a cute illustration so that you understand better!\n\n{ascii_art1_content}\n\n",
            "Page 2:\n\nContinuing....\nThat illustration shows the Central Processing Unit (CPU) telling the display to light up! By saying, 'Hello! You seem bright today!'\n"
            "Obviously, it's not as simple as giving the screen a compliment, but that is essentially how it works. The CPU is like the president, telling all the other parts what to do, and it uses binary to tell them what to do.\n\n"
            "To make it simple, let's say that you pressed 'a'. Think about it like the brain, when you touch something hot, your hand will quickly move back, right? It is essentially the same thing!\n"
            "When you press the 'a' key, Mr. A Key quickly sends a message using Binary to the CPU (aka the Brain), the CPU decides what to do. Let's say that in this case, the CPU decides to display the letter 'a' on the screen.\n"
            "The CPU sends a Binary message to Mr. Screen to display 'a'.\n\n"
            "Now you know what happens when you type into YouTube!\nEverything else that I have mentioned here, this is all called machine language. Now you know!",
            "Page 3:\n\n\n\n\n\nThis is the End of Course 1, Press the right arrow to continue to the next section!"
        ],
        2: [
            f"Page 1:\n\nWelcome to Course 2, {name}!\nThis course will focus on understanding how the Python Programming Language works.\n"
            "So what is Python?\nRemember we talked about how binary has 0s and 1s? Imagine if everybody had to code in 0s and 1s, what a pain that would be!\n"
            "That is why languages like Python exist. Think of it as a simplified version of the secret language: You can actually speak it!\n"
            "There are other languages like Python, such as C, C++, C#, but those are a little too tricky for your little minds!\n"
            "For now, let's stick to Python.\nWhere were we...ah! How does it work?\n"
            "When you code in Python, it basically converts the binary form of that into something that coders like you can understand.\n"
            "For example, rather than having to type a long line of 1s and 0s to print something (oh, what a headache!), in Python you can simply type:\n\n"
            '    print("Python is easy!")',
            f"Page 2:\n\nContinuing with Course 2...\nPython is known as a high-level language because it allows you to write instructions using human-friendly syntax...\nYou can think of high level programming languages as like a ladder: When you run a python script, it goes down the 'ladder' to the CPU which translates it into its own language\nAfter translating, the CPU sends out its order!\n\nFor the code above, the CPU will command the screen to print 'Python is easy!'\nMachine language is a 'low level' language because the CPU doesn't need to use that high of its power level to understand what the code wants to do!\n\n{ascii_art2_content}",
            "Page 3:\n\nEnd of Course 2, Chapter 1. Press the right arrow to continue."
        ],
        3: [
            f"Page 1:\n\nWelcome to Course 3, {name}!\nIn this lesson, we'll dive into how binary interacts with memory...\n"
            "Every action you take on a computer involves storing and retrieving data from memory...\n",
            "Page 2:\n\nCourse 3 continues with a deeper dive into memory management...\nUnderstanding how data is stored in bits...\n",
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
        stdscr.addstr(max_y - 1, 1, "Use arrow keys or 'n'/'p' to navigate, 'q' to go to the Table of Contents.")

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

def main():
    """Main entry point for the program."""
    # Launch the TOC menu and get the selected course number
    course_number = curses.wrapper(display_toc_menu)

    # Launch the main content display for the selected course
    curses.wrapper(main1, course_number)

if __name__ == "__main__":
    main()
