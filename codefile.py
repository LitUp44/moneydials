import streamlit as st

# -----------------------------
# Data Definitions (Quiz)
# -----------------------------

# List of quiz questions and answers.
# Each answer is a tuple: (category, answer_text)
questions = [
    ("1. When it comes to lunch, what’s your preference?", [
        ("Convenience", "Grab something quick and easy to save time"),
        ("Experiences", "Try out a new restaurant or café every time"),
        ("Health", "Meal-prep at home so I know it’s healthy"),
        ("Relationships", "Meet a friend or family member for lunch")
    ]),
    ("2. It’s Saturday night! How do you like to spend it?", [
        ("Generosity", "I love to host my friends or family."),
        ("Experiences", "Plan a special experience like a concert."),
        ("SelfImprovement", "Definitely work on a personal project."),
        ("Freedom", "I like not having a set plan.")
    ]),
    ("3. How do you feel about traveling?", [
        ("Travel", "Love it! I want to explore as many places as possible."),
        ("Freedom", "Always happy with a weekend away to recharge."),
        ("Health", "Any adventure with lots of hiking or sports works for me!"),
        ("Luxury", "I love traveling in style and splurging on luxury experiences."),
        ("Convenience", "Nah, not for me – lots to do at home!")
    ]),
    ("4. What’s your ideal work environment?", [
        ("Freedom", "A job that allows me to work my own hours and in whichever location I choose."),
        ("Relationships", "An office where I can meet new people and network."),
        ("Travel", "Any job that lets me have long weekends for traveling or the occasional work from abroad."),
        ("SelfImprovement", "Most important for me is feeling like I’m always improving my skills and developing.")
    ]),
    ("5. How do you approach fitness and health?", [
        ("Convenience", "Convenience matters—I like online classes or easy workout options that fit my schedule."),
        ("Health", "I’m happy to invest in a great gym or workout clothing/equipment."),
        ("Relationships", "It’s more of a social thing; I love group classes or going with friends!"),
        ("Experiences", "Fitness isn’t my main focus, but I love splurging on a wellness retreat or trying a new sport now and then.")
    ]),
    ("6. What do you spend the most 'splurge' money on every month?", [
        ("Convenience", "Meal kits to make food easier, being able to take Ubers, someone to help with cleaning or any of the above."),
        ("Travel", "Flights or trips, even if they’re short – I can’t get enough travel!"),
        ("Health", "High-quality fitness classes, health foods, or wellness apps."),
        ("SelfImprovement", "A hobby, course, or app that builds my skills."),
        ("Experiences", "Doing something new and exciting – I like to explore wherever I am and find something unique to try.")
    ]),
    ("7. You come across a windfall of cash. What’s your first thought on how to use it?", [
        ("Luxury", "No question - buy a luxury item I normally can’t afford."),
        ("Experiences", "Wahoo more money to add to my 'fun' fund for experiences with friends."),
        ("Freedom", "Straight to the bank! Best thing I can do is have more financial flexibility in the future."),
        ("Generosity", "Wow - great opportunity to donate part of it to causes I care about!")
    ]),
    ("8. Which best describes your spending philosophy?", [
        ("Luxury", "Focus on quality, even if it means spending a lot more."),
        ("Experiences", "Money is best spent on experiences over stuff. I’ll scrimp unless I get to experience something new."),
        ("SelfImprovement", "There’s no budget if it’s something that feels like it’s helping me grow and develop."),
        ("Relationships", "Extra money goes to improving relationships and treating my loved ones."),
        ("Travel", "Travel. All day. Everyday. I want to see the world.")
    ]),
    ("9. How do you typically approach learning or personal growth?", [
        ("SelfImprovement", "I regularly take online courses or attend workshops."),
        ("Travel", "I travel and experience new cultures to learn more about the world."),
        ("Health", "I engage in self-care practices or focus on activities that support my mental and physical wellness."),
        ("Relationships", "I attend networking events and connect with others who have similar goals.")
    ]),
    ("10. What’s one thing you’re willing to spend more on to treat others?", [
        ("Generosity", "I love to host dinner or throw a fun party."),
        ("Relationships", "Giving gifts or doing something special for a loved one."),
        ("Luxury", "I’ll splurge on a high-end experience or something extravagant for them."),
        ("Experiences", "Taking people on exciting adventures or trips.")
    ]),
    ("11. When it comes to your personal style, what’s most important?", [
        ("Luxury", "The brand – I like to wear pieces that make an impression"),
        ("Convenience", "Comfort and convenience; I don’t like to overthink it"),
        ("Generosity", "Buying things that reflect my values, like eco-friendly or locally made products"),
        ("Health", "Practicality, I like to be able to walk a lot or go to a workout class in my usual clothes")
    ]),
    ("12. If you could improve one area of your life, what would it be?", [
        ("Convenience", "Freeing up more time for things I enjoy by automating daily tasks"),
        ("Relationships", "Building stronger connections with friends, family, or a partner"),
        ("Generosity", "Living more generously by giving more time or money to causes I care about"),
        ("Freedom", "Increasing my ability to travel and explore new places regularly")
    ]),
    ("13. What’s your favourite way to celebrate a personal milestone?", [
        ("Luxury", "Treat myself to something luxurious and indulgent"),
        ("Travel", "Go on an exciting trip or adventure"),
        ("Generosity", "Host a gathering to share the joy with friends or family"),
        ("SelfImprovement", "Reflect on what I’ve achieved and set new goals for growth"),
        ("Freedom", "Take a day off to enjoy the freedom to do whatever I want")
    ])
]

