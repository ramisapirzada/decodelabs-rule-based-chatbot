
def normalize_input(user_input):
    user_input = user_input.lower().strip()

    punctuation = "?!.,"
    for character in punctuation:
        user_input = user_input.replace(character, "")

    return user_input


def detect_intent(user_input):

    greeting_words = [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good evening"
    ]

    if user_input in greeting_words:
        return "greeting"

    elif user_input == "help":
        return "help"

    elif (
        "what is ai" in user_input
        or "what is artificial intelligence" in user_input
        or "explain ai" in user_input
        or "define ai" in user_input
        or "tell me about ai" in user_input
    ):
        return "ai"

    elif (
        "machine learning" in user_input
        or "explain ml" in user_input
        or "what is ml" in user_input
        or "tell me about machine learning" in user_input
    ):
        return "machine_learning"

    elif (
        "python" in user_input
        or "what is python" in user_input
        or "explain python" in user_input
        or "tell me about python" in user_input
    ):
        return "python"

    elif (
        "learning tip" in user_input
        or "give me a tip" in user_input
        or "study tip" in user_input
        or "give me a learning tip" in user_input
    ):
        return "learning_tip"

    elif (
        "current topic" in user_input
        or "what are we learning" in user_input
        or "what topic are we learning" in user_input
        or "which topic are we studying" in user_input
    ):
        return "current_topic"

    elif user_input in [
        "quiz",
        "start quiz",
        "take quiz",
        "test me"
    ]:
        return "quiz"

    elif user_input in [
        "bye",
        "exit",
        "quit",
        "goodbye"
    ]:
        return "exit"

    else:
        return "unknown"


def get_response(intent, current_topic):

    if intent == "greeting":
        return (
            "Hello! I am your AI Learning Companion. "
            "How can I help you today?"
        )

    elif intent == "help":
        return (
            "You can ask me about Artificial Intelligence, "
            "Machine Learning, Python, request a learning tip, "
            "or type 'quiz' to test your knowledge."
        )

    elif intent == "ai":
        return (
            "Artificial Intelligence is the field of creating "
            "systems that can perform tasks requiring "
            "human-like intelligence."
        )

    elif intent == "machine_learning":
        return (
            "Machine Learning is a branch of AI where systems "
            "learn patterns from data and improve their performance."
        )

    elif intent == "python":
        return (
            "Python is a beginner-friendly programming language "
            "commonly used in AI, data science, and automation."
        )

    elif intent == "learning_tip":
        return (
            "Learning tip: Practice coding every day and build "
            "small projects to strengthen your understanding."
        )

    elif intent == "current_topic":

        if current_topic is not None:
            return f"We are currently learning {current_topic}."

        return (
            "We have not selected a learning topic yet. "
            "Ask me about AI, Machine Learning, or Python."
        )

    elif intent == "unknown":
        return (
            "I am still learning. Try asking about AI, "
            "Machine Learning, Python, or learning tips."
        )


def get_quiz_questions(current_topic):

    if current_topic == "Python":

        return [
            {
                "question": "Which keyword is used to define a function in Python?",
                "answers": ["def"],
                "correct": "def"
            },
            {
                "question": "Which data type stores an ordered collection of items?",
                "answers": ["list"],
                "correct": "List"
            },
            {
                "question": "Which symbol is used for a single-line comment in Python?",
                "answers": ["#", "hash"],
                "correct": "#"
            }
        ]

    elif current_topic == "Machine Learning":

        return [
            {
                "question": "What is the process of learning patterns from data called?",
                "answers": ["machine learning", "ml"],
                "correct": "Machine Learning"
            },
            {
                "question": "What is used to train a machine learning model?",
                "answers": ["data", "training data"],
                "correct": "Data"
            },
            {
                "question": "Which type of learning uses labeled data?",
                "answers": ["supervised learning", "supervised"],
                "correct": "Supervised Learning"
            }
        ]

    elif current_topic == "Artificial Intelligence":

        return [
            {
                "question": "What does AI stand for?",
                "answers": [
                    "artificial intelligence",
                    "ai"
                ],
                "correct": "Artificial Intelligence"
            },
            {
                "question": "Which field focuses on enabling computers to understand human language?",
                "answers": [
                    "natural language processing",
                    "nlp"
                ],
                "correct": "Natural Language Processing"
            },
            {
                "question": "What is a system that performs tasks requiring human-like intelligence called?",
                "answers": [
                    "artificial intelligence",
                    "ai",
                    "ai system"
                ],
                "correct": "Artificial Intelligence"
            }
        ]

    else:

        return [
            {
                "question": "What does AI stand for?",
                "answers": [
                    "artificial intelligence",
                    "ai"
                ],
                "correct": "Artificial Intelligence"
            },
            {
                "question": "Which programming language is commonly used in AI?",
                "answers": [
                    "python"
                ],
                "correct": "Python"
            },
            {
                "question": "What does ML stand for?",
                "answers": [
                    "machine learning",
                    "ml"
                ],
                "correct": "Machine Learning"
            }
        ]


def run_quiz(current_topic):

    print("\n===================================")
    print("        AI KNOWLEDGE QUIZ")
    print("===================================")

    if current_topic is not None:
        print(f"Bot: Your quiz topic is {current_topic}.")

    else:
        print("Bot: This is a general AI quiz.")

    questions = get_quiz_questions(current_topic)

    score = 0

    for number, question_data in enumerate(questions, start=1):

        print(f"\nQuestion {number}:")
        print(question_data["question"])

        answer = input("You: ")
        answer = normalize_input(answer)

        if answer in question_data["answers"]:

            print("Bot: Correct! Well done.")
            score += 1

        else:

            print(
                "Bot: Incorrect. The correct answer is "
                + question_data["correct"]
                + "."
            )

    print("\n===================================")
    print("          QUIZ RESULTS")
    print("===================================")

    print(f"Bot: You scored {score} out of {len(questions)}.")

    if score == 3:

        print("Bot: Outstanding! You answered everything correctly.")

    elif score == 2:

        print("Bot: Great job! Keep practicing to improve further.")

    elif score == 1:

        print("Bot: Good effort! Review the concepts and try again.")

    else:

        print("Bot: Keep learning! Practice will help you improve.")


def chatbot():

    current_topic = None

    print("===================================")
    print("   Welcome to AI Learning Companion")
    print("===================================")
    print("Type 'help' to see available topics.")
    print("Type 'quiz' to test your knowledge.")
    print("Type 'exit' to end the conversation.\n")

    while True:

        user_input = input("You: ")

        user_input = normalize_input(user_input)

        intent = detect_intent(user_input)

        if intent == "ai":
            current_topic = "Artificial Intelligence"

        elif intent == "machine_learning":
            current_topic = "Machine Learning"

        elif intent == "python":
            current_topic = "Python"

        if intent == "exit":

            print("Bot: Goodbye! Keep learning and improving.")
            break

        elif intent == "quiz":

            run_quiz(current_topic)

        else:

            response = get_response(intent, current_topic)
            print("Bot:", response)


if __name__ == "__main__":
    chatbot()