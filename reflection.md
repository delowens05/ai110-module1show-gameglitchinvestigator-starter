# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  - The first time I ran it, the game was looked fine. However, when I started playing the game, I was guessing a the top ranged number, and it kept telling me to go higher. If I am guesses the. highest. number in the range, it should eitehr say my guess is right or that I should go lower.  It also told me to keep going higher even though the number I was guessing was already higher then the answer. In this case, it should tell me to guess lower. Additionally, when you pick the diffculties, it shows that each diffculy is a different range, however, when I click a difficulty, the same range 1-100 stays on the screen and does not change. Lastly, when I tried to start a new game (I pressed the button), it would not let me. So when I press the new game button, it should start a new game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used Copilot for this project, which suggested that I move the check_guess to the logic folder, actually update the prompts to refresh the game and to also fix the logic associated with how higher or lower a guess should go. These suggestions were correct and I verioed this by asking Copiolot to make a test associated with each bug found in the test folder, I then made sure it passed the test and ran the game again to make sure thsoe chnages were modified. 

- I also used chat gpt to help me with this project, which it suggested that I make sure the logic for the higher and lower guess were correct. It also suggested that I make sure the ranges of the diffulties actaully match the ranges being guessed on. Chat GPT was correct and helped me fix some of the bugs associated with these problems. In the end, i made sure the changes chat gpt told me to make were right by making sure they were fixed in the game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I decided if a bug was really fixed by asking copilot to make test for that certain bug and I also made sure to test if the actually fixes were present in the game. I sued differnt numbers and test cases myself to do this. One test that I used to verify if a bug was fixed was the test to reset a game. It made sure that when the "New Game" button was clicked on that the game actually refreshed with new attempts or new diffcuties if changed. I asked AI to ultimitly make a test that sees if pushing the "New Game" button would actually refresh the game and add new attempts. AI explained to me that it verifies if the secret guessing number is in the difficulty range, if the atremps are reset to 6, and if the status is set to play.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