# Explanatory texts for each category.
explanatory_texts = {
    "Travel": """**Travel:** Travel is your top money dial!! You find joy in exploring new places and cultures, valuing experiences that broaden your horizons and love to create lasting memories. You prioritise using your money to see the world even if that means you need to save in other places. Amazing - keep exploring the world!""",
    "Experiences": """**Experiences:** You have Experiences as a top money dial! It means you like to use your hard earned money to be able to do activities that bring you excitement and fulfilment, from concerts and adventures to simple moments that create meaningful stories. Your motto is likely: “let’s try something new”.""",
    "Convenience": """**Convenience:** You have Convenience as a top money dial! Convenience is all about using money to save yourself time and reduce stress; streamlining your life so you can focus on what matters most. Whether that means taking ride shares instead of transport, ordering food, or hiring a cleaner - you aim to use money to make life as easy as possible.""",
    "Luxury": """**Luxury:** You have Luxury as a top money dial! This means you appreciate high-quality items and experiences, value comfort, elegance, and the finer things in life. Nothing wrong with appreciating beauty in your life and really loving special things. Keep using your money to make your life luxurious!""",
    "Relationships": """**Relationships:** You have Relationships as a top money dial! If relationships are your priority, that means you probably enjoy using money to spend time with your family and friends. Whether hosting a dinner, buying presents for every loved one or using money to help you free up time to see them - you put people above all else.""",
    "SelfImprovement": """**Self-Improvement:** You have self-improvement as a top money dial! You like to invest in personal growth through education, skills, and tools that help you become the best version of yourself. Incredibly admirable - keep calm and carry on learning & growing!""",
    "Health": """**Health & Wellness:** You have health & wellness as a top money dial! You value spending your cash on fitness, nutrition, and mental well-being to support a vibrant, balanced lifestyle. You know better than anyone that if we don’t have our health we don’t have anything. Keep getting those expensive workout classes and treating yourself to new gym clothes!""",
    "Generosity": """**Generosity:** You have generosity as a top money dial!  This means you find fulfilment in giving to others, whether through gifts, donations, or acts of kindness that make a positive impact. This is a lovely way to spend your hard earned money - keep finding ways to give money to causes and people you care about!""",
    "Freedom": """**Freedom:** You have Freedom as a top money dial! The best way to use your money is to buy yourself flexibility, autonomy, and the ability to live life on your own terms. Whether the ability to work your own hours or change jobs as you please you like to be in control of your own time. Keep living free!"""
}

# -----------------------------
# Session State Initialization (for multi-page flow)
# -----------------------------
if "phase" not in st.session_state:
    # "quiz" → answering quiz questions.
    # "spending" → entering spending amounts for each top dial.
    # "final" → final results page.
    st.session_state.phase = "quiz"

if st.session_state.phase == "quiz":
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "scores" not in st.session_state:
        # Initialize scores for every possible category.
        all_categories = { answer[0] for _, answers in questions for answer in answers }
        st.session_state.scores = {cat: 0 for cat in all_categories}

# For spending input pages:
if st.session_state.phase == "spending":
    if "spending_index" not in st.session_state:
        st.session_state.spending_index = 0  # index for the current money dial (0, 1, 2)
    if "spending_data" not in st.session_state:
        # Will store ideal and actual amounts for each dial.
        st.session_state.spending_data = {}  # key: money dial name, value: dict with "ideal" and "actual"
    if "spending_subphase" not in st.session_state:
        # "ideal" or "actual" for the current money dial.
        st.session_state.spending_subphase = "ideal"
        
