import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv


load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Title of the app
st.title('Maths QA generator')

# Combobox for selecting difficulty level
difficulty = st.selectbox('Select Difficulty Level',
                          ['Easy', 'Medium', 'Hard'])

# Combobox for selecting grade
grade = st.selectbox(
    'Select Grade', ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5'])

# Text input for writing topics
topic = st.text_input('Enter Topic')

# Function to call Gemini API


def get_math_questions(difficulty, grade, topic):
    topic = topic
    grade = grade
    difficulty = difficulty

    # Create an instance of the GenerativeModel with JSON response format
    model = genai.GenerativeModel('gemini-1.5-flash',
                                  generation_config={"response_mime_type": "application/json"})
    prompt = """
      Generate  10 maths questions along with their answers for {topic} at {difficulty} level for {grade}. Take syllabus of CBSE Board.
      Using this JSON schema:
            qa = {"question": str, "answer": str}
        Return a `list[qa]
      """

    # text_prompt = """
    #     Generate a set of 5 math questions and their corresponding answers. The questions should be based on the following criteria:

    #     - **Grade level**: {grade}
    #     - **Difficulty**: {difficulty}(easy, medium, hard)
    #     - **Topic(s)**: {topic} (e.g., addition, subtraction, multiplication, division, algebra, geometry, fractions, etc.)

    #     Each question should be formatted in a clear and concise manner, and the answers should be provided right after the questions.

    #     ### Example Criteria:
    #     - Grade: 3
    #     - Difficulty: Easy
    #     - Topic: Addition and Subtraction

    #     ### Output Format:
    #     1. Question: [Question text here]
    #     Answer: [Answer text here]

    #     2. Question: [Question text here]
    #     Answer: [Answer text here]

    #     ... (up to 5 questions)

    # """
    response = model.generate_content(prompt)
    # text_response = model.generate_content(text_prompt)
    return response.text


# Submit button
if st.button('Submit'):
    if difficulty and grade and topic:
        qa = get_math_questions(difficulty, grade, topic)
        st.write('Generated Questions and Answers:')
        st.write(qa)

    else:
        st.write("Please fill in all fields.")
