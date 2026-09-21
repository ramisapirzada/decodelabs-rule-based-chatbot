
def chatbot():
    print("===================================")
    print("   Welcome to AI Learning Companion")
    print("===================================")
    print("Type 'help' to see available topics.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you learn today?")

        elif user_input == "help":
            print("Bot: You can ask me about:")
            print("- Artificial Intelligence")
            print("- Machine Learning")
            print("- Python")
            print("- Learning tips")
            print("- Exit")

        elif user_input in ["what is ai", "what is artificial intelligence"]:
            print("Bot: Artificial Intelligence is a field of computing "
                  "that focuses on creating systems that perform tasks "
                  "associated with human intelligence.")

        elif user_input in ["what is machine learning", "define machine learning"]:
            print("Bot: Machine Learning is a branch of AI where systems "
                  "learn patterns from data to make predictions or decisions.")

        elif user_input in ["what is python", "define python"]:
            print("Bot: Python is a programming language commonly used "
                  "in areas such as automation, data science, and AI.")

        elif user_input in ["learning tip", "give me a learning tip"]:
            print("Bot: Practice one concept at a time and build small "
                  "projects to strengthen your understanding.")

        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Keep learning and improving.")
            break

        else:
            print("Bot: I'm sorry, I don't understand that question yet.")
            print("Bot: Type 'help' to see what you can ask me.")


if __name__ == "__main__":
    chatbot()