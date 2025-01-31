import streamlit as st

# Define quiz questions and categories
questions = [
    {"question": "When it comes to lunch, what’s your preference?", "options": {
        "A. Grab something quick and easy to save time.": "Convenience",
        "B. Grab something quick and easy to save time.": "Experiences",
        "C. Meal-prep at home so I know it’s healthy – or a salad bar": "Health/Fitness",
        "D. Meet a friend or family member for lunch to catch up.": "Relationships"}},
    {"question": "It’s Saturday night! How do you like to spend it?", "options": {
        "A. I love to host my friends or family, whether at mine or take them out!": "Generosity",
        "B. Plan a special experience if I can manage, like a concert or unique event.": "Experiences",
        "C. Definitely use the time to work on a personal project.": "Self-Improvement",
        "D. It’s always different, I just like knowing it’s not set in stone.": "Freedom"}},
    {"question": "How do you feel about traveling?", "options": {
        "A. Love it! I want to explore as many places as possible.": "Travel",
        "B. Always happy with a weekend away to recharge.": "Freedom",
        "C. Any adventure with lots of hiking or sports works for me!": "Health/Fitness",
        "D. I love traveling in style and splurging on luxury experiences.": "Luxury",
        "E. Nah, not for me – lots to do at home!": "None"}},
]

# Initialize session state
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "category_scores" not in st.session_state:
    st.session_state.category_scores = {}

# Display questions one at a time
if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    st.write(f"**Question {st.session_state.current_question + 1}: {q['question']}**")
    user_choice = st.radio("Select an answer:", list(q["options"].keys()), index=None, key=f"q{st.session_state.current_question}")

    if st.button("Next"):
        if user_choice:
            category = q["options"][user_choice]
            st.session_state.answers[st.session_state.current_question] = category
            st.session_state.category_scores[category] = st.session_state.category_scores.get(category, 0) + 1
            st.session_state.current_question += 1
            st.experimental_rerun()
else:
    st.write("## Quiz Completed!")
    st.write("### Your Results:")
    for category, score in sorted(st.session_state.category_scores.items(), key=lambda x: x[1], reverse=True):
        st.write(f"**{category}: {score} points**")
    if st.button("Restart Quiz"):
        st.session_state.answers = {}
        st.session_state.current_question = 0
        st.session_state.category_scores = {}
        st.experimental_rerun()

