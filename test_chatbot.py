
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


print("All chatbot tests passed successfully!")