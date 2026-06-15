
import random
import re

# ── Response rules: each entry is (regex_pattern, [replies]) ─
# The chatbot picks a random reply from the matching list.
RULES: list[tuple[str, list[str]]] = [
    # Greetings
    (r"\b(hi|hello|hey|howdy|hiya)\b",
     ["Hi there! 😊", "Hello! How can I help?", "Hey! Nice to see you!"]),

    # How are you
    (r"\bhow are you\b|\bhow('?re| are) (you|u)\b",
     ["I'm doing great, thanks for asking! 😄",
      "Feeling wonderful! How about you?",
      "All systems go! 🤖"]),

    # User is fine
    (r"\bi('?m| am) (fine|good|great|okay|ok|well)\b",
     ["That's great to hear! 😊",
      "Wonderful! Is there anything I can help you with?"]),

    # Name questions
    (r"\bwhat('?s| is) your name\b|\bwho are you\b",
     ["I'm ChatBot, your friendly assistant! 🤖",
      "They call me ChatBot — nice to meet you!"]),

    # Capabilities
    (r"\bwhat can you do\b|\bhelp\b",
     ["I can chat with you, answer simple questions, and keep you company! 😊",
      "Try asking me how I'm doing, what time it is, or tell me a joke!"]),

    # Time / date
    (r"\bwhat (time|day|date) is it\b|\btime\b|\bdate\b",
     ["I don't have a clock, but your device can tell you! ⏰"]),

    # Jokes
    (r"\btell me a joke\b|\bjoke\b",
     ["Why do programmers prefer dark mode? Because light attracts bugs! 🐛😄",
      "Why did the Python programmer break up? Too many exceptions! 😂",
      "How do you comfort a JavaScript developer? You console them! 🖥️"]),

    # Weather
    (r"\bweather\b",
     ["I wish I could check the weather, but I'm just a simple chatbot! Try a weather app. ☀️"]),

    # Thank you
    (r"\b(thanks|thank you|thx|ty)\b",
     ["You're welcome! 😊", "Happy to help!", "Anytime! 🙌"]),

    # Goodbye
    (r"\b(bye|goodbye|see you|cya|exit|quit)\b",
     ["Goodbye! Have a great day! 👋",
      "See you later! Take care! 😊",
      "Bye bye! Come chat again soon! 🤖"]),

    # Sadness / problems
    (r"\b(sad|unhappy|depressed|upset|not okay)\b",
     ["I'm sorry to hear that. 😔 Remember, tough times don't last!",
      "I hope things get better soon. You've got this! 💪"]),

    # Fun / bored
    (r"\b(bored|boring)\b",
     ["Let's play a game — ask me to tell you a joke! 😄",
      "How about a fun fact? Python was named after Monty Python, not the snake! 🐍"]),

    # Affirmations
    (r"\b(yes|yeah|yep|yup|sure|absolutely)\b",
     ["Great! 😊", "Awesome! What's next?", "Perfect!"]),

    # Negations
    (r"\b(no|nope|nah|not really)\b",
     ["Okay, no problem!", "Alright, let me know if you need anything else."]),
]

FALLBACK_REPLIES = [
    "Hmm, I'm not sure I understand. Could you rephrase?",
    "Interesting! I'm still learning. 🤔",
    "I didn't quite catch that. Try asking something else!",
    "Could you elaborate? I want to help! 😊",
]


def get_response(user_input: str) -> str:
    """Return the best matching reply for user_input."""
    text = user_input.lower().strip()

    for pattern, replies in RULES:
        if re.search(pattern, text):
            return random.choice(replies)

    return random.choice(FALLBACK_REPLIES)


def chat() -> None:
    print("\n" + "=" * 50)
    print("   🤖 CodeAlpha BasicChatbot")
    print("=" * 50)
    print("  Type a message and press Enter.")
    print("  Say 'bye' or 'quit' to exit.\n")

    while True:
        try:
            user_input = input("  You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Bot: Goodbye! 👋\n")
            break

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"  Bot: {response}\n")

        # Exit on farewell
        if re.search(r"\b(bye|goodbye|cya|see you|exit|quit)\b", user_input.lower()):
            break


if __name__ == "__main__":
    chat()
