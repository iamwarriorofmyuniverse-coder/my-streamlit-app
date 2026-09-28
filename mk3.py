import streamlit as st
import random

st.title("Guess the Number (1-100)")

if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.done = False

guess = st.number_input("Enter guess:", 1, 100, disabled=st.session_state.done)

if st.button("Submit", disabled=st.session_state.done):
    st.session_state.tries += 1
    
    if guess < st.session_state.num:
        st.warning("Too low")
    elif guess > st.session_state.num:
        st.warning("Too high")
    else:
        st.success(f"Correct! Attempts: {st.session_state.tries}")
        st.session_state.done = True

if st.button("New Game"):
    st.session_state.num = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.done = False
    st.rerun()