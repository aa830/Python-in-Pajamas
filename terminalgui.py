import curses
import sys
from asciirenderer import get_ascii_art

# Get the name passed as a command-line argument
name = sys.argv[1] if len(sys.argv) > 1 else "User"

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Get the ASCII art
    ascii_art = get_ascii_art()

    # Sample text for demonstration, split into pages
    pages = [
        f"Page 1:\n\nHello {name}, welcome to your first lesson on Python in Pajamas!\nSince you are so curious to learn, let's get to it!\n\n\nSo what is binary?\nYou know how sometimes in class or around other people, you don't want them to know what you are saying, so you speak a made-up language?\nBinary is exactly the same! It is a secret language that a computer uses to communicate between the different parts of the computer, for example the screen.\nThe funny thing about this language, however, is that it only has two letters! 1, or 0!\nHow would the computer be able to tell the other parts what to do with just 1s and 0s?\nWell, it works kind of like maths: a certain combination of 0s and 1s will make a certain letter or command\n\n\n\nHere is a cute illustration so that you understand better!\n\n" + ascii_art + "\n\n",
        "Page 2:\n\nContinuing....\nThat illustration shows the Central Processing Unit (CPU) telling the display to light up! By saying, 'Hello! You seem bright today!'\nObviously, it's not as simple as giving the screen a compliment, but that is essentially how it works. The CPU is like the president, telling all the other parts what to do, and it uses binary to tell them what to do.",
        "Page 3:\n\n\n\n\n\nThis is the End of Course 1, Chapter 1. Press the right arrow to continue to the next section!"
    ]

    # Initialize variables
    current_page = 0
    key = 0

    # Main loop
    while key != ord('q'):
        stdscr.clear()
        
        # Get screen dimensions
        max_y, max_x = stdscr.getmaxyx()

        # Display the current page text
        text = pages[current_page]
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if len(line) > max_x - 2:
                line = line[:max_x - 2]  # Truncate the line if too long
            
            if i + 1 < max_y - 1:
                stdscr.addstr(i + 1, 1, line)
        
        # Draw a border around the text box
        stdscr.box()

        # Display navigation instructions
        stdscr.addstr(max_y - 1, 1, "Use arrow keys or 'n'/'p' to navigate, 'q' to quit.")
        
        # Refresh the screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Handle navigation
        if key in [curses.KEY_RIGHT, ord('n')]:
            if current_page < len(pages) - 1:
                current_page += 1
        elif key in [curses.KEY_LEFT, ord('p')]:
            if current_page > 0:
                current_page -= 1

if __name__ == "__main__":
    curses.wrapper(main)
