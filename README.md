# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
  - The games purpose is to all the user to guess the secret number in a fixed amount of times, optional hints are given that tell you if the users guess is higher or lower than the secret number. You win if you guess the right number before all 6 attemps run out or you lose if you don't guess the right number before your attemps run out.
- [ ] Detail which bugs you found.
   - The bugs found in this game consisted of incorrect higher/lower comparasion, not reseting a new game correctly and displaying the wrong range of numbers for certain difficulties. 
- [ ] Explain what fixes you applied.
   - In order to fix these bugs, for the high/low comparasion, I made sure if the users number that was being guessed was higher than the secret number, than it would advise them to guess lower and vice versa. For the new game reset, I made a reset function that made sure that the secret number was in the difficulty range and at all the attemps were reset to 0. Lastly, I made sure that the ranges of the difficulies were being accurated displayed and had the accurate range. Copilot helped me identify where in the code these areas might be and gave me suggestions to fix it.

## 📸 Demo

- ![alt text](<Screenshot 2026-03-16 at 11.05.08 PM.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
