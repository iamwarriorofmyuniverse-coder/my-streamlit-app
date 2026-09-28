import streamlit as st
from datetime import datetime
st.set_page_config(
    page_title="User Profile App",
    page_icon="🚗",
    layout="centered"
)
st.title("🥷 Interactive User Profile")
st.caption("Fill in your details below and click **Generate Profile**.")
st.divider()
st.header("1. Basic Information")
name=st.text_input(
    label="Full Name",
    placeholder="e.g. Dharshan",
    help="Can't you see just Enter your first and last name"
)
age=st.number_input(
    label="Age",
    min_value=1,
    max_value=120,
    value=25,
    step=1,
    help="Can't you see just Enter your age in years"
)

st.header("2. Gender & Location")
gender=st.radio(
    label="Gender",
    options=["🚹","🚺","Non-binary","Prefer not to say"],
    horizontal=True
)
country = st.selectbox(
    label="Country",
    options=["India","United States","United Kingdom","Canada","Australia","Germany"],
    index=0
    )
st.header("3. Skills & Interests")
skills=st.multiselect(
    label="Select your skills",
    options=["Python","Java","SQL","ML","GIT","Docker","Cloud","Streamlit"
             ],
    default=["Python","Streamlit"]
    )
experience =st.slider(
    label="Years of Experience",
    min_value=0,
    max_value=40,
    value=3,
    step=1,
    )
st.header("4. Preferences")
newsletter= st.checkbox("Subscribe to newsletter 📰")
remote_ok=st.checkbox("Open to remote work 🌍")
st.divider()
submitted=st.button("⭐ Generate Profile",use_container_width=True,type="primary")