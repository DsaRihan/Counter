def count_words(text):
    """
    Function to count the number of words in a given text.
    A word is defined as any sequence of characters separated by spaces.
    """
    words = text.split()  # Split the text by spaces to get individual words
    return len(words)  # Return the number of words


def word_counter():
    """
    Function to handle user input for counting words.
    Includes error handling for empty input and displays the word count.
    """
    print("Enter a sentence or paragraph to count the words:")
    user_input = input("> ").strip()  # Strip removes leading/trailing whitespaces

    # Error handling for empty input
    if not user_input:
        print("Error: Input cannot be empty. Please try again.")
        return

    # Call the word counting function
    word_count = count_words(user_input)

    # Display the result
    print(f"The total number of words in the given text is: {word_count}\n")


def main():
    """
    Main function to display the menu and handle user choices.
    Runs infinitely until the user chooses to exit.
    """
    while True:
        # Display menu
        print("=== Word Counter Menu ===")
        print("1. Count the number of words")
        print("2. Exit")
        print("=========================")

        # Get user choice
        choice = input("Enter your choice (1 or 2): ").strip()

        # Handle user choices
        if choice == "1":
            word_counter()
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")


# Entry point of the program
if __name__ == "__main__":
    main()
