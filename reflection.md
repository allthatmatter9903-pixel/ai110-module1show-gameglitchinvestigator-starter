# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

When I first ran the application using python -m streamlit run app.py, the interface rendered properly, but the underlying game logic was heavily glitched. The most obvious issue was that hint directions were reversed; entering a guess lower than the secret target prompted the app to tell me to "Go LOWER!". In addition, numerical inputs were intermittently compared as strings, resulting in alphabetical evaluation errors (e.g., treating "9" as larger than "10"). Lastly, the scoring system added points instead of deducting penalties during even-numbered attempts.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior         | Actual Behavior | Console Output / Error |
|-------|--------------------------|-----------------|------------------------|
| 2 |    Hint displays Higher      | Displays Lower | None
| 100 |  Evaluates 100>56           | Evaluates it incorrectly | None 
| 15 | Score decreases by 10 points  | Score went haywire | None

---

## 2. How did you use AI as a teammate?

Correct AI Suggestion: The AI recommended refactoring pure functions like check_guess(), parse_guess(), and update_score() out of app.py into logic_utils.py. I verified this by running pytest in the terminal to confirm the standalone logic passed all unit tests independently of Streamlit.

Rejected AI Suggestion: The AI suggested managing high-score logging by storing state inside an external dictionary and writing it to a JSON file from within logic_utils.py. I rejected this because it over-engineered helper functions, introduced unnecessary side effects, and violated the requirement of keeping logic clean and modular.
---

## 3. Debugging and testing your fixes

I verified that a bug was fixed by combining manual testing in Streamlit with automated unit testing. Specifically, I ran a unit test in tests/test_game_logic.py passing a guess of 60 against a target secret of 50, ensuring check_guess() returned ("Lower", "📉 Go LOWER!"). The AI assistant helped design unit tests by generating pytest functions that checked edge cases—such as float string inputs ("3.14") and non-numeric inputs ("abc")—confirming that parse_guess() handled errors gracefully without crashing the application.

---

## 4. What did you learn about Streamlit and state?

Streamlit operates on an execution model where the entire script re-runs from top to bottom every single time a user interacts with a widget (like typing in a text box or clicking a submit button). Standard Python variables lose their values and reset during each rerun. st.session_state acts as a persistent memory dictionary that retains values across these script executions, allowing the app to keep track of variables like secret, attempts, and score throughout a game session.
---

## 5. Looking ahead: your developer habits
One habit I will reuse in future projects is separating core business logic from UI components into utility modules and writing automated pytest suites to verify fixes before integrating them. Next time I work with AI on a coding task, I will carefully review diffs line-by-line rather than accepting bulk changes all at once. This project showed me that while AI generated code can quickly create plausible scaffolding, it frequently hides subtle logic errors and type mismatches that require careful human inspection and test-driven verification.


