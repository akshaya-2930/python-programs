question = {
    "question": "What is the capital of India?",
    "options": {
        "A": "Mumbai",
        "B": "New Delhi",
        "C": "Chennai",
        "D": "Kolkata"
    },
    "answer": "B"
}
quiz = [
    {
        "question": "What is the capital of India?",
        "options": {"A": "Mumbai", "B": "New Delhi", "C": "Chennai", "D": "Kolkata"},
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": {"A": "O2", "B": "H2O", "C": "CO2", "D": "NaCl"},
        "answer": "B"
    }
]
score = 0

for q in quiz:
    print(q["question"])
    for key, value in q["options"].items():
        print(f"{key}. {value}")
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer is {q['answer']}.\n")

print(f"Final Score: {score}/{len(quiz)}")
