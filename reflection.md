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

- I decided if a bug was really fixed by asking Copilot to create tests for that specific bug, and I also made sure to check if the fixes were actually present in the game. I used different numbers and test cases myself to do this. One test that I used to verify if a bug was fixed was testing the reset of the game. It made sure that when the "New Game" button was clicked, the game actually refreshed with new attempts or new difficulties if they were changed. I asked AI to ultimately create a test that checks if pressing the "New Game" button would actually refresh the game and add new attempts. AI explained to me that it verifies whether the secret number is within the difficulty range, if the attempts are reset to 6, and if the status is set to play.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit reruns are basically refreshing your whole program and its functionalities, which re-executes every part of your code from beginning to end. Session state is a way to save and store variables after every rerun so that during all your reruns, your variables and progress won’t disappear.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- I think one habit from this project that I want to use is the ability to use Copilot to create tests for any code fixes. I want to be able to understand why I fixed something and create a test to see if my fix is efficient. If I had to do something differently, I would probably be more specific in my specs for AI. My specs were pretty brief, not only when it came to fixing bugs, but also when creating tests. I need to be more specific with my prompts and specs so that AI can produce tests that are more accurate. Lastly, I think this project has allowed me to understand how AI solves problems in code. After it fixes one bug, it points out something else that may be wrong and gives suggestions on how to fix it without me having to ask. I also thought it was nice that AI understood all of my tasks and provided efficient solutions.
