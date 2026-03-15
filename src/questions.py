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

def get_random_question():
   with open("src/data/dbd.json", "r") as file:
      data = json.load(file)
      questions = data["questions"]
      random_question = random.choice(questions)
      return Question(**random_question)
   