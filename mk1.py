import streamlit as st 
st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="M",
    layout="centered",
    initial_sidebar_state="auto"
)
st.title("My First Streamlit App")
st.header("Welcome to Streamlit")
st.subheader("A quick tour of text elements")
st.text("This is plain text using st.text(). No formatting is applied.")
st.markdown("### Markdown Support")
st.markdown(
    """
    Streamlit supports **Markdown** out of the box:
    -**Bold** and *italic* text
    -[Links](https://streamlit.io)
    -`inline code`
    -Lists, tables, blockquotes and more
    >"Streamlit turns data scipts into shareable web in minutes."
    """
)
st.write("`st.write()` is the Swiss Army Knife - it renders text, numbers, DataFrames,charts, and more.")
st.caption("This is a small caption using st.caption().")
st.code("print('Hello, Streamlit!')",language="python")
st.latex(r"E = mc^2")
st.divider()
st.success(" Your first Streamilt app is running!")
