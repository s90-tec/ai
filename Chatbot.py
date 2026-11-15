
# Simple Rule-Based Chatbot

while True:

    msg = input("You: ").lower()

    if "hello" in msg or "hi" in msg:
        print("Bot: Hello! How are you?")

    elif "name" in msg:
        print("Bot: I am a Python Chatbot.")

    elif "how are you" in msg:
        print("Bot: I am fine. Thank you!")

    elif "bye" in msg:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
