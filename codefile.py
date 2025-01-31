import streamlit as st

# Initialize session state for tracking progress
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# Quiz questions
questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
]

# Display current question
if st.session_state.question_index < len(questions):
    q = questions[st.session_state.question_index]
    st.write(f"**Question {st.session_state.question_index + 1}: {q['question']}**")
    
    user_answer = st.radio("Select your answer:", q["options"], index=None)
    
    if st.button("Submit"):
        if user_answer:
            if user_answer == q["answer"]:
                st.session_state.score += 1
                st.success("Correct! 🎉")
            else:
                st.error(f"Wrong! The correct answer is {q['answer']}.")
            
            # Move to next question
            st.session_state.question_index += 1
            st.experimental_rerun()

else:
    st.write(f"**Quiz completed! Your final score: {st.session_state.score}/{len(questions)}**")
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.experimental_rerun()
