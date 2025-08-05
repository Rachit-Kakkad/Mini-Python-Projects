import random

User_score = 0



get_chemistry_questions = [
    {
        "question": "Which of the following is a physical change?",
        "options": ["A. Rusting of iron", "B. Dissolving salt in water", "C. Burning of magnesium", "D. Souring of milk"],
        "answer": "B"
    },
    {
        "question": "Which of the following is not a colligative property?",
        "options": ["A. Boiling point elevation", "B. Depression of freezing point", "C. Viscosity", "D. Osmotic pressure"],
        "answer": "C"
    },
    {
        "question": "The rate of a reaction doubles when the temperature is increased by:",
        "options": ["A. 1°C", "B. 10°C", "C. 100°C", "D. 5°C"],
        "answer": "B"
    },
    {
        "question": "In electrolysis of molten NaCl, which of the following is formed at the cathode?",
        "options": ["A. Na+", "B. Na", "C. Cl-", "D. Cl₂"],
        "answer": "B"
    },
    {
        "question": "Which of the following has the highest boiling point?",
        "options": ["A. CH₄", "B. C₂H₆", "C. C₃H₈", "D. C₄H₁₀"],
        "answer": "D"
    },
    {
        "question": "The unit of molality is:",
        "options": ["A. mol L⁻¹", "B. mol kg⁻¹", "C. mol m⁻³", "D. mol mL⁻¹"],
        "answer": "B"
    },
    {
        "question": "Which of the following electrolytes has the highest conductance?",
        "options": ["A. NaCl", "B. CH₃COOH", "C. NH₄OH", "D. HCl"],
        "answer": "D"
    },
    {
        "question": "Which enzyme converts glucose to ethanol?",
        "options": ["A. Zymase", "B. Maltase", "C. Invertase", "D. Lactase"],
        "answer": "A"
    },
    {
        "question": "Which of the following statements is true for adsorption?",
        "options": ["A. It is an exothermic process", "B. It increases with temperature", "C. It is an endothermic process", "D. It always decreases surface area"],
        "answer": "A"
    },
    {
        "question": "What is the oxidation number of Mn in KMnO₄?",
        "options": ["A. +2", "B. +4", "C. +6", "D. +7"],
        "answer": "D"
    }
]

random.shuffle(get_chemistry_questions)

prefix = input("Are you (Sir / Ma'am): ").strip()

name = input(f"Enter your name, {prefix}: ").strip()

print(f"\n👋 A heartfelt welcome, {prefix} {name}!")

print("📘 This is our Class 12ᵗʰ Chemistry Quiz Challenge!\n")

print("📝 Just type A, B, C, or D to answer each question.\n")


for i, q in enumerate(get_chemistry_questions):

    print(f"Q{i+1}: {q['question']}")

    for option in q["options"]:

        print(option)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        User_score += 1
        
    else:
        print(f"❌ Wrong! Correct answer was: {q['answer']}\n")


print("🎉 Quiz Complete!")

print(f"📊 You got {User_score} out of {len(get_chemistry_questions)} correct.\n")

if User_score == len(get_chemistry_questions):
    print("🏆 Perfect score! You're a Chemistry champ!")


elif User_score >= 7:
    print("🔥 Great job! Keep revising and stay sharp!")


else:
    print("📘 Keep practicing! You're getting there!")
