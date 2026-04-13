import json
import random

class Question:
   def __init__(self, id, question, category, options, correct_answer, difficulty):
      self.id = id
      self.question = question
      self.category = category
      self.options = options
      self.correct_answer = correct_answer
      self.difficulty = difficulty

class Quiz:
   def __init__(self, questions):
      self.questions = questions
      self.current_question_index = 0
      self.score = 0
      self.total_questions = len(questions)

   def get_current_question(self):
      if self.current_question_index < self.total_questions:
         return self.questions[self.current_question_index]
      else:
         return None
   
   def increment_score(self):
      self.score += 1

   def increment_question_index(self):
      self.current_question_index += 1

def load_questions(amount = 20):
   with open("src/data/dbd.json", "r") as file:
      data = json.load(file)

   selected = random.sample(data["questions"], amount)
   
   return [Question(**q) for q in selected]


def get_random_question():
   with open("src/data/dbd.json", "r") as file:
      data = json.load(file)
      questions = data["questions"]
      random_question = random.choice(questions)
      return Question(**random_question)
   
def generate_choices(question):
   wrong_answers = random.sample([option for option in question.options if option != question.correct_answer], 3)
   choices = wrong_answers + [question.correct_answer]
   random.shuffle(choices)
   return choices

def fifty_fifty(question):
    """Remove 2 wrong answers, keep correct + 1 wrong"""
    wrong = [o for o in question.options if o != question.correct_answer]
    kept_wrong = random.sample(wrong, 1)
    return [question.correct_answer] + kept_wrong

def ask_audience(question):
    """Return simulated audience percentages"""
    choices = [c for c in question.options]
    random.shuffle(choices)
    # Simulate 70% bias toward correct answer
    percentages = {choice: random.randint(5, 15) for choice in choices}
    percentages[question.correct_answer] = 70 - sum(percentages.values())
    return percentages

def phone_friend(question):
    """70% chance of correct answer hint, 30% wrong"""
    if random.random() < 0.7:
        return question.correct_answer
    else:
        wrong = [o for o in question.options if o != question.correct_answer]
        return random.choice(wrong)