# For final results, no extra state is needed.

# -----------------------------
# Page Functions
# -----------------------------

def show_quiz():
    """Display the quiz questions one by one."""
    st.title("What are your money dials?")
    st.subheader("Where do you get the most JOY spending money?")
    
    idx = st.session_state.current_question
    question_text, answers = questions[idx]
    
    st.markdown(f"### {question_text}")
    options = [f"{answer_text}" for _, answer_text in answers]
    choice = st.radio("Select your answer:", options, key=f"question_{idx}")
    
    if st.button("Next"):
        # Update the score for the selected answer.
        for cat, answer_text in answers:
            if answer_text == choice:
                st.session_state.scores[cat] += 1
                break
        st.session_state.current_question += 1
        st.rerun()

def prepare_spending_phase():
    """After the quiz is done, compute the top three money dials and transition to spending input."""
    # Sort categories by score (highest first) and get top three (ignoring zeros).
    sorted_scores = sorted(
        st.session_state.scores.items(), key=lambda item: item[1], reverse=True
    )
    top_categories = [cat for cat, score in sorted_scores if score > 0][:3]
    if not top_categories:
        st.write("It looks like you did not answer any questions.")
        return
    st.session_state.top_dials = top_categories  # store the top 3 dials
    # Initialize spending data for each dial.
    for dial in top_categories:
        st.session_state.spending_data[dial] = {"ideal": None, "actual": None}
    st.session_state.phase = "spending"
    st.session_state.spending_index = 0
    st.session_state.spending_subphase = "ideal"
    st.rerun()

def show_spending_input():
    """Display input pages for ideal and actual spending for each top money dial."""
    current_index = st.session_state.spending_index
    top_dials = st.session_state.top_dials
    current_dial = top_dials[current_index]
    subphase = st.session_state.spending_subphase

    if subphase == "ideal":
        st.title(f"Ideal Spending for {current_dial}")
        st.subheader("How much would you ideally like to spend on this dial?")
        ideal = st.number_input("Enter your ideal amount:", min_value=0.0, value=0.0, step=1.0, key=f"ideal_{current_dial}")
        if st.button("Next"):
            st.session_state.spending_data[current_dial]["ideal"] = ideal
            # Switch to actual spending input for the same dial.
            st.session_state.spending_subphase = "actual"
            st.rerun()
    elif subphase == "actual":
        st.title(f"Actual Spending for {current_dial}")
        st.subheader("How much do you currently spend on this dial?")
        actual = st.number_input("Enter your current spending amount:", min_value=0.0, value=0.0, step=1.0, key=f"actual_{current_dial}")
        if st.button("Next"):
            st.session_state.spending_data[current_dial]["actual"] = actual
            # Move to the next dial if available.
            if current_index + 1 < len(top_dials):
                st.session_state.spending_index += 1
                st.session_state.spending_subphase = "ideal"
            else:
                # Finished input for all dials. Move to final results.
                st.session_state.phase = "final"
            st.rerun()

def show_final_results():
    """Display the final results with the three money dials and spending amounts plus a reference image."""
    st.title("Your Money Dial Spending Summary")
    top_dials = st.session_state.top_dials
    spending_data = st.session_state.spending_data

    for dial in top_dials:
        st.markdown(f"### {dial}")
        ideal = spending_data[dial]["ideal"]
        actual = spending_data[dial]["actual"]
        st.write(f"**Ideal Spending:** ${ideal:,.2f}")
        st.write(f"**Actual Spending:** ${actual:,.2f}")
        st.markdown(explanatory_texts.get(dial, ""))
        st.markdown("---")
    
    st.subheader("Reference")
    # Make sure 'reference_image.png' is in your repo or adjust the path as needed.
    st.image("reference_image.png", caption="Reference Image", use_column_width=True)
    
    if st.button("Restart All"):
        # Clear all session state variables and restart.
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# -----------------------------
# Main App Logic (Page Flow)
# -----------------------------
if st.session_state.phase == "quiz":
    # If we have not yet answered all quiz questions:
    if st.session_state.current_question < len(questions):
        show_quiz()
    else:
        # Quiz is done; prepare spending input phase.
        # (This can be triggered by a button on a results page if you want.)
        st.title("Understanding your money dials!")
        st.markdown("Your quiz is complete. Click below to proceed to spending inputs.")
        if st.button("Proceed to Spending Inputs"):
            prepare_spending_phase()
elif st.session_state.phase == "spending":
    show_spending_input()
elif st.session_state.phase == "final":
    show_final_results()

