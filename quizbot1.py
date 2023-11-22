class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, answer):
        return answer.lower() == self.correct_option.lower()


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run_quiz(self):
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question.text}")
            for j, option in enumerate(question.options, 1):
                print(f"{j}. {option}")

            answer = input("Your answer (enter the number): ")
            if question.is_correct(answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_option}\n")

        print(f"You got {self.score} out of {len(self.questions)} questions correct.")


# Sample questions
question1 = Question("What is the capital of France?", ["A. London", "B. Paris", "C. Berlin", "D. Madrid"], "B")
question2 = Question("Which programming language is this quiz written in?", ["A. Java", "B. Python", "C. C++", "D. JavaScript"], "B")
question3 = Question("What is the largest planet in our solar system?", ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"], "B")

# Create a quiz
quiz = Quiz()
quiz.add_question(question1)
quiz.add_question(question2)
quiz.add_question(question3)

# Run the quiz
quiz.run_quiz()
