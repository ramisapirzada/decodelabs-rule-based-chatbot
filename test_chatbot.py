from chatbot import normalize_input, detect_intent


def test_normalize_input():
    assert normalize_input("  Hello! ") == "hello"


def test_greeting_intent():
    assert detect_intent("hello") == "greeting"


def test_ai_intent():
    assert detect_intent("explain ai") == "ai"


def test_machine_learning_intent():
    assert detect_intent("what is ml") == "machine_learning"


def test_python_intent():
    assert detect_intent("tell me about python") == "python"


def test_quiz_intent():
    assert detect_intent("quiz") == "quiz"


def test_exit_intent():
    assert detect_intent("bye") == "exit"


def test_unknown_intent():
    assert detect_intent("random question") == "unknown"


def run_all_tests():
    test_normalize_input()
    test_greeting_intent()
    test_ai_intent()
    test_machine_learning_intent()
    test_python_intent()
    test_quiz_intent()
    test_exit_intent()
    test_unknown_intent()

    print("All chatbot tests passed successfully!")


if __name__ == "__main__":
    run_all_tests()