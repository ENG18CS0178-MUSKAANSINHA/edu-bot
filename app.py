import streamlit as st
import pandas as pd
from database import init_db, save_progress, get_progress
from utils import ask_gpt, summarize_topic, generate_quiz
import json

# Initialize DB
init_db()

st.set_page_config(page_title="EduBot", page_icon=":mortar_board:")

# Sidebar - user & topic
st.sidebar.title("EduBot")
user = st.sidebar.text_input("Enter your name", "Student")
with open("data/topics.json") as f:
    topics_data = json.load(f)
topic = st.sidebar.selectbox("Select Topic", list(topics_data.keys()))

# Sidebar - show progress
st.sidebar.subheader("Your Progress")
progress = get_progress(user)
if progress:
    df_progress = pd.DataFrame(progress, columns=["Topic", "Score", "Timestamp"])
    st.sidebar.dataframe(df_progress)
else:
    st.sidebar.write("No progress yet!")

# Main Area
st.title("EduBot - Your Personal Learning Assistant")
st.write(f"Learning Topic: **{topic}**")

# Chat / Ask Question
st.subheader("Ask a Question")
question = st.text_input("Type your question here:")
if st.button("Ask"):
    if question.strip():
        answer = ask_gpt(f"Explain '{question}' related to '{topic}' in simple terms.")
        st.markdown(f"**Answer:** {answer}")

# Summarize Topic
st.subheader("Summarize Topic")
if st.button("Summarize Topic"):
    summary = summarize_topic(topic)
    st.markdown(f"**Summary:** {summary}")

# Quiz
st.subheader("Take a Quiz")
num_questions = st.slider("Number of Questions", 1, 10, 5)
if st.button("Generate Quiz"):
    quiz_text = generate_quiz(topic, num_questions)
    st.markdown(f"**Quiz:**\n{quiz_text}")
    # Simple simulation: user scores randomly for demo
    import random
    score = random.randint(0, num_questions)
    st.write(f"Your Score: {score}/{num_questions}")
    save_progress(user, topic, score)
    st.success("Progress saved!")
