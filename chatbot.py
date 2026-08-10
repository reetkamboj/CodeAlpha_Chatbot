"""
A simple rule-based chatbot that responds to predefined inputs.
Concepts used: if-elif, functions, loops, input/output
"""

EXIT_WORDS = ("bye", "goodbye", "exit", "quit")


def get_response(user_input):
    """Return a predefined response based on user's input."""
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi there! How can I help you today?"
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"
    elif "your name" in text:
        return "I'm a simple chatbot built for the CodeAlpha internship."
    elif "help" in text:
        return "You can say hello, ask how I am, ask my name, or say bye to exit."
    elif text in EXIT_WORDS:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def chat():
    print("Chatbot: Hi! Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if user_input.lower().strip() in EXIT_WORDS:
            break


if __name__ == "__main__":
    chat()
