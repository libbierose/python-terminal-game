# Data Folder - DBD Trivia Game

This folder contains the data files used by the **DBD Trivia Game**. These files store questions, configuration settings, and player high scores. Keeping them separate from the Python code makes the game easy to update and maintain.

---

## **1. questions.json**

Stores all trivia questions used in the game.

**Structure of each question:**

- `question`: The trivia question text.
- `hint`: A hint for the player (used for the "Ask the Chat" lifeline).
- `answers`: A list of multiple-choice options (A, B, C, D).
- `correct`: The correct answer from the list.
- `difficulty`: The difficulty level (`easy`, `medium`, `hard`).

**Example:**

```json
{
	"question": "Which perk makes it so the gen does not make a noise when a skill check is failed?",
	"hint": "Think Technician!",
	"answers": ["Sprint Burst", "Dead Hard", "Technician", "Iron Will"],
	"correct": "Technician",
	"difficulty": "easy"
}
```

## **2. config.json**

Contains game-wide settings and paths to other data files.

Fields:

max_questions_per_game: Maximum number of questions per game session.

lifelines: Number of uses allowed per lifeline (50/50, skip_question, ask_the_chat).

leaderboard_file: Path to the leaderboard CSV file.

questions_file: Path to the questions JSON file.

shuffle_questions: Whether to randomize question order each game.

allow_replay: Whether the player can restart after finishing or failing.

Example:

```json
{
	"max_questions_per_game": 20,
	"lifelines": {
		"50/50": 1,
		"skip_question": 1,
		"ask_the_chat": 1
	},
	"leaderboard_file": "data/leaderboard.csv",
	"questions_file": "data/questions.json",
	"shuffle_questions": true,
	"allow_replay": true
}
```

## **3. leaderboard.csv**

Stores the high scores for all players.

Structure:

player: Player name

score: Score achieved in the game

Example:

```csv
player,score
Libbie,5
```
