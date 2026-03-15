import os
import csv

class Score:
    def __init__(self, score: int = 0):
        self.score = score

    def add(self, points: int):
        self.score += points

    def reset(self):
        self.score = 0

    def get_score(self) -> int:
        return self.score
    
def save_score(name: str, score: int, filename: str = "src\\data\\leaderboard.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Score"])
        writer.writerow([name, score])

def leadboard(filename: str = "src\\data\\leaderboard.csv"):
   try:
      with open(filename, 'r') as file:
         scores = {}
            
         reader = csv.reader(file)

         next(reader)  # skip header
            
         for row in reader:
            name, score = row
            scores[name] = int(score)
            
         return scores
   except FileNotFoundError:
      return {}