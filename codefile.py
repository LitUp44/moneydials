import streamlit as st

# Define quiz questions and categories
questions = [
    ("When it comes to lunch, what’s your preference?", [
        ("Grab something quick and easy to save time.", "Convenience"),
        ("Grab something quick and easy to save time.", "Experiences"),
        ("Meal-prep at home so I know it’s healthy – or a salad bar.", "Health/Fitness"),
        ("Meet a friend or family member for lunch to catch up.", "Relationships")
    ]),
    ("It’s Saturday night! How do you like to spend it?", [
        ("I love to host my friends or family, whether at mine or take them out!", "Generosity"),
        ("Plan a special experience if I can manage, like a concert or unique event.", "Experiences"),
        ("Definitely use the time to work on a personal project.", "Self-Improvement"),
        ("It’s always different, I just like knowing it’s not set in stone.", "Freedom")
    ]),
    ("How do you feel about traveling?", [
        ("Love it! I want to explore as many places as possible.", "Travel"),
        ("Always happy with a weekend away to recharge.", "Freedom"),
        ("Any adventure with lots of hiking or sports works for me!", "Health/Fitness"),
        ("I love traveling in style and splurging on luxury experiences.", "Luxury"),
        ("Nah, not for me – lots to do at home!", None)
    ]),
    ("What’s your ideal work environment?", [
        ("A job that allows me to work my own hours and in whichever location I choose.", "Freedom"),
        ("An office where I can meet new people and network.", "Relationships"),
        ("Any job that lets me have long weekends for traveling or the occasional work from abroad.", "Travel"),
        ("Most important for me is feeling like I’m always improving my skills and developing.", "Self-Improvement")
    ])
]

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = "quiz"
    st.session_state.answers = {}
    st.session_state.category_scores = {}

# Step 1: Take the Quiz
if st.session_state.step == "quiz":
    st.title("📝 Lifestyle & Spending Priorities Quiz")
    
    for idx, (question, options) in enumerate(questions):
        st.write(f"**{idx + 1}. {question}**")
        selected = st.radio(f"Q{idx + 1}", [opt[0] for opt in options], key=f"q{idx}", index=None)
        
        if selected:
            for opt_text, category in options:
                if selected == opt_text:
                    st.session_state.answers[idx] = category
                    if category:
                        st.session_state.category_scores[category] = st.session_state.category_scores.get(category, 0) + 1

    if len(st.session_state.answers) == len(questions):
        if st.button("Submit Quiz"):
            st.session_state.step = "show_results"
            st.rerun()

# Step 2: Show Top Category Result
elif st.session_state.step == "show_results":
    if st.session_state.category_scores:
        top_category = max(st.session_state.category_scores, key=st.session_state.category_scores.get)
    else:
        top_category = "None (No strong preference detected)"

    st.write(f"### Your top spending category is: **{top_category}** 🎉")
    st.write("Now, let's explore how much you spend on this category.")
    
    if st.button("Continue"):
        st.session_state.top_category = top_category
        st.session_state.step = "ask_ideal_spending"
        st.rerun()

# Step 3: Ask for Ideal Spending
elif st.session_state.step == "ask_ideal_spending":
    st.write(f"### How much would you *ideally* like to spend on **{st.session_state.top_category}** per month?")
    ideal_spending = st.number_input("Enter your ideal amount ($)", min_value=0, step=10)

    if st.button("Next"):
        st.session_state.ideal_spending = ideal_spending
        st.session_state.step = "ask_actual_spending"
        st.rerun()

# Step 4: Ask for Actual Spending
elif st.session_state.step == "ask_actual_spending":
    st.write(f"### How much do you *actually* spend on **{st.session_state.top_category}** per month?")
    actual_spending = st.number_input("Enter your actual amount ($)", min_value=0, step=10)

    if st.button("See Results"):
        st.session_state.actual_spending = actual_spending
        st.session_state.step = "show_comparison"
        st.rerun()

# Step 5: Show Spending Comparison
elif st.session_state.step == "show_comparison":
    ideal = st.session_state.ideal_spending
    actual = st.session_state.actual_spending
    difference = actual - ideal

    st.write(f"### Spending Comparison for **{st.session_state.top_category}**")
    st.write(f"💡 *Ideal Spending:* **${ideal}**")
    st.write(f"💰 *Actual Spending:* **${actual}**")

    if difference > 0:
        st.write(f"🔴 You're spending **${difference} more** than your ideal budget.")
    elif difference < 0:
        st.write(f"🟢 You're spending **${abs(difference)} less** than you expected.")
    else:
        st.write("✅ Your spending perfectly aligns with your ideal budget!")

    if st.button("Restart Quiz"):
        st.session_state.clear()
        st.rerun()





