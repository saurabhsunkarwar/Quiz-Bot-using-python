class QuizBot:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, correct_answer):
        print(question)
        user_answer = input("Your answer: ").lower()
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.\n")

    def run_quiz(self):
        for question, answer in self.questions.items():
            self.ask_question(question, answer)
        print(f"You got {self.score} out of {len(self.questions)} questions correct.")

# Example usage
questions_dict = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal?": "Blue Whale",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
}

quiz_bot = QuizBot(questions_dict)
quiz_bot.run_quiz()
