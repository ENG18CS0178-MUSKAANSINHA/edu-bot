import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message['content']

def summarize_topic(topic):
    prompt = f"Summarize the topic '{topic}' in simple terms for a student."
    return ask_gpt(prompt)

def generate_quiz(topic, num_questions=5):
    prompt = f"Generate {num_questions} multiple-choice questions (with answers) on '{topic}'."
    return ask_gpt(prompt)
