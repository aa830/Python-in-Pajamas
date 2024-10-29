import curses
from PIL import Image

# Sample images for course illustrations (make sure to have these images)
a1 = "path/to/your/image1.png"  # Replace with actual image path
a2 = "path/to/your/image2.png"  # Replace with actual image path

# Define your courses content
name = "Student"  # You can change this to the actual user's name
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
            "Congrats!\n\n(P.S. your Thonny should look something like this). Press the right arrow to see the image!\n\n"
        ),
        (
            "Page 3:\n\nEnd of Course 3. Press 'q' to select the next course. Thank you for using my prototype!"
        )
    ]
}

def display_text(stdscr, text):
    stdscr.clear()
    stdscr.addstr(text)
    stdscr.refresh()
    stdscr.getch()

def display_courses(stdscr):
    current_course = 1
    while True:
        for page in courses_content[current_course]:
            display_text(stdscr, page)
        
        # Navigation to the next course
        key = stdscr.getch()
        if key == ord('q') and current_course < len(courses_content):
            current_course += 1
        elif key == ord('o'):
            # Here you can add logic to open a URL for downloading Python
            pass

def main():
    curses.wrapper(display_courses)

if __name__ == "__main__":
    main()
