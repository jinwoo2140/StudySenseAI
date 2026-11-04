import random


def generate_question(subject, topic, difficulty):
    """
    Generate one question based on the selected
    subject, topic and difficulty.
    """

    subject = subject.lower().strip()
    topic = topic.strip()
    difficulty = difficulty.capitalize()

    if not topic:
        raise ValueError("Please enter a topic.")

    # Temporary placeholder until Gemini integration
    # is connected.
    return {
        "subject": subject,
        "topic": topic,
        "difficulty": difficulty,
        "question": "Question generation is being prepared.",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": "Option A",
        "explanation": "This is a temporary test question."
    }
