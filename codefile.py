import streamlit as st
import pandas as pd
import altair as alt

st.markdown(
    """
    <style>
    div[data-baseweb="radio"] label {
        font-size: 60px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def app_header():
    """Display a persistent header with the logo and main title."""
    st.image("Aligned White.png", width=200)  # Adjust width as needed.
    st.markdown(
        """
        <div style="background-color: #f5724b; padding: 10px; text-align: center; border-radius: 8px;">
            <h1 style="color: #ffeae6; margin: 0;">What are your Money Dials?</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

def quiz_subheader():
    """Display the sub-header for the quiz only."""
    st.markdown(
        """
        <div style="background-color: #8f4e52; padding: 10px; text-align: center; border-radius: 8px;">
            <p style="color: #ffeae6; margin: 5px 0 0 0; font-size: 32px;">
                Where do you get the most JOY spending money? Take the quiz and find out!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


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
# Session State Initialization (for multi-phase flow)
# -----------------------------
if "phase" not in st.session_state:
    # "quiz" → answering quiz questions.
    # "results" → showing the top money dials (quiz results) with explanatory text.
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
        
# -----------------------------
# Page Functions
# -----------------------------

import streamlit as st

# (Assuming you have your app_header() and quiz_subheader() functions defined.)

def show_quiz():
    """Display the initial quiz page.
    
    Initially shows the header, subheader, and a 'Start Now' button.
    Once the button is clicked, the quiz starts and the subheader is hidden.
    """
    # Always show the persistent header.
    app_header()
    
    # Check if the quiz has started.
    if not st.session_state.get("quiz_started", False):
        # Quiz has not started: show the subheader and a 'Start Now' button.
        quiz_subheader()
        st.markdown("<div style='padding-bottom: 20px;'></div>", unsafe_allow_html=True)
        if st.button("Start Now"):
            st.session_state.quiz_started = True
            st.rerun()
        return  # do not show any quiz questions yet.
    
    # If quiz has started, only display the header (no subheader) and then the quiz questions.
    # (Here we assume the quiz questions are managed via st.session_state.current_question.)
    if st.session_state.current_question < len(questions):
        # Display the current quiz question.
        question_text, answers = questions[st.session_state.current_question]
        st.markdown(f"### {question_text}")
        options = [answer_text for _, answer_text in answers]
        choice = st.radio("Select your answer:", options, key=f"question_{st.session_state.current_question}")
        if st.button("Next"):
            # Update the score for the selected answer.
            for cat, answer_text in answers:
                if answer_text == choice:
                    st.session_state.scores[cat] += 1
                    break
            st.session_state.current_question += 1
            st.rerun()
    else:
        # All questions answered, move on to the results phase.
        show_quiz_results()

import pandas as pd
import altair as alt
import streamlit as st

def show_quiz_results():
    """Display the quiz results with the top money dial, a vertical bar chart of all scores,
    and explanatory text for the 2nd and 3rd top money dials."""
    app_header()  # persistent header
    
    # Retrieve scores from session state; if not defined, provide an empty dict.
    scores = st.session_state.get("scores", {})
    
    if not scores:
        st.write("No scores found. It appears you have not completed the quiz.")
        return

    # Sort the scores in descending order.
    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    
    # Get the top three categories with non-zero scores.
    top_categories = [cat for cat, score in sorted_scores if score > 0][:3]
    
    if not top_categories:
        st.write("It looks like you did not answer any questions.")
        return
    
    # Display the top money dial and its explanatory text.
    st.markdown(f"## Your top money dial is: **{top_categories[0]}**")
    st.markdown(explanatory_texts.get(top_categories[0], ""))
    
    # Create a DataFrame from the scores dictionary.
    data = pd.DataFrame(list(scores.items()), columns=["Money Dial", "Score"])
    
    # Create a vertical bar chart with Altair.
    chart = alt.Chart(data).mark_bar(color="#682d24").encode(
        x=alt.X(
            "Money Dial:N",
            title="Money Dial",
            sort=alt.EncodingSortField(field="Score", op="sum", order="descending"),
            axis=alt.Axis(grid=False)
        ),
        y=alt.Y(
            "Score:Q",
            title="Points",
            axis=alt.Axis(grid=False, format="d", tickMinStep=1)
        )
    ).properties(
        width=600,
        height=400,
        title="Money Dial Scores"
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    # Display the explanatory text for the 2nd and 3rd top money dials (if available).
    if len(top_categories) > 1:
        others = top_categories[1:]
        others_str = " & ".join([f"**{cat}**" for cat in others])
        st.markdown(f"### Your other top money dials are: {others_str}")
        for cat in others:
            st.markdown(explanatory_texts.get(cat, ""))
    
    # Button to proceed to the spending inputs phase.
    if st.button("See how your spending compares!"):
        st.session_state.top_dials = top_categories
        st.session_state.spending_data = {dial: {"ideal": None, "actual": None} for dial in top_categories}
        st.session_state.phase = "spending"
        st.session_state.spending_index = 0
        st.session_state.spending_subphase = "ideal"
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
    
    # Save the top dials in session state.
    st.session_state.top_dials = top_categories
    
    # Initialize spending_data if it doesn't exist.
    if "spending_data" not in st.session_state:
        st.session_state.spending_data = {}
    
    # Initialize spending data for each dial.
    for dial in top_categories:
        st.session_state.spending_data[dial] = {"ideal": None, "actual": None}
    
    st.session_state.phase = "spending"
    st.session_state.spending_index = 0
    st.session_state.spending_subphase = "ideal"
    st.rerun()

def show_spending_input():
    """Display input pages for ideal and actual spending for each top money dial."""
    # Display the persistent header.
    app_header()
    
    current_index = st.session_state.spending_index
    top_dials = st.session_state.top_dials
    current_dial = top_dials[current_index]
    subphase = st.session_state.spending_subphase

    if subphase == "ideal":
        st.title(f"Ideal spending for {current_dial}")
        st.subheader(f"How much would you ideally like to allocate to {current_dial} per month or per year?")
        ideal = st.number_input("Ideal amount:", min_value=0.0, value=0.0, step=1.0, key=f"ideal_{current_dial}")
        if st.button("Next"):
            st.session_state.spending_data[current_dial]["ideal"] = ideal
            # Switch to actual spending input for the same dial.
            st.session_state.spending_subphase = "actual"
            st.rerun()
    elif subphase == "actual":
        st.title(f"Actual spending for {current_dial}")
        st.subheader(f"If you had to guess, how much do you currently spend on {current_dial}?")
        actual = st.number_input("Current amount:", min_value=0.0, value=0.0, step=1.0, key=f"actual_{current_dial}")
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
    """Display the final summary page with a grouped bar chart for the top 3 money dials,
    a custom explanatory message, a horizontal rule, and a reference image."""
    
    # Display the persistent header.
    app_header()
    st.title("Your Money Dial Spending Summary")
    
    # Ensure that top_dials is available.
    if "top_dials" not in st.session_state:
        st.error("Top money dials not found.")
        return
    
    # Prepare the data for the grouped bar chart.
    # st.session_state.top_dials is a list of the three top money dial names in order.
    # st.session_state.spending_data is a dictionary with keys "ideal" and "actual" for each dial.
    data = []
    for dial in st.session_state.top_dials:
        ideal = st.session_state.spending_data[dial]["ideal"]
        actual = st.session_state.spending_data[dial]["actual"]
        data.append({"Money Dial": dial, "Allocation": "Ideal", "Amount": ideal})
        data.append({"Money Dial": dial, "Allocation": "Actual", "Amount": actual})
    
    df = pd.DataFrame(data)
    
    # Create a grouped (side-by-side) bar chart using Altair.
    # Set the sort order of the Money Dial axis based on st.session_state.top_dials.
    chart = alt.Chart(df).mark_bar().encode(
        # x-axis: Money Dial with sort order defined by top_dials.
        x=alt.X("Money Dial:N", 
                title="Money Dial", 
                sort=st.session_state.top_dials,  # Use the explicit order from session state.
                axis=alt.Axis(grid=False)
        ),
        # xOffset separates the Ideal and Actual bars for each category.
        xOffset=alt.X("Allocation:N", title="Allocation"),
        # y-axis: Amount.
        y=alt.Y("Amount:Q", 
                title="Amount", 
                axis=alt.Axis(grid=False, format="d", tickMinStep=1)
        ),
        # Color encoding for the two types with your custom colours.
        color=alt.Color("Allocation:N", 
                        scale=alt.Scale(
                            domain=["Ideal", "Actual"],
                            range=["#682d24", "#ff9e70"]
                        ), 
                        title="Allocation"
        ),
        tooltip=["Money Dial", "Allocation", "Amount"]
    ).properties(
        width=200,  # width per group; adjust as needed
        height=400,
        title="Ideal vs. Actual Spending"
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    # Display the custom explanatory text.
    st.markdown(
        """
        Not every dollar spent is created equal. Some money is going to go much further for us, 
        helping us feel like we're living a life that is more or less in alignment with our values. 
        The money dials is one exercise to help us think about how in alignment we currently feel with our spending!
        """
    )
    
    # Display a horizontal rule.
    st.markdown("___")
    
    # Display the reference image.
    st.subheader("Reference")
    st.image("MoneyDials.png", caption="Reference Image", width=300)
    
    # Optional: A button to restart the entire app.
    if st.button("Restart All"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# -----------------------------
# Main App Logic (Page Flow)
# -----------------------------
if st.session_state.phase == "quiz":
    if st.session_state.current_question < len(questions):
        show_quiz()
    else:
        # When all quiz questions are answered, show the results page.
        show_quiz_results()

elif st.session_state.phase == "spending":
    show_spending_input()

elif st.session_state.phase == "final":
    show_final_results()


