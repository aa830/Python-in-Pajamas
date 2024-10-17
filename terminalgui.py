import curses
from asciirenderer import get_ascii_art  # Import the function
from pythoninpajamas import name

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Get the ASCII art
    ascii_art = get_ascii_art()

    # Sample text for demonstration, split into pages
    pages = [
        "Page 1:\n\nHello {name}, welcome to your first lesson on Python in Pajamas!\nSince you are so curious to learn, lets get to it!\n\n\nSo what is binary?\nYou know how sometimes in class or around other people, you dont want them to know what you are saying, so you speak a made up language?\n Binary is exactly the same! It is a secret language that a computer uses to communicate between the different parts of the computer, for example the screen.\n The funny thing about this language, however is that it only has two letters! 1, or 0!\n How would the computer be able to tell the other parts what to do with just 1s and 0s?\n Well, it works kind of like maths: a certain combination of 0s and 1s will make a certain letter or command\n\n\n\nHere is a cute illustration so that you understand better!\n\n" + ascii_art + "\n\n" ,
        "Page 2:\n\nContinuing....\nThat illustration shows the Central Processing Unit (CPU) telling the display to light up! By saying, ""Hello! you same look bright today!""\nObviously, its not as simple as giving the screen a compliement, but that is essentially how it works. The CPU is like the president, telling all the other parts what to do, and it uses binary to tell them what to do. ",
        "Page 3:\n\n\n\n\n\n This is the End of Course 1, Chapter 1, press the right arrow to continue to the next section!."
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
            # Check if the line exceeds the maximum width
            if len(line) > max_x - 2:  # Leave space for borders
                line = line[:max_x - 2]  # Truncate the line
            
            if i + 1 < max_y - 1:  # Ensure we don't exceed the window height
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
            # Go to the next page if there is one
            if current_page < len(pages) - 1:
                current_page += 1
        elif key in [curses.KEY_LEFT, ord('p')]:
            # Go to the previous page if possible
            if current_page > 0:
                current_page -= 1

if __name__ == "__main__":
    curses.wrapper(main)
