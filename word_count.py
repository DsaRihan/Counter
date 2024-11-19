def count_words(text):
    words = text.split()
    return len(words)

def count_characters(input_string, include_spaces=True):
    if include_spaces:
        return len(input_string)
    else:
        return len(input_string.replace(" ", ""))

def word_counter():
    user_input = input("> ").strip()

    if not user_input:
        print("Error: Input cannot be empty. Please try again.\n")
        return

    word_count = count_words(user_input)
    char_count_incl_spaces = count_characters(user_input)
    char_count_excl_spaces = count_characters(user_input, include_spaces=False)

    print("\n=== Analysis Result ===")
    print(f"Total number of words: {word_count}")
    print(f"Total number of characters (including spaces): {char_count_incl_spaces}")
    print(f"Total number of characters (excluding spaces): {char_count_excl_spaces}")
    print("=======================\n")

def main():
    while True:
        print("=== Word & Character Counter Menu ===")
        print("1. Analyze text")
        print("2. Exit")
        print("=====================================")

        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            word_counter()
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")

if __name__ == "__main__":
    main()
