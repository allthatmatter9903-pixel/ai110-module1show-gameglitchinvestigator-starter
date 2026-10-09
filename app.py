import streamlit as st
from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)

st.set_page_config(page_title="Game Glitch Investigator", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.write("An AI-generated guessing game. Fix the bugs to win!")

# Sidebar Settings
st.sidebar.header("Settings")
difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Normal", "Hard"], index=1)
min_val, max_val = get_range_for_difficulty(difficulty)

st.sidebar.write(f"Range: {min_val} to {max_val}")

# Initialize Session State
if "secret" not in st.session_state or st.session_state.get("difficulty") != difficulty:
    import random
    st.session_state.secret = random.randint(min_val, max_val)
    st.session_state.attempts = 0
    st.session_state.score = 100
    st.session_state.difficulty = difficulty
    st.session_state.history = []
    st.session_state.game_over = False

st.write(f"Guess a number between **{min_val}** and **{max_val}**.")

# Input Form
with st.form("guess_form"):
    raw_guess = st.text_input("Enter your guess:", key="user_input")
    submit = st.form_submit_button("Submit Guess 🚀")

if submit and not st.session_state.game_over:
    is_valid, guess, error_msg = parse_guess(raw_guess)

    if not is_valid:
        st.error(error_msg)
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess)

        status, hint = check_guess(guess, st.session_state.secret)

        if status == "Win":
            st.success(f"{hint} You guessed it in {st.session_state.attempts} attempts!")
            st.session_state.game_over = True
        else:
            st.info(hint)
            st.session_state.score = update_score(
                st.session_state.score,
                st.session_state.attempts,
                guess,
                st.session_state.secret
            )

# Display Stats
col1, col2 = st.columns(2)
col1.metric("Score", st.session_state.score)
col2.metric("Attempts", st.session_state.attempts)

if st.button("New Game 🔁"):
    st.session_state.clear()
    st.rerun()
