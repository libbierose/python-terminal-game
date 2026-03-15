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
   # Make sure the folder exists
   os.makedirs(os.path.dirname(filename), exist_ok=True)
    
   # Check if file exists to know whether to write header
   file_exists = os.path.exists(filename)
    
   # Open in append mode so you don't overwrite previous scores
   with open(filename, 'a', newline='') as file:
      writer = csv.writer(file)
      # Only write header if file is new
      if not file_exists:
         writer.writerow(["Name", "Score"])
      # Write the new score
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