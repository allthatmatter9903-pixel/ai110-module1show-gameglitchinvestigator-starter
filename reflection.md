# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
When I first launched the Streamlit application using python -m streamlit run app.py, the interface rendered, but the underlying game logic contained multiple severe bugs. The most obvious issue was that the hint direction was completely reversed; guessing higher than the secret number generated a prompt telling me to "Go HIGHER!". Additionally, after a couple of guesses, string and integer comparisons caused logic errors where numbers were evaluated alphabetically rather than numerically. Finally, the scoring system was faulty, adding points for incorrect higher guesses during even attempt numbers instead of deducting points.
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior  | Actual Behavior    | Console Output / Error |
|-------|--------------------|--------------------|------------------------|
| 67 |   Hint to say go lower  Hint said go higher | None
100  |  Evaluates 100>36 | Evaluated incorrectly | None
105 |   Score should decrease |   Score increased | None

---

## 2. How did you use AI as a teammate?

Throughout this project, I used GitHub Copilot as an AI coding assistant to help refactor and isolate game logic. One correct suggestion was moving check_guess(), parse_guess(), and update_score() out of app.py into logic_utils.py, which I verified by checking that imports functioned correctly in Streamlit and running pytest. On the other hand, I rejected an AI suggestion that tried to introduce complex session-state handling and an external dictionary to store player statistics inside logic_utils.py. I discarded this because it over-engineered the simple helper functions and violated the scope of keeping game logic separated from Streamlit state management.

---

## 3. Debugging and testing your fixes

I confirmed that bugs were resolved using a combination of playthroughs and automated testing with pytest. Specifically, I ran a unit test in tests/test_game_logic.py that passed a guess of 60 against a secret number of 50 to verify that check_guess() returned the expected lower hint and correctly identified the mismatch. The AI assistant helped design edge-case tests by generating pytest functions to verify handling of non-numeric string inputs and boundary inputs, ensuring invalid inputs were parsed smoothly without crashing the app.

---

## 4. What did you learn about Streamlit and state?

Streamlit operates on an execution model where the entire script re-runs from top to bottom every time a user interacts with a widget. Because standard variables reset on every script execution, st.session_state acts as a persistent memory dictionary across these reruns. Without storing variables like st.session_state.secret or st.session_state.attempts, the game would lose track of the target number and current score every time the user submits a guess.
---

## 5. Looking ahead: your developer habits

One strategy I will reuse in future projects is writing unit tests for core logic in a separate helper module before integrating it with UI components. This project changed how I view AI-generated code: while AI speeds up boilerplate creation and refactoring, it frequently introduces subtle logic and type-casting bugs that require manual line-by-line inspection. In future tasks, I will carefully review git diffs and test function returns independently rather than assuming AI code works right out of the box.
