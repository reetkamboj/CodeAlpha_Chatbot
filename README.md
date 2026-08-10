# CodeAlpha_Chatbot

A simple rule-based chatbot built in Python. Completed as **Task 4: Basic Chatbot** for the CodeAlpha Python Programming Internship.

## Description
The chatbot reads a line typed by the user, checks it against a set of predefined keywords/phrases, and replies with a matching response. If nothing matches, it gives a fallback reply. The conversation loops until the user types an exit word like "bye".

## Concepts Used
- **`if`-`elif`-`else` statements** – compare the user's message against known keywords to choose a reply.
- **Functions** – `get_response()` handles the decision logic separately from `chat()`, which runs the conversation loop.
- **Loops** – a `while True` loop keeps the conversation going until an exit keyword is typed.
- **Input/Output** – `input()` reads what the user types; `print()` shows the chatbot's reply.
- **String methods** – `.lower()` and `.strip()` normalize input so matching works regardless of capitalization or extra spaces.

## Files
- `chatbot.py` – the chatbot
- `README.md` – this file

## How to Run
1. Make sure Python 3 is installed.
2. Run:
   ```
   python chatbot.py
   ```
3. Try typing `hello`, `how are you`, `help`, or `bye`.

## Example
```
Chatbot: Hi! Type 'bye' to end the conversation.

You: hello
Chatbot: Hi there! How can I help you today?
You: how are you
Chatbot: I'm fine, thanks! How about you?
You: bye
Chatbot: Goodbye! Have a great day!
```

## Possible Improvements
- Add more keywords/topics for richer conversation.
- Match on simple keyword similarity instead of exact phrases.
- Log the conversation to a file.